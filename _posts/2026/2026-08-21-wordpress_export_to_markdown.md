---
title: "Exporting a WordPress blog to Markdown"
date: "2026-08-21"
categories:
  - "docs-as-code"
layout: post
lang: en
---

My workflows are increasingly based on docs-as-code and Markdown. Markdown files are easy to access locally, quick to edit and search, and work well with the tools I use to build a personal knowledge base. For those reasons, I decided to move the content of my WordPress blog to Markdown.

The [wordpress-export-to-markdown](https://github.com/lonekorean/wordpress-export-to-markdown) project does exactly that: it converts a WordPress export file into Markdown files and downloads the associated media.

## Prerequisites

You need [Node.js](https://nodejs.org/) and npm installed. On Ubuntu Linux 22.04, I installed them with:

```sh
sudo apt install npm
```

Check the installation with:

```sh
node --version
npm --version
```

## Export your WordPress content

First, create a WordPress export file using the [WordPress Export tool](https://wordpress.org/support/article/tools-export-screen/). Choose **All content** unless you only want to migrate a subset of your site, then save the resulting XML file locally.

## Run the converter

The simplest way to run the converter is with `npx`:

```sh
npx wordpress-export-to-markdown
```

The program asks for the path to the WordPress XML file and then guides you through the available options. You can also provide the input file on the command line:

```sh
npx wordpress-export-to-markdown --input=/path/to/wordpress-export.xml
```

For my export, I used these options:

```sh
npx wordpress-export-to-markdown \
    --input=/path/to/wordpress-export.xml \
    --prefix-date=true \
    --date-folders=year
```

`--prefix-date=true` adds the publication date to each filename. `--date-folders=year` groups the generated posts by publication year. The remaining options can stay at their defaults, although it is worth reviewing them in the interactive prompts before starting a large export.

## Node.js version error

When I first tried this with Node.js 18.19.1, `npx` failed while loading `@inquirer/core`:

```text
file:///home/myuser/.npm/_npx/a8913a54bce5e168/node_modules/@inquirer/core/dist/lib/theme.js:1
import { styleText } from 'node:util';
                ^^^^^^^^^
SyntaxError: The requested module 'node:util' does not provide an export named 'styleText'
        at ModuleJob._instantiate (node:internal/modules/esm/module_job:123:21)
        at async ModuleJob.run (node:internal/modules/esm/module_job:191:5)
        at async ModuleLoader.import (node:internal/modules/esm/loader:336:24)
        at async loadESM (node:internal/process/esm_loader:34:7)
        at async handleMainPromise (node:internal/modules/run_main:106:12)

Node.js v18.19.1
```

This means that the installed dependency expects a newer Node.js runtime than the one being used.
As I did not want to use a newer Node.js version than supported by my Ubuntu version, I installed the converter from source instead.

## Install and run from source

If `npx` does not work in your environment, clone the converter repository and install its dependencies locally:

```sh
git clone https://github.com/lonekorean/wordpress-export-to-markdown.git
cd wordpress-export-to-markdown
npm install
```

From the repository root, run the converter with `node .`:

```sh
node . --input=/path/to/wordpress-export.xml --output=/path/to/output # ...
```

Alternatively, run it from another directory by passing the path to the local checkout:

```sh
node /path/to/wordpress-export-to-markdown # ...
```

After the export completes, review the generated Markdown and media files before publishing them.
WordPress content often contains embeds, shortcodes or formatting that needs a small amount of manual cleanup during migration.

## Summary

What I liked most about this converter is that it also preserves my tags and categories, and saves them in the front matter of each generated document.
As a next step, I'll add a static site generator (like [Sphinx](https://www.sphinx-doc.org/en/master/) or [Hugo](https://gohugo.io/)) to generate HTML pages.
In the future, I will re-publish my blog again, based on github pages.
