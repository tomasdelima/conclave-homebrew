# Maliced Lands

Maliced Lands is the settled world for this collection: an original bestiary, with spells and items to follow, for the revised fifth edition rules. Source code `ML`. The pillars below were chosen with the user and shouldn't change without them. Names of specific creatures, places, and institutions are working names until content using them ships.

## One sentence

People make monsters by feeling strongly together, and the kind of emotion shapes the kind of monster.

## How a monster is made

Any strong emotion, shared by enough people for long enough, takes flesh. Fear, grief, rage, lust, envy, longing, joy, shame, and pride all do it. None of them is special. A village that dreads its well makes a well-thing. A village that mourns a lost year of children makes something that walks the rows at harvest. A mining town's rage at the owners makes something that breaks doors at night. A parish's pride in its own godliness makes something that counts sins.

A monster is a portrait of a specific feeling, not of a mood in general. Its body, its habits, and its rules all come from the exact emotion that made it, so a monster's form is a clue to its origin and its origin is a clue to how it behaves.

Once made, a monster is real and independent. When the feeling fades, the monster doesn't. Shared emotion only governs growth: a thing fed by a household stays small, and a thing fed by a province becomes a regional power. Every monster in the world has to be destroyed by hand. There is no ritual of calm, no reconciliation, and no forgetting that unmakes one.

New monsters are still being made. Every war, plague, festival, funeral, bad harvest, and cruel new lord seeds the next generation. The bestiary is never complete in-world, and a campaign can watch a monster be born.

## What they want

Monsters want territory and subjects. They are landlords, not exterminators. A population that keeps feeling the thing that made them is the soil they grow in, so a successful monster keeps people alive, inside its domain, and feeling. "Taking over" looks different by emotion and biome: drowning a coast one boat at a time, keeping a forest village mourning by never giving the bodies back, feeding a city district's envy with one impossible fortune, owning every debt in a brothel. The goal is the same: a fed domain.

They think in dream logic. Each one is fixated and rule-bound, and its rules mirror the feeling that made it. The drowned caller only takes those who answer to their name. The grief-thing only visits those who have stopped mourning. The thing in the tavern can't touch anyone who hasn't raised a hand. You can learn a monster's rules and exploit them, and you can survive by keeping them, but you can't reason it out of what it is. Talking is possible only inside the rules, and a monster that talks is still trying to rule you.

## Who knows

Most people think the world is cursed. A few know better: certain priests, magistrates, physicians, and archivists have worked out that shared feeling breeds monsters, and they suppress the knowledge and the feeling both. Their reasoning is sound. A nation that learned the truth would feel something about it together, and that feeling would be nation-sized.

So they forbid songs and stories, break up crowds, license funerals, ban festivals in bad years, quietly move villages, and burn the records of what was killed. Working name for these institutions: the Hush. They aren't part of the bestiary, which contains monsters only, but lore entries should show their fingerprints: censored parish records, a monster whose name was outlawed, a town relocated for reasons nobody will state, a mourning period cut short by decree.

## Families by biome

Biome is the primary key, and emotion is the second. Each biome breeds monsters from whichever feelings its life produces most, usually two or three, and monsters of different emotions in the same biome compete for the same people. Each biome has its own material language so players can read origin from silhouette. Palettes are recorded in `art/prompts.json`.

| Biome | Dominant emotions | What they draw on |
| --- | --- | --- |
| Coast and sea | Fear, longing, grief | Drowning, the undertow, what the nets bring up, the fog that takes boats. Those who wait on the shore for ships that don't come back. The ones the tide never returned |
| Deep forest | Fear, grief, longing | Getting lost, being watched, what lives under the leaves. The ones left buried out there and the ones who never stopped searching. Wanting to go back to a place that isn't there anymore |
| Mountains and mines | Fear, rage, envy | Collapse, being buried alive, firedamp, the dark below. Pit disasters blamed on owners, strikes broken with blood. The seam the next crew struck |
| Walled cities | Fear, envy, pride | Neighbors, plague, the crowd, the one who governs you. The house across the square, the guild that got the contract. The certainty that this city is chosen and the rest are not |
| Urban haunts | Grief and fear in cemeteries; rage and joy in taverns; lust and shame in brothels | The dead returning and being forgotten. The violent drunk, the mob, the best night of your life. Disease, exposure, being owned, and wanting that outlives the client |

Urban haunts are the fifth family rather than a sub-line of the city, because cemeteries, taverns, and brothels each breed something so distinct that they need their own visual language.

Monsters of different emotions are not allies. A longing-born thing on the coast fights the drowned for the same widows, and may spare the party to do it, but it wants those widows too. Monster-on-monster conflict is a feature: parties can set them against each other.

## Scale

Challenge Rating is scope of feeling. The bigger the population that shares an emotion, the bigger the thing it makes.

| Scope of the feeling | CR band | Example |
| --- | --- | --- |
| One household or crew | 1/8 to 2 | The hand that grips your ankle in the shallows. The thing that sits in a dead child's chair |
| A village or parish | 3 to 8 | The fog that has taken this village's boats for three generations. The mine's rage, wearing the foreman's coat |
| A region or province | 9 to 16 | The thing the whole coast means when it says "the deep". The envy of every town that a capital has ever taxed |
| A nation or an age | 17 to 24 | Famine. Winter. Victory. The end of the world |
| Fused | 25 to 30 | Many feelings merged into one visibly composite body, a thing made of things |

Fusion is how the top of the range works. When several great feelings overlap in one population, their monsters can merge. A fused monster shows its parts: the sea-thing's drowned bulk with the plague-thing's masks grafted on and the mourners' hands reaching from its sides, each still obeying its own rules.

## Signature mechanic

Every monster is fed by the emotion that made it, and its stat block says how. Each emotion has a signature trigger. Fear is the only one that maps straight onto a printed condition, so fear-born things key on Frightened creatures. Lust-born things key on Charmed creatures. Grief-born things key on the wounded and on corpses. Rage-born things key on whoever hurt them. Envy-born things key on whoever has the most. Longing-born things key on the isolated. Joy, shame, and pride get triggers when their first monsters are designed.

Every monster can produce its own trigger, at least one of its abilities keys on it, and players can find a counter. Bonus damage, advantage, extra attacks, resistances, and healing are all in play. Refusing to give a monster what feeds it is a tactical resource: steady nerves against fear-born things, staying together against longing-born things, not striking a rage-born thing until you're ready to finish it. The full rule and the trigger table are in `docs/design-notes.md`.

## Appearance

Fully graphic. Gore, viscera, exposed anatomy, and mutilation are core visual language, for a mature table. Each family has its own materials and palette rather than a shared look. Bodies should read as the feeling made literal: the drowned are bloated and hung with net, the buried are crushed and coal-packed, the plague-thing wears the mask, longing-born things are hollow and reaching, rage-born things are torn open from the inside, joy-born things are still dancing on what's left of their feet.

Full illustrations show the whole subject in its habitat. Tokens use a close portrait inside one shared ring, a raised rim of blackened, pitted iron with a thin old-brass lip, transparent outside the circle. Keep the face or identifying feature legible on a battle map. Retain the same anatomy, colors, and distinguishing features in both versions.

## Collection scope

The campaign begins on the coast. The expanded roster now spans every CR from 1/8 through 30 and all five biome families, with nine emotional origins and fused powers at the top of the range. The complete roster is in `docs/bestiary-index.md`, and individual mechanics and playtest assumptions are in `docs/monster-playtests.md`. This is CR coverage across the collection, not a separate entry at every CR within each biome.

Spells and items stay empty until the first monsters have been at a table. When they arrive, spells should raise, dampen, or redirect shared feeling, and items should be made from monsters or made against them, with an identifiable maker.
