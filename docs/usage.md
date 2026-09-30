# Repository usage guide

This guide explains how to preview, import, and rebuild Conclave Homebrew. The repository follows the data and asset conventions of [5etools](https://github.com/5etools-mirror-3/5etools-src), with an independent local preview.

## Local preview

Open `index.html` from the repository root in a browser. The preview works directly from disk without dependencies or a server.

## Import into 5etools

Use Manage Homebrew to load `homebrew/unfinished-dawn.portable.json` from a file. The portable export embeds its images and requires no separate public image hosting. Actual import in a running 5etools instance still needs a manual check.

For a self-hosted installation, copy the source-specific directories under `img/bestiary/` and `img/bestiary/tokens/` into the corresponding directories in the installation. Import the smaller `homebrew/unfinished-dawn.json` export. Don't replace the installation's complete data indexes with this repository's indexes.

The modern [upstream renderer](https://github.com/5etools-mirror-3/5etools-src/blob/main/js/render.js) supports `tokenHref` and image `href` with internal paths or external URLs. Stat-block tags follow the [revised bestiary data format](https://github.com/5etools-mirror-3/5etools-src/blob/main/data/bestiary/bestiary-xmm.json).

## File layout

Canonical data lives in `data/`, final image assets in `img/`, and source metadata and generated exports in `homebrew/`. Setting and design notes live in `docs/`. Generation prompts and asset provenance live in `art/prompts.json`. Preview styling and behavior live in `css/` and `js/`.

## Rebuild after editing

With Python 3.9 or newer, run:

```bash
python3 scripts/build.py
```

The build validates source and lore relationships, duplicate identities, CR range, ability scores, HP arithmetic and Hit Die sizes, proficient saving throws, Passive Perception, printed damage averages, renderer tags, image existence, square tokens, and actual transparent PNG corners. It regenerates the exports and local preview.

These checks don't replace upstream schema validation, a live import test, or tabletop playtesting.
