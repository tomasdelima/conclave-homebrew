# Maliced Lands bestiary roster

One creature at each Challenge Rating from 1/8 through 30, across five clans. Challenge
Ratings are design targets, not verified balance claims. Every entry has full artwork and a
matching transparent token.

Two things shape a monster. Its **clan** is the landscape that bred it, and it decides how the
monster fights: every member of a clan carries the same plainly named trait, listed first in its
stat block. Its **emotion** is what made it, and it decides whom the monster preys on. A reader
who has met one coast monster knows how the next one moves; what changes is who it is coming for.

| Creature | CR | Clan | Clan trait | Emotion | Role | Lair |
| --- | --- | --- | --- | --- | --- | --- |
| Tidewrack Hand | 1/8 | Coast and sea | Tidebound | fear | finisher | — |
| Rootlisten | 1/4 | Deep forest | Underleaf | fear | precision hunter | — |
| Netmouth | 1/2 | Coast and sea | Tidebound | fear | conditional defender | — |
| Tallow Knocker | 1 | Mountains and mines | Deepsign | fear | retaliating striker | — |
| Drowned Caller | 2 | Coast and sea | Tidebound | fear | finisher | — |
| Shorewaiter | 3 | Coast and sea | Tidebound | longing | isolating skirmisher | — |
| Last Seat | 4 | Urban haunts | Anchored | grief | attrition threat | — |
| Haar Shepherd | 5 | Coast and sea | Tidebound | fear | finisher | — |
| Redmeasure | 6 | Mountains and mines | Deepsign | rage | retaliating striker | — |
| Window Envier | 7 | Walled cities | Crowded Ground | envy | conditional defender | — |
| Merry Unending | 8 | Urban haunts | Anchored | joy | finisher | — |
| Bellwound | 9 | Deep forest | Underleaf | grief | attrition threat | — |
| Seam Duchess | 10 | Mountains and mines | Deepsign | envy | finisher | — |
| Velvet Debt | 11 | Urban haunts | Anchored | lust | isolating skirmisher | — |
| Parish Inquisitor | 12 | Walled cities | Crowded Ground | pride | precision hunter | — |
| Pathless Mother | 13 | Deep forest | Underleaf | longing | finisher | — |
| Undertoll | 14 | Coast and sea | Tidebound | grief | attrition threat | — |
| Hushweight | 15 | Walled cities | Crowded Ground | fear | conditional defender | — |
| Pit Reprisal | 16 | Mountains and mines | Deepsign | rage | finisher | — |
| Last Dance | 17 | Urban haunts | Anchored | joy | retaliating striker | yes |
| Returned Room | 18 | Urban haunts | Anchored | grief | conditional defender | yes |
| Country Behind Trees | 19 | Deep forest | Underleaf | fear | finisher | yes |
| Nation Below | 20 | Mountains and mines | Deepsign | fear | precision hunter | yes |
| Admiralty of Absence | 21 | Coast and sea | Tidebound | longing | isolating skirmisher | yes |
| Lord of Other Windows | 22 | Walled cities | Crowded Ground | envy | finisher | yes |
| Unconfessed | 23 | Urban haunts | Anchored | shame | retaliating striker | yes |
| Crown Without Subjects | 24 | Walled cities | Crowded Ground | pride | conditional defender | yes |
| Wreck-Parish Confluence | 25 | Coast and sea | Tidebound | fear, grief | finisher | yes |
| Root-and-Rail Concord | 26 | Deep forest | Underleaf | fear, longing | precision hunter | yes |
| Furnace of the Unpaid | 27 | Mountains and mines | Deepsign | rage, envy | retaliating striker | yes |
| City That Watches | 28 | Walled cities | Crowded Ground | fear, pride | conditional defender | yes |
| House of All Last Nights | 29 | Urban haunts | Anchored | lust, shame, joy | finisher | yes |
| Country of Teeth | 30 | Confluence | Every Country at Once | fear, grief, rage, envy, longing | finisher | yes |

## Clans

| Clan | Shared trait | What it does | How a party answers it |
| --- | --- | --- | --- |
| Coast and sea | Tidebound | Advantage on attacks in, on, or above water; halved Speed and Disadvantage on dry ground | Fight it on dry rock |
| Deep forest | Underleaf | Half Cover and free movement while within 5 feet of trees, undergrowth, or its own roots | Burn the growth, or pull it into the open |
| Mountains and mines | Deepsign | Tremorsense 60 ft.; Disadvantage on attacks and no Bonus Action while a creature within 30 feet carries an uncovered open flame | Open a lamp, and accept being visible |
| Walled cities | Crowded Ground | Advantage against a creature within 5 feet of another; Disadvantage against a creature with nobody within 15 feet | Spread out |
| Urban haunts | Anchored | A named object in its space with printed AC and Hit Points gates its emotion trait | Break the object, or cover it with a cloth |
| Confluence | Every Country at Once | Carries several clans' rules in separately breakable organs | All of the above, at once |

Each clan's counter uses a different axis — terrain, cover, light, formation, an attackable
object — so no two clans play the same way.

## Emotion triggers

| Emotion | Whom it preys on |
| --- | --- |
| Fear | Frightened creatures |
| Grief | Creatures below half their Hit Points, and creatures near a corpse |
| Rage | Whoever has damaged it; worse the more different creatures join in |
| Envy | Whoever has taken no damage since the start of its last turn |
| Longing | Creatures with no conscious ally within 30 feet |
| Lust | Charmed creatures |
| Joy | Prone creatures that can hear it |
| Shame | Prone creatures with another creature within 10 feet |
| Pride | Creatures that failed a saving throw against it, except anyone willingly Prone |

## Lair actions and regional effects

The fourteen creatures at CR 17 and above each hold a domain with its own lair actions and
regional effects, recorded in `data/bestiary/legendarygroups.json` and shipped with the homebrew
exports. Below CR 17 a monster owns a household, a parish, or a province, but not a country.

## Condition interactions

Fear is not the only source of Blinded or Deafened here. Grief suppresses senses, longing binds
and moves prey, envy restrains a rival, and pride punishes a failed save. Effects keep the
durations and escape routes printed in each stat block, ordinary condition immunities still work,
and no creature gets an unlisted extra turn because a trigger is met.

## Verification status

Local structural, arithmetic, asset, and coverage checks are automated and currently pass. No
live toolset import and no tabletop balance test has been completed.
