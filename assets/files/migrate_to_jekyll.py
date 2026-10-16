#!/usr/bin/env python3
"""Convert the exported post bundles into Jekyll posts."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
DATE_PREFIX = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)$")
GERMAN_WORDS = {
    "aber",
    "auf",
    "aus",
    "das",
    "der",
    "die",
    "eine",
    "ein",
    "für",
    "ich",
    "ist",
    "mit",
    "nicht",
    "und",
    "von",
}


def post_sources(root: Path) -> list[tuple[Path, str, str]]:
    sources = []
    for year_dir in sorted(root.iterdir()):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        for post_dir in sorted(year_dir.iterdir()):
            index = post_dir / "index.md"
            if index.is_file():
                match = DATE_PREFIX.match(post_dir.name)
                if match:
                    sources.append((index, match.group(1), post_dir.name))

        for markdown in sorted(year_dir.glob("*.md")):
            match = DATE_PREFIX.match(markdown.stem)
            if match:
                sources.append((markdown, match.group(1), markdown.stem))
    return sources


def front_matter_and_body(text: str) -> tuple[str, str]:
    match = FRONT_MATTER.match(text)
    if not match:
        raise ValueError("missing YAML front matter")
    return match.group(1), text[match.end() :]


def language_for(body: str) -> tuple[str, bool]:
    words = re.findall(r"[A-Za-zÄÖÜäöüß]+", body.lower())
    german_hits = sum(word in GERMAN_WORDS for word in words)
    english_hits = sum(
        word in {"and", "are", "for", "from", "is", "not", "the", "this", "to", "with"}
        for word in words
    )
    if german_hits > english_hits and german_hits >= 2:
        return "de-DE", german_hits - english_hits < 2
    if english_hits > german_hits and english_hits >= 2:
        return "en", english_hits - german_hits < 2
    return "en", True


def add_values(front_matter: str, language: str) -> str:
    lines = front_matter.splitlines()
    existing_keys = {line.split(":", 1)[0].strip() for line in lines if ":" in line}
    additions = []
    if "layout" not in existing_keys:
        additions.append("layout: post")
    if "lang" not in existing_keys:
        additions.append(f"lang: {language}")
    return "\n".join(lines + additions)


def rewrite_images(body: str, source_dir: Path, destination: Path, asset_root: Path) -> tuple[int, str]:
    image_dir = source_dir / "images"
    if not image_dir.is_dir():
        return 0, body

    asset_dir = asset_root / destination.stem
    asset_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    for image in sorted(image_dir.iterdir()):
        if image.is_file():
            shutil.copy2(image, asset_dir / image.name)
            body = body.replace(f"images/{image.name}", f"/assets/img/posts/{destination.stem}/{image.name}")
            copied += 1
    return copied, body


def migrate(root: Path, dry_run: bool) -> int:
    posts_root = root / "_posts"
    asset_root = root / "assets" / "img" / "posts"
    review = []
    migrated = 0

    for source, year, slug in post_sources(root):
        text = source.read_text(encoding="utf-8")
        front_matter, body = front_matter_and_body(text)
        language, uncertain = language_for(body)
        match = DATE_PREFIX.match(slug)
        assert match is not None
        destination = posts_root / year / f"{slug}.md"
        if not dry_run:
            _, body = rewrite_images(body, source.parent, destination, asset_root)
        output = f"---\n{add_values(front_matter, language)}\n---\n{body}"
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(output, encoding="utf-8")
        migrated += 1
        if uncertain:
            review.append(f"{destination}: detected {language}")

    print(f"Migrated {migrated} posts")
    if review:
        print("Review language detection for:")
        print("\n".join(f"- {item}" for item in review))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return migrate(args.root.resolve(), args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
