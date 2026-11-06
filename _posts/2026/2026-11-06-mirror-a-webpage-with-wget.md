---
title: "Mirror a webpage efficiently with wget"
date: "2026-11-06"
categories:
  - "linux"
layout: post
lang: en
---

When you want to keep a local copy of a website, `wget` can download its pages and the files they need in one go.
I find that especially useful for documentation sites.
Some problem that I encountered every once in a while is that images referenced in the documentation are hosted on other domains.

The following command creates a mirror of a documentation site with external images. I've used the [iceoryx2 book](https://ekxide.github.io/iceoryx2-book/main/) URL in this example:

```sh
wget --mirror  --page-requisites --convert-links --adjust-extension --span-hosts \
  --accept-regex='^https://ekxide[.]github[.]io/iceoryx2-book/main/|[.](png|jpe?g|gif|svg|webp|ico|avif|bmp)([?].*)?$' \
  https://ekxide.github.io/iceoryx2-book/main/
```

The `--accept-regex` filter lets `wget` follow pages under that URL, and also accepts image files from other hosts.
It does not accept other external pages, so links to unrelated websites are not followed.

Here is what the options do:

- `--mirror` enables recursive downloading and timestamping, and sets options suited to making a mirror.
- `--page-requisites` downloads files needed to display each page, such as images and stylesheets.
- `--convert-links` rewrites links in downloaded pages so they point to the local copies.
- `--adjust-extension` adds an appropriate extension, such as `.html`, to downloaded pages if needed.
- `--span-hosts` allows `wget` to fetch files from other hosts; the URL filter below limits which ones it accepts.
- `--accept-regex` is a regular expression that limits which external URLs are accepted when using the `--span-hosts` option.

The image extensions in the regular expression cover common formats, and the optional query-string part allows image URLs with query parameters.

## Wrap it in a bash function

This format is not really easy to remember, and you have to write the URL twice - once with and once without regular expressions syntax.
If you plan to use this often, add this function to your `~/.bashrc` or `aliases.bash` file:

```bash
# mirror a webpage with wget
mirror() {
  echo "Using wget to create a mirror of $1"
  if [ -z "$1" ]; then
    echo "Usage: mirror <url with trailing />"
    return
  fi
  local WGET_URL="$1"
  wget --mirror --page-requisites --convert-links --adjust-extension --span-hosts \
    --accept-regex="^${WGET_URL//./[.]}|[.](png|jpe?g|gif|svg|webp|ico|avif|bmp)([?].*)?\$" $WGET_URL
}
```

After reloading your shell configuration, call it with the URL you want to mirror, including its trailing slash:

```sh
mirror <URL>
```

The function builds the URL filter regex from the address you provide and accepts the same image extensions from external hosts.
