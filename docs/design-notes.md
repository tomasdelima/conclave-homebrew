# Monster design and playtest notes

CR labels are initial design targets for revised fifth edition play, not verified balance claims. Everything here is newly authored. Nothing has been playtested or imported into a live 5etools instance yet.

## The feeding rule

Every monster in Maliced Lands has three parts. The fear-born version is spelled out below because Frightened is a printed condition; the trigger table after it covers the other emotions with the same structure.

1. **A hunger.** At least one way to impose the Frightened condition, and it should mirror the fear that made the monster. A drowned caller frightens you by speaking your name. A pit-thing frightens you when your light goes out. Prefer save-based, thematic triggers over a generic Frightful Presence.
2. **A feeding.** At least one ability that keys on Frightened creatures. Pick one or two from this list and scale with CR:
   - Bonus damage against a Frightened target
   - Advantage on attack rolls against Frightened targets
   - An extra attack or Bonus Action when a creature within 30 feet is Frightened of it
   - Resistance to all damage, or to Bludgeoning, Piercing, and Slashing, while any creature within 30 feet is Frightened of it
   - Regain Hit Points at the start of its turn for each Frightened creature within 30 feet
   - Movement or teleportation toward Frightened creatures without provoking Opportunity Attacks
   - Frightened creatures have Disadvantage on saving throws against its other effects
3. **A counter.** Something players can discover in play that turns the feeding off: a rule from the monster's origin (cover your ears, keep the lamps lit), a way to end the Frightened condition, or line of sight. The counter must be findable through observation, a lore check, or a survivor's account. A monster whose only counter is "be immune to fear" is a bad design.

Monsters of other emotions follow the same three-part structure with their own trigger. Joy, shame, and pride get rows when their first monsters are designed.

| Origin | Keys on |
| --- | --- |
| Fear-born | Frightened creatures |
| Longing-born | Creatures separated from all allies, or more than 30 feet from any ally |
| Grief-born | Creatures below half their Hit Points, and creatures adjacent to a corpse |
| Rage-born | Creatures that damaged it since its last turn; it grows by being hurt |
| Envy-born | Creatures holding more than others: the highest current Hit Points, the most magic items, the most gold |
| Lust-born | Charmed creatures |
| Joy-born | Prone creatures that can hear the monster's rhythm |
| Shame-born | Prone creatures within 10 feet of another creature, a visible witness |
| Pride-born | Creatures that failed a save against the monster since the start of its previous turn, except willingly Prone creatures |

## Damage assumptions

Compute offensive CR assuming the feeding is active half the rounds. A monster whose bonus damage only lands against Frightened targets is not a monster that deals that bonus every round. Record the with-feeding and without-feeding damage per round separately in each monster's notes, so a table can see what steady nerves buy the party.

Defensive CR counts conditional resistance at half value as well. Legendary Resistances never raise printed Hit Points.

For each monster, write down: HP formula and average, the to-hit and average damage of each attack, save DCs, the three-round damage estimate with and without feeding, and the intended counter. State the party level range it was designed against.

## Scope and CR

Scope of fear sets the band (see `docs/theme.md`). Within a band, the more literal and specific the fear, the lower the CR. A monster made from one family's dread of one particular well sits at CR 1/8 to 1. The fear a whole parish shares about the same well is CR 3 or higher, and the monster should look like it has been fed: larger, more elaborate, with more rules.

Fused monsters at CR 25 and above should carry at least two hungers and two feedings, one per merged fear, and each part should keep its own counter. Killing a fused monster in stages is the intended play pattern.

## Coast and sea starting designs

These starting concepts now have stat blocks in the full CR roster. Last Seat, Bellwound, Undertoll, and Returned Room develop grief feeding across the other tiers and biomes. Each creature has a specific feeling, a body that portrays it, a rule it obeys, and a counter.

| Working name | CR target | Feeling | Body | Rule and counter |
| --- | --- | --- | --- | --- |
| Tidewrack Hand | 1/8 | The undertow grabbing your ankle | A forearm and hand of knotted kelp and swollen grey fingers, severed at the elbow, moving under sand | Only grips in water below the knee. Stand on dry rock and it has nothing. |
| Netmouth | 1/2 | What comes up in the net | A tangle of net, hooks, and fish-gape that lies still on deck until touched | Plays dead until something warm touches it. Burn or cut the net from a distance. |
| Drowned Caller | 2 | The drowned coming back | A bloated relative, hung with weed, standing at the tideline calling names | Can only take those who answer to their name. Don't answer. Don't let the children answer. |
| Shorewaiter | 3 | Longing: those who wait for ships that never came back | A hollow, reaching figure of driftwood and salt crust, always facing the sea | Not hostile unless you take a waiting person from the shore. Hunts drowned callers for the same widows. |
| Haar Shepherd | 5 | The fog that takes boats, three generations deep | Huge, seen only as a shape in the fog, herding boats with a sound like a bell that isn't there | Feeds while it can't be seen. Fire, wind, or a real bell breaks its herding. |

Playtest order: Tidewrack Hand and Netmouth as a level 1 to 2 nuisance set, Drowned Caller as the first monster with a real rule, Shorewaiter to test how monsters of different emotions compete, Haar Shepherd as a village-scale threat for levels 4 to 6.

## Revision record

Version 0.3.0: the requested full roster covers CR 1/8, 1/4, 1/2, and 1–30 across all five biome families, all fourteen creature types, and all nine emotions. CR 25–30 creatures have multiple independently countered feedings and visible organ thresholds. See [the roster](bestiary-index.md), [individual playtest records](monster-playtests.md), and the structured calculations in `monster-notes.json`. All are unplaytested designs; no live import has been checked.

Baseline damage calculations use ordinary attacks and, where available, one two-use Legendary Attack per round. Recharge actions replace the whole action and must also be evaluated against one and two targets. The build checks arithmetic and assets; it does not certify CR. Condition durations and ally-assisted escapes are part of the intended threat budget.

Conditions use the revised [Rules Glossary](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary). Action economy follows [How to Use a Monster](https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster). No published monster design was copied.

Version 0.2.0: theme replaced. The Unfinished Dawn drafts (Glimmer Gleaner, Vesperglass Prowler, Kiln of the Ninth Dawn) were removed from the collection along with their art. They remain in git history. No monsters have been authored yet under Maliced Lands.

After each session record party composition, terrain, rounds survived, whether the counter was found and how, how many rounds the feeding was active, and adjustments. Don't inflate a CR because a creature looks imposing. Keep monster, lore, art, and token identities together when revising.
