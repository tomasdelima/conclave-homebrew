# Conclave homebrew authoring

- Read `docs/theme.md` and `docs/design-notes.md` before extending the collection. Maliced Lands is the settled theme. Change its pillars only when the user asks.
- Author original monsters, spells, items, and lore for the revised fifth edition rules. Follow the data structure and renderer-tag conventions already established in this repository; don't copy published creature designs or artwork into this collection.
- Keep canonical content under `data/`. Use source code `ML` for this setting and preserve matching monster and monsterFluff identities.
- Every monster and item needs full artwork plus a matching circular portrait token with real transparency outside its metallic ring. Derive tokens from their corresponding artwork. Store final assets as lossless WebP in this workspace and record prompts in `art/prompts.json`.
- Every monster follows the three-part rule in `docs/design-notes.md`: a clan trait shared with every other monster of its biome family and listed first, an emotion trait naming in plain words whom it preys on, and a counter the players can discover. Don't reintroduce the retired `Emotion Made Flesh`, `Rule of the Body`, `X Feeding`, or `X Hunger` template; `scripts/check_bestiary.py` rejects it.
- Stat blocks must stand alone. Name physical features inside the block (an ability that targets "a creature that can see the chair" requires the block to say the monster is a chair, with the chair's AC and Hit Points), don't restate the core rules, and keep table-safety notes in the shipped primer at `data/variantrules-ml.json` rather than in every creature.
- Creatures at CR 17 and above need a `legendaryGroup` with lair actions and regional effects in `data/bestiary/legendarygroups.json`.
- Treat CR as a playtest target. Document damage assumptions and encounter behavior. The planned eventual range is CR 1/8 through CR 30; expand only within the user's requested milestone.
- Run `python3 scripts/build.py` after changing content or assets. It rebuilds the two homebrew exports and offline preview. Don't edit those generated files directly.
- State whether a live import into a toolset and tabletop balance have been checked. Local arithmetic and asset validation don't establish either.
