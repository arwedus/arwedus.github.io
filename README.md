# Arwed's Blog

Jekyll site (theme: [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy), with
[jekyll-polyglot](https://github.com/untra/polyglot) for English / German) exported from
arwedus.wordpress.com. Published at <https://arwedus.github.io>.

## Prerequisites

- Ruby (with development headers) and Bundler: `gem install bundler`
- A C compiler and `make` (needed by some native gems)

On Debian/Ubuntu: `sudo apt install ruby-full build-essential zlib1g-dev`

## Run locally

Gems are installed into `vendor/bundle` (see `.bundle/config`), so nothing is installed system-wide.

```bash
# 1. Install dependencies (first time, and whenever Gemfile changes)
bundle install

# 2. Build and serve with live reload
bundle exec jekyll serve --livereload
```

Then open <http://127.0.0.1:4000>.

Useful variants:

```bash
bundle exec jekyll serve --drafts --future   # include drafts and future-dated posts
bundle exec jekyll build                     # one-off build into _site/
```

Note: with jekyll-polyglot, the default language (English) is served at `/` and German at `/de-DE/`.
Polyglot builds all languages at once, so builds take a bit longer than a plain Jekyll site.

## Project layout

| Path | Purpose |
|------|---------|
| `_posts/` | Blog posts |
| `_tabs/` | Sidebar pages (About, Archives, …) |
| `_data/` | Site data and translations |
| `assets/` | Images and other static files |
| `_config.yml` | Site configuration |
| `scripts/migrate_to_jekyll.py` | One-off converter for the WordPress export |

`_site/` and `.jekyll-cache/` are generated; don't edit them.

## Troubleshooting

- **Missing gems / `Could not find ...`**: run `bundle install` again.
- **Stale output**: `bundle exec jekyll clean`, then rebuild.
- **Port in use**: `bundle exec jekyll serve --port 4001`.
