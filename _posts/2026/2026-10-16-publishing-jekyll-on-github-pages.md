---
title: "Publishing a Jekyll site with a custom GitHub Actions workflow"
date: "2026-10-16"
categories:
  - "docs-as-code"
layout: post
lang: en
---

After I [migrated my WordPress blog]({% post_url 2026/2026-08-21-wordpress_export_to_markdown %}) to [a Jekyll site]({% post_url _posts/2026/2026-10-15-wordpress_export_to_jekyll %}), one very important step remained: publishing that site to <https://arwedus.github.io/>.

## Creating a Github Pages Site

I followed the [GitHub documentation on creating a GitHub Pages site with Jekyll](https://docs.github.com/en/enterprise-cloud@latest/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll) to set up the repository.
When you create a repository whose name ends with `.github.io`, GitHub automatically adds a `pages-build-deployment` workflow to the "Actions" tab.
That workflow (which does not appear in the `.github` directory of the repository) runs Jekyll and generates the site.

[The first run](https://github.com/arwedus/arwedus.github.io/actions/runs/34696283926) succeeded, but the site contained only the initial `README.md`.

### The default workflow fails with a custom theme

Then I pushed my full site with the Chirpy theme and the additional Jekyll plugins.
The [second run](https://github.com/arwedus/arwedus.github.io/actions/runs/38883038874/job/116914085266) failed.

The reason lies in how the default workflow builds your site.
It uses the `github-pages` gem, which pins Jekyll to a fixed version and allows only a short list of themes and plugins.
Chirpy and `jekyll-polyglot` are not on that list, so the build cannot load them.

Sites with a supported theme such as Minima and only whitelisted plugins have it easier.
They keep the default source, "Deploy from a branch", pick the branch and folder to publish, and need no custom Github Actions workflow file.

## Building with a custom workflow

The GitHub docs explain [how to create a custom workflow to publish your site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#creating-a-custom-github-actions-workflow-to-publish-your-site).
You can read [my workflow file](https://github.com/arwedus/arwedus.github.io/blob/main/.github/workflows/pages-deploy.yml) to put the pieces together:

`pages-deploy.yml` runs a plain `bundle exec jekyll build` with the `Gemfile` of the project.
It can therefore use any gem in any version.
It installs all dependencies, builds the site, uploads the `_site` folder as an artifact, and deploys it to GitHub Pages.

GitHub had already created the deployment environment `github-pages` along with the repository before.
The only remaining setting which needs to be changed was the publishing source, because the default, "Deploy from a branch", ignores the custom workflow.

Go to Settings → Pages → Build and deployment → Source and choose "GitHub Actions".

After the switch, the "Pages" settings offer a "Jekyll Action" to configure.
I ignored it, because my workflow was already in the repository, and saved the settings.

[The first run of my workflow](https://github.com/arwedus/arwedus.github.io/actions/runs/38886251352) succeeded.

## Summary

So, there you have it! This is how I migrated my wordpress.com blog to a Jekyll blog hosted on Github Actions.

When you're just starting out, or want to publish some pre-existing markdown files as a blog, you can simply use the [GitHub documentation on creating a GitHub Pages site with Jekyll](https://docs.github.com/en/enterprise-cloud@latest/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll), which leads you step-by-step through all steps to create and configure your generated Jekyll site locally and on `github.com`.
