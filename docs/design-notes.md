# Monster design and playtest notes

Challenge Ratings are design targets for revised fifth edition play, not verified balance claims.
Everything here is newly authored. Nothing has been playtested or imported into a live toolset
instance.

## The three-part rule

Every monster has a clan trait, an emotion trait, and a counter the players can find. A reader who
has only the stat block has everything they need; there is no shared vocabulary to look up.

1. **A clan trait.** The landscape that bred the monster decides how it fights, and every member
   of a clan carries the same plainly named trait, listed first. The trait states its own counter.
   The five clan traits and their counters are tabulated in [the setting notes](theme.md) and in
   the roster. Fused monsters carry more than one, in separately breakable organs.
2. **An emotion trait.** The feeling that made the monster decides whom it preys on, stated in
   plain words inside the trait: Frightened creatures, the wounded near a corpse, whoever struck
   it, whoever is still untouched, whoever is alone, the Charmed, the Prone who can hear it, the
   Prone with a witness, whoever just failed a save. The benefit is bonus damage, Advantage, an
   extra attack, conditional Resistance, healing, or movement, scaled to the tier.
3. **A counter.** Something a table can discover in play and then hold: a rule from the monster's
   origin, a condition to end, an object to break, a formation to keep. The counter is printed in
   the stat block and repeated in the lore entry. A monster whose only counter is "be immune to
   fear" is a bad design.

Two triggers are deliberately shaped to avoid bookkeeping and dead abilities. **Envy** keys on
whoever has taken no damage since the start of the monster's last turn, rather than on comparing
every creature's current Hit Points each round. **Rage** keeps a tally of how many different
creatures have struck it, so the party's choice is whether to nominate one striker or all pile in
— rather than an offered free attack that any competent party simply refuses.

## Ladders

These hold across the whole collection and should stay monotonic as it grows.

| Quantity | Rule |
| --- | --- |
| Save DC | One DC per monster, from a fixed ladder by CR: 11 through CR 1, then rising by 1 roughly every two CRs to 26 at CR 29–30 |
| Attack bonus | Ability modifier plus proficiency bonus, as printed |
| Raw damage per round | Rises with CR across the collection; roles create deliberate spread within a tier |
| AC and Hit Points | Rise with CR, with role-driven dips where a creature trades durability for damage |

Roles are part of the budget, not decoration. A conditional defender trades damage for
Resistance; an attrition threat trades it for healing; a finisher trades defense for damage.

## Damage assumptions

Compute offensive CR assuming the emotion trigger is live half the rounds. A monster whose bonus
damage only lands against Frightened targets does not deal that bonus every round. Record the
with-trigger and without-trigger damage separately so a table can see what steady nerves buy.

Clan traits are terrain- and formation-dependent, so every damage figure carries an assumption
about where the fight happens. Coast figures assume water; mines figures assume no uncovered open
flame within 30 feet; walled-city figures assume targets standing close together. Moving the fight
moves the numbers, which is the whole point of a clan trait.

Defensive CR counts conditional Resistance at half value. Legendary Resistances never raise
printed Hit Points. For each monster record the HP formula and average, each attack's to-hit and
average damage, the save DC, three-round damage with and without the trigger, the intended
counter, and the party level range it was designed against.

## Scope and CR

Scope of feeling sets the band (see [the setting notes](theme.md)). Within a band, the more
literal and specific the feeling, the lower the CR. One family's dread of one particular well is
CR 1/8 to 1; a whole parish's dread of the same well is CR 3 or higher, and the monster should
look fed: larger, more elaborate, with more rules.

Monsters at CR 17 and above hold a domain outright and have lair actions and regional effects.
Fused monsters at CR 25 and above carry at least two clan or emotion organs, each with its own
counter, and each breaking permanently at a printed Hit Point threshold. Killing a fused monster
in stages is the intended play pattern; breaking every organ does not kill it, and the last
stretch is fought against what is left.

## Writing a stat block

- Clan trait first, then the emotion trait, then at most one trait unique to this creature.
- Name physical features inside the block. If an ability targets "a creature that can see the
  chair", the block has to say that the monster is a chair, with the chair's AC and Hit Points.
- Do not restate the core rules. No "this does not stack", no "once per turn, not once per
  target", no answering objections that the rules already answer.
- Table-safety notes belong in the shipped primer (`data/variantrules-ml.json`), not repeated in
  every block. No ability requires a player to disclose a real secret or reveal a private
  inventory.
- Vary Multiattack, recharge values, areas, and legendary options between monsters. One shared
  legendary movement option per clan is enough to carry family resemblance.

## Revision record

Version 0.4.0: retired the `Emotion Made Flesh` / `Rule of the Body` / `X Feeding` / `X Hunger`
template across all 33 creatures and replaced it with clan traits and plainly named emotion
traits. Added lair actions and regional effects for the fourteen creatures at CR 17 and above,
and a shipped primer explaining the system to readers who only have the import. Rewrote every
lore entry as player-facing lore plus DM tactics, with a rumours list per monster. Fixed the
non-monotonic save-DC ladder, twelve adjacent-CR damage inversions, and the specific defects
recorded below. Rewrote all lore and stat-block text to stand alone. All designs remain
unplaytested; no live import has been checked.

Defects fixed in 0.4.0: the rage bonus action that a party could simply decline; envy's
current-Hit-Point comparison; Hushweight's zero-cost counter; Netmouth's resistance ending on any
Slashing damage; Window Envier's near-permanent Resistance; Shorewaiter's reaction that fled the
melee it needed; Redmeasure's reaction that provoked Opportunity Attacks every round; Haar
Shepherd's Thunder vulnerability that reduced its Speed to 0; Last Seat's and Pathless Mother's
damage and Hit Points sitting in the wrong CR bands.

Version 0.3.0: the full roster, covering CR 1/8, 1/4, 1/2, and 1–30 across all five clans, all
fourteen creature types, and all nine emotions.

Version 0.2.0: theme replaced. The Unfinished Dawn drafts were removed along with their art and
remain in git history.

## Playtest procedure

After each session record party composition, terrain, rounds survived, whether the counter was
found and how, how many rounds the trigger was live, and adjustments. Do not inflate a CR because
a creature looks imposing. Keep monster, lore, art, and token identities together when revising.

Conditions use the revised [Rules Glossary](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary).
Action economy follows [How to Use a Monster](https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster).
No published monster design was copied.
