# dnd-5e-core-en (mkdocs branch)
```
Pranav Chiploonkar <mail@pranavchip.com>
Fri 2026-07-10 08:53:31 UTC
```

> [!NOTE]
> This branch is specifically dedicated to the **Material for MkDocs** documentation site for the English translation of the `dnd-5e-core` engine. The ported codebase and raw markdown source are managed on the `main` branch.

## Project Overview
This repository is an independent English translation fork of the original project: **[codingame-team/dnd-5e-core](https://github.com/codingame-team/dnd-5e-core)**.
- **Translation:** The Python engine documentation has been translated from French to English using **Google Antigravity**.
- **Documentation Port:** The documentation structure is designed to be hosted via [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) to provide a professional, searchable, and fully-featured API reference site.

## Local Development & Setup
To view and edit the documentation webpages locally, you will need Python installed. Follow these steps to set up and serve the site:

### 1. Install Dependencies
It is recommended to use a virtual environment. Install `mkdocs-material` and its dependencies:
```bash
pip install mkdocs-material
```

### 2. Run the Development Server
Start the live-reloading development server to preview your changes:
```bash
mkdocs serve
```
Once running, open your browser and navigate to:
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### 3. Build the Static Site
To compile the documentation into static HTML files (output to a `site/` folder):
```bash
mkdocs build
```

## File Structure
```text
mkdocs
├── api                        - markdown documentation  
│   ├── core
│   │   ├── combat.md
│   │   ├── customization.md
│   │   ├── data-loading.md
│   │   ├── entities.md
│   │   ├── equipment.md
│   │   ├── magic-spells.md
│   │   ├── rules-mechanics.md
│   │   └── ui-utilities.md
│   ├── index.md
│   └── stylesheets
│       └── catppuccin.css
├── docs                       - static site
├── LICENSE
├── mkdocs.yaml                - mkdocs config file
└── README.md                  - you are here!
```

## Theme & Customization
The site is configured using the popular **Material for MkDocs** theme, enhanced with a customized **Catppuccin Mocha** color palette stylesheet (`api/stylesheets/catppuccin.css`) from the [Catppuccin](https://catppuccin.com/) project.

## Maintenance & Support Policy
> [!WARNING]
> **No support, active development, or maintenance will be provided in this repository.**
> This is a static translation port designed solely for convenience.
- For issues regarding English spelling, translation quality, or the MkDocs layout on this branch, please submit a Pull Request directly to this repository.
- For all engine bugs, feature requests, or queries regarding the core codebase, please refer to the upstream repository: **[codingame-team/dnd-5e-core](https://github.com/codingame-team/dnd-5e-core)**.
