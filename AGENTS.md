# Conclave homebrew authoring

- Read `docs/theme.md` and `docs/design-notes.md` before extending the collection. The Unfinished Dawn is provisional until the user settles the theme.
- Author original monsters, spells, items, and lore for the revised fifth edition rules. Use upstream 5etools for data structure and renderer conventions; don't copy published creature designs or artwork into this collection.
- Keep canonical content under `data/`. Use source code `UD` for this setting and preserve matching monster and monsterFluff identities.
- Every monster and item needs full artwork plus a matching circular portrait token with real transparency outside its metallic ring. Derive tokens from their corresponding artwork. Store final assets in this workspace and record prompts in `art/prompts.json`.
- Treat CR as a playtest target. Document damage assumptions and encounter behavior. The planned eventual range is CR 1/8 through CR 30; expand only within the user's requested milestone.
- Run `python3 scripts/build.py` after changing content or assets. It rebuilds the two homebrew exports and offline preview. Don't edit those generated files directly.
- State whether live 5etools import and tabletop balance have been checked. Local arithmetic and asset validation don't establish either.
