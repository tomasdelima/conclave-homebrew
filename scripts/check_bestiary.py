#!/usr/bin/env python3
"""Check the Maliced Lands roster contract and its authored design records."""

import json
from build import ROOT, dice_average, require


def read(path):
    return json.loads((ROOT / path).read_text())


def main():
    monsters = read("data/bestiary/bestiary-ml.json")["monster"]
    roster = read("docs/roster.json")
    notes = read("docs/monster-notes.json")
    names = {m["name"] for m in monsters}
    require(names == {m["name"] for m in roster} == {m["name"] for m in notes}, "Design records and monsters differ")
    require(len(names) == len(monsters) == len(roster) == len(notes), "Duplicate identities")
    require({"1/8", "1/4", "1/2", *(str(i) for i in range(1, 31))} <= {m["cr"] for m in monsters}, "Missing CR tier")
    require({"coast", "forest", "mines", "city", "haunts"} <= {m["biome"] for m in roster}, "Missing biome family")
    require({"fear", "grief", "longing", "rage", "envy", "joy", "lust", "shame", "pride"} <= {e for m in notes for e in m["emotions"]}, "Missing emotional family")
    require({"aberration", "beast", "celestial", "construct", "dragon", "elemental", "fey", "fiend", "giant", "humanoid", "monstrosity", "ooze", "plant", "undead"} <= {m["type"] for m in monsters}, "Missing creature type")
    by_name = {m["name"]: m for m in monsters}
    for n in notes:
        m = by_name[n["name"]]
        require(m["source"] == "ML" and m["cr"] == n["cr"], f"Source/CR mismatch: {m['name']}")
        require(not set(m.get("immune", [])) & set(m.get("resist", [])), f"Redundant defenses: {m['name']}")
        require(n["hpFormula"] == m["hp"]["formula"] and n["hpAverage"] == m["hp"]["average"], f"Stale HP notes: {m['name']}")
        require(n["attackAverage"] == dice_average(n["attackFormula"]), f"Stale attack notes: {m['name']}")
        require(n["rawDprWithoutFeeding"] == n["attackAverage"] * n["attacksPerMultiattack"] + n["legendaryAttackAveragePerRound"], f"Incorrect damage baseline: {m['name']}")
        require(n["rawDprHalfFeeding"] == (n["rawDprWithoutFeeding"] + n["rawDprWithFeeding"]) / 2, f"Incorrect feeding midpoint: {m['name']}")
        for suffix in ("WithoutFeeding", "WithFeeding", "HalfFeeding"):
            require(n["threeRoundDamage" + suffix] == 3 * n["rawDpr" + suffix], f"Incorrect three-round model: {m['name']}")
        traits = {t["name"]: t for t in m["trait"]}
        bonus = {b["name"] for b in m["bonus"]}
        require("Rule of the Body" in traits and n["counter"] in traits["Rule of the Body"]["entries"], f"Counter mismatch: {m['name']}")
        for emotion in n["emotions"]:
            hunger = emotion.title() + " Hunger"
            require(emotion.title() + " Feeding" in traits and any(b == hunger or b.startswith(hunger + " (") for b in bonus), f"Incomplete hunger loop: {m['name']}")
        if n["stages"]:
            stage_text = " ".join(traits["Divided Body"]["entries"])
            thresholds = [s["hpThreshold"] for s in n["stages"]]
            require(thresholds == sorted(set(thresholds), reverse=True), f"Invalid stage order: {m['name']}")
            require(all(0 < v < m["hp"]["average"] for v in thresholds), f"Invalid stage HP: {m['name']}")
            require(all(str(s["hpThreshold"]) in stage_text and s["organ"] in stage_text for s in n["stages"]), f"Stale stage notes: {m['name']}")
    assets = read("art/prompts.json")["assets"]
    lore = {m["name"]: m for m in read("data/bestiary/fluff-bestiary-ml.json")["monsterFluff"]}
    relevant = [a for a in assets if a["name"] in names]
    require(len(relevant) == 2 * len(names), "Each monster requires exactly two prompt records")
    for name in names:
        pair = [a for a in relevant if a["name"] == name]
        require({a["kind"] for a in pair} == {"full-art", "token"}, f"Missing art/token record: {name}")
        full = "img/" + lore[name]["images"][0]["href"]["path"]
        token = "img/" + by_name[name]["tokenHref"]["path"]
        for a in pair:
            require(a["path"] == (token if a["kind"] == "token" else full), f"Asset reference mismatch: {name}")
            if a["kind"] == "token":
                require(a.get("derived_from") == full, f"Missing token derivation: {name}")
            path = ROOT / a["path"]
            require(path.is_file() and path.suffix == ".webp", f"Missing WebP: {path}")
            data = path.read_bytes()
            # VP8L is the lossless WebP image chunk. Search parsed RIFF chunks,
            # rather than assuming it is the first chunk after metadata.
            offset, chunks = 12, []
            while offset + 8 <= len(data):
                kind = data[offset:offset + 4]
                size = int.from_bytes(data[offset + 4:offset + 8], "little")
                chunks.append(kind)
                offset += 8 + size + (size % 2)
            require(b"VP8L" in chunks and b"VP8 " not in chunks, f"Asset is not lossless: {path}")
    print(f"Roster checks passed: {len(names)} monsters; complete CR, biome, emotion, and type coverage; matching damage/stage notes and lossless artwork records.")


if __name__ == "__main__":
    main()
