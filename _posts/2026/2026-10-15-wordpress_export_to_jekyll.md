---
title: "From WordPress export to a Jekyll site"
date: "2026-10-15"
layout: post
lang: en
---

In [the previous post]({% post_url 2026/2026-08-21-wordpress_export_to_markdown %}) I converted my WordPress blog into Markdown files. This post covers the second half: turning those files into a working [Jekyll](https://jekyllrb.com/) site that I can publish on GitHub Pages.

## Starting point

The converter left me with one folder per year. Each post is either a single `YYYY-MM-DD-slug.md` file, or a `YYYY-MM-DD-slug/` folder containing an `index.md` and an `images/` subfolder:

```text
2014/
  2014-01-02-windows-cddvd-brennen-ohne-adminrechte/
    index.md
    images/screenshot.png
2015/
  2015-03-04-some-post.md
```

Jekyll expects something slightly different: posts in `_posts/<year>/YYYY-MM-DD-slug.md`, a `layout` in the front matter, and static files somewhere under the site root.

## Choosing a theme

I use the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme, which gives me a sidebar, categories, tags, an archive and dark mode out of the box. Since my blog mixes English and German posts, I added [jekyll-polyglot](https://github.com/untra/polyglot) for a bilingual site: English is served at `/`, German at `/de-DE/`. The relevant parts of `_config.yml` are:

```yaml
theme: jekyll-theme-chirpy

plugins:
  - jekyll-polyglot

languages: ["en", "de-DE"]
exclude_from_localization: ["assets", "fonts", "css", "js"]
```

Polyglot needs a `lang` value in each post's front matter, which the WordPress export does not contain. That is one of the things the migration script takes care of.

## The migration script

Instead of fixing 62 posts by hand, I let Claude write a small Python script. It uses only the standard library:

**[Download migrate_to_jekyll.py]({{ '/assets/files/migrate_to_jekyll.py' | relative_url }})**

For every exported post, it does the following:

1. **Finds the posts.** It walks the year folders and picks up both `slug.md` files and `slug/index.md` bundles whose name starts with a date.
2. **Moves them into place.** Each post is written to `_posts/<year>/<date>-<slug>.md`.
3. **Completes the front matter.** If missing, it adds `layout: post` and a `lang` value. The original `title`, `date`, tags and categories are kept as they are.
4. **Guesses the language.** The script counts common German and English stop words in the text and picks the language with more hits. When the result is close, it lists the post at the end so that I can check it manually.
5. **Copies the images.** Files from a post's `images/` folder go to `assets/img/posts/<date>-<slug>/`, and the relative `images/...` links in the text are rewritten to the new absolute paths.

Two caveats: the language detection is a heuristic, so short posts or posts with a lot of code can be misclassified. And the script is a one-off tool written for my export layout, so expect to adapt it if your converter options differ (I used `--prefix-date=true` and `--date-folders=year`).

Of course, I did this conversion step because of my personal preferences. I could have used the converter output as-is.

## Building the site

After the migration, I built the Jenkins site locally to fix any conversion errors (like missing assets, broken links...):

```sh
bundle install
bundle exec jekyll serve --livereload
```

## Alternatives

My route, with a converter plus a custom script, was not the shortest one. If you do not have special requirements, such as a bilingual site or a particular folder layout, one of these is likely easier:

- **[Jekyll Exporter](https://github.com/benbalter/wordpress-to-jekyll-exporter)**: a WordPress plugin that exports your site as a ZIP file that is already a Jekyll site, with posts in `_posts`, front matter, and uploads included. This is probably the easiest option if you can install plugins on your WordPress instance. It does not work with a hosted wordpress.com site on a plan without plugin support, which was my situation.
- **[jekyll-import](https://import.jekyllrb.com/)**: Jekyll's official importer gem. It reads a WordPress XML export (or the database directly) and writes Jekyll posts. It is a good fit if you start from the same XML file as I did, but it needs a bit of Ruby scripting and does less for images and cleanup than my approach.
- **[Pandoc](https://pandoc.org/)**: a general document converter. It can convert the HTML of single posts to Markdown, but you would have to take care of the front matter and the file layout yourself.

## Summary

Getting from the WordPress export to Jekyll came down to two steps: the exporter produced Markdown, and a short script moved it into Jekyll's layout, added the missing front matter and fixed the image links. If you can use the Jekyll Exporter plugin, start there. If not, feel free to take the [script](/assets/files/migrate_to_jekyll.py) and adapt it to your own export.
