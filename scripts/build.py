#!/usr/bin/env python3
"""Validate local content and build 5etools homebrew exports and an offline preview."""

import base64
import copy
from fractions import Fraction
import html
import json
import math
from pathlib import Path
import re
import struct
import subprocess
import zlib

ROOT = Path(__file__).resolve().parents[1]
ABILITIES = ("str", "dex", "con", "int", "wis", "cha")
SECTIONS = {"trait": "Traits", "action": "Actions", "bonus": "Bonus Actions", "reaction": "Reactions", "legendary": "Legendary Actions"}


def read(path):
    return json.loads((ROOT / path).read_text())


def write_json(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def dice_average(formula):
    match = re.fullmatch(r"(\d+)d(\d+)(?:\s*([+-])\s*(\d+))?", formula)
    require(match, f"Unsupported dice formula: {formula}")
    count, sides, sign, extra = match.groups()
    return int(count) * (int(sides) + 1) / 2 + (int(extra or 0) * (-1 if sign == "-" else 1))


def image_info(path):
    """Read dimensions and actual alpha range without changing generated images."""
    data = path.read_bytes()
    if path.suffix.lower() == ".webp":
        require(data[:4] == b"RIFF" and data[8:12] == b"WEBP", f"Expected WebP: {path}")
        try:
            result = subprocess.run(
                ["dwebp", str(path), "-quiet", "-o", "-"],
                check=True, capture_output=True, timeout=30,
            )
        except FileNotFoundError as exc:
            raise ValueError("WebP validation requires dwebp from the libwebp tools; on macOS run brew install webp") from exc
        data = result.stdout
    require(data[:8] == b"\x89PNG\r\n\x1a\n", f"Expected PNG: {path}")
    width, height, depth, color, _, _, interlace = struct.unpack(">IIBBBBB", data[16:29])
    if color != 6:
        return width, height, None
    require(depth == 8 and interlace == 0, f"Unsupported RGBA PNG layout: {path}")
    compressed = bytearray()
    offset = 8
    while offset < len(data):
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8]
        if kind == b"IDAT":
            compressed.extend(data[offset + 8:offset + 8 + length])
        offset += 12 + length
    pixels = zlib.decompress(compressed)
    stride = width * 4
    previous = bytearray(stride)
    minimum, maximum = 255, 0
    corners = []
    for y in range(height):
        offset = y * (stride + 1)
        filter_type = pixels[offset]
        row = bytearray(pixels[offset + 1:offset + 1 + stride])
        require(filter_type <= 4, f"Unknown PNG filter: {path}")
        for x in range(stride):
            left = row[x - 4] if x >= 4 else 0
            up = previous[x]
            upper_left = previous[x - 4] if x >= 4 else 0
            if filter_type == 1:
                predictor = left
            elif filter_type == 2:
                predictor = up
            elif filter_type == 3:
                predictor = (left + up) // 2
            elif filter_type == 4:
                p = left + up - upper_left
                distances = (abs(p - left), abs(p - up), abs(p - upper_left))
                predictor = (left, up, upper_left)[distances.index(min(distances))]
            else:
                predictor = 0
            row[x] = (row[x] + predictor) & 255
        alpha = row[3::4]
        minimum, maximum = min(minimum, min(alpha)), max(maximum, max(alpha))
        if y in (0, height - 1):
            corners.extend((alpha[0], alpha[-1]))
        previous = row
    return width, height, (minimum, maximum, corners)


def image_path(href):
    require(href["type"] == "internal", "Canonical images must have internal paths")
    path = (ROOT / "img" / href["path"]).resolve()
    require(path.is_relative_to(ROOT / "img"), "Image path escapes img/")
    require(path.is_file(), f"Missing image: {path.relative_to(ROOT)}")
    return path


def validate(pack):
    sources = {source["json"] for source in pack["_meta"]["sources"]}
    monsters = pack["monster"]
    lore = {(entry["name"], entry["source"]): entry for entry in pack["monsterFluff"]}
    names = set()
    require(len(lore) == len(pack["monsterFluff"]), "Duplicate lore entries")
    for mon in monsters:
        identity = (mon["name"], mon["source"])
        require(identity not in names, f"Duplicate monster: {identity}")
        names.add(identity)
        require(mon["source"] in sources, f"Unknown source: {identity}")
        require(identity in lore, f"Missing lore: {identity}")
        cr = Fraction(mon["cr"])
        require(Fraction(1, 8) <= cr <= 30, f"CR out of range: {identity}")
        pb = 2 if cr < 5 else 2 + (math.ceil(cr) - 1) // 4
        for ability in ABILITIES:
            require(1 <= mon[ability] <= 30, f"Invalid ability: {identity} {ability}")
        require(mon["hp"]["average"] == math.floor(dice_average(mon["hp"]["formula"])), f"Incorrect HP average: {identity}")
        hp_match = re.fullmatch(r"(\d+)d(\d+)\s*\+\s*(\d+)", mon["hp"]["formula"])
        require(hp_match is not None, f"Expected HP formula with Constitution: {identity}")
        count, sides, extra = map(int, hp_match.groups())
        require(sides == {"T": 4, "S": 6, "M": 8, "L": 10, "H": 12, "G": 20}[mon["size"][0]], f"Incorrect Hit Die: {identity}")
        require(extra == count * ((mon["con"] - 10) // 2), f"Incorrect HP Constitution bonus: {identity}")
        for ability, bonus in mon.get("save", {}).items():
            require(int(bonus) == (mon[ability] - 10) // 2 + pb, f"Incorrect proficient save: {identity} {ability}")
        require(mon["passive"] == 10 + int(mon.get("skill", {}).get("perception", (mon["wis"] - 10) // 2)), f"Incorrect Passive Perception: {identity}")
        text = json.dumps(mon)
        for displayed, formula in re.findall(r"(\d+) \(\{@damage ([^}]+)\}\)", text):
            require(int(displayed) == math.floor(dice_average(formula)), f"Incorrect damage average: {identity} {formula}")
        allowed_tags = {"atkr", "hit", "h", "damage", "recharge", "actSave", "dc", "actSaveFail", "actSaveSuccess"}
        require(set(re.findall(r"\{@(\w+)", text)) <= allowed_tags, f"Unknown renderer tag: {identity}")
        token = image_path(mon["tokenHref"])
        width, height, alpha = image_info(token)
        require(width == height, f"Token isn't square: {identity}")
        require(alpha and alpha[0] == 0 and alpha[1] == 255 and alpha[2] == [0, 0, 0, 0], f"Token requires real transparent corners and opaque art: {identity}")
        for image in lore[identity]["images"]:
            path = image_path(image["href"])
            width, height, _ = image_info(path)
            image["width"], image["height"] = width, height
        print(f"Validated {mon['name']}: CR {mon['cr']}, PB +{pb}, HP and damage dice, lore, artwork, transparent token")
    require(set(lore) == names, "Lore and monsters don't match")


def image_data_url(path):
    mime = {".png": "image/png", ".webp": "image/webp"}.get(path.suffix.lower())
    require(mime, f"Unsupported image format: {path}")
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def embed_images(pack):
    portable = copy.deepcopy(pack)
    for mon in portable["monster"]:
        path = image_path(mon["tokenHref"])
        mon["tokenHref"] = {"type": "external", "url": image_data_url(path)}
    for lore in portable["monsterFluff"]:
        for image in lore["images"]:
            path = image_path(image["href"])
            image["href"] = {"type": "external", "url": image_data_url(path)}
    return portable


def readable(text):
    def replace(match):
        tag, value = match.group(1), (match.group(2) or "").strip()
        values = {
            "atkr": "Melee Attack Roll:" if value == "m" else "Ranged Attack Roll:",
            "hit": f"{int(value):+}" if tag == "hit" else "",
            "h": "Hit:",
            "recharge": f"(Recharge {value}–6)",
            "actSave": {"dex": "Dexterity", "con": "Constitution", "str": "Strength", "wis": "Wisdom"}.get(value, value) + " Saving Throw:",
            "dc": f"DC {value}",
            "actSaveFail": "Failure:",
            "actSaveSuccess": "Success:",
        }
        return values.get(tag, value.split("|")[0])
    return html.escape(re.sub(r"\{@(\w+)(?: ([^}]*))?\}", replace, text))


def entries_html(entries):
    parts = []
    for entry in entries:
        if isinstance(entry, str):
            parts.append(f"<p>{readable(entry)}</p>")
        else:
            parts.append(f"<h3>{readable(entry['name'])}</h3>" + entries_html(entry["entries"]))
    return "".join(parts)


def preview(pack):
    lore = {(entry["name"], entry["source"]): entry for entry in pack["monsterFluff"]}
    cards = []
    links = []
    sizes = {"T": "Tiny", "L": "Large", "H": "Huge"}
    alignments = {"U": "Unaligned", "L": "Lawful", "N": "Neutral"}
    for mon in pack["monster"]:
        name = html.escape(mon["name"])
        slug = re.sub(r"[^a-z0-9]+", "-", mon["name"].lower())
        fluff = lore[(mon["name"], mon["source"])]
        art = "img/" + fluff["images"][0]["href"]["path"]
        token = "img/" + mon["tokenHref"]["path"]
        links.append(f'<a href="#{slug}">{name} <small>CR {mon["cr"]}</small></a>')
        speeds = []
        for kind, value in mon["speed"].items():
            if kind == "canHover":
                continue
            number = value["number"] if isinstance(value, dict) else value
            suffix = " " + value.get("condition", "") if isinstance(value, dict) else ""
            speeds.append(f"{kind.title()} {number} ft.{suffix}")
        initiative = (mon["dex"] - 10) // 2
        if mon.get("initiative", {}).get("proficiency"):
            cr = Fraction(mon["cr"])
            initiative += 2 + (math.ceil(cr) - 1) // 4 if cr >= 5 else 2
        ability_html = "".join(f'<div><b>{ability.upper()}</b><span>{mon[ability]} ({(mon[ability] - 10) // 2:+})</span></div>' for ability in ABILITIES)
        other = []
        for key, label in (("save", "Saving Throws"), ("skill", "Skills")):
            if mon.get(key):
                other.append(f"<p><b>{label}</b> " + ", ".join(f"{k.upper() if key == 'save' else k.title()} {v}" for k, v in mon[key].items()) + "</p>")
        for key, label in (("immune", "Damage Immunities"), ("conditionImmune", "Condition Immunities"), ("languages", "Languages")):
            if mon.get(key):
                other.append(f"<p><b>{label}</b> {html.escape(', '.join(mon[key]))}</p>")
        senses = ", ".join(mon.get("senses", []))
        other.append(f"<p><b>Senses</b> {html.escape(senses)}; Passive Perception {mon['passive']}</p>")
        if not mon.get("languages"):
            other.append("<p><b>Languages</b> None</p>")
        sections = []
        for key, label in SECTIONS.items():
            if mon.get(key):
                sections.append(f"<h2>{label}</h2>")
                if key == "legendary":
                    sections.append(entries_html(mon["legendaryHeader"]))
                for entry in mon[key]:
                    sections.append(f"<div class=ability><h3>{readable(entry['name'])}</h3>{entries_html(entry['entries'])}</div>")
        cr = Fraction(mon["cr"])
        pb = 2 if cr < 5 else 2 + (math.ceil(cr) - 1) // 4
        xp = {"1/8": "25", "5": "1,800", "13": "10,000"}.get(mon["cr"])
        challenge = f"CR {mon['cr']}" + (f" (XP {xp}; PB +{pb})" if xp else f" (PB +{pb})")
        cards.append(f'''<article id="{slug}" data-search="{name.lower()} cr {mon['cr']}">
<div class="art"><a href="{art}"><img class="full-art" src="{art}" alt="Full illustration of {name}" loading="lazy"></a>
<div class="token-row"><img src="{token}" alt="Circular portrait token of {name}" loading="lazy"><div><a href="{art}" download>Download full artwork</a><a href="{token}" download>Download token</a></div></div>
<details class="lore" open><summary>Ecology and encounters</summary>{entries_html(fluff['entries'])}</details></div>
<div class="stat"><p class="eyebrow">The Unfinished Dawn · CR {mon['cr']}</p><h1>{name}</h1>
<p class="type">{sizes[mon['size'][0]]} {mon['type'].title()}, {' '.join(alignments[x] for x in mon['alignment'])}</p>
<div class="vitals"><span><b>AC</b> {mon['ac'][0]}</span><span><b>HP</b> {mon['hp']['average']} ({mon['hp']['formula']})</span><span><b>Initiative</b> {initiative:+}</span></div>
<p><b>Speed</b> {', '.join(speeds)}</p><div class="abilities">{ability_html}</div>{''.join(other)}<p><b>Challenge</b> {challenge}</p>{''.join(sections)}</div></article>''')
    (ROOT / "index.html").write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>The Unfinished Dawn Bestiary</title><link rel="stylesheet" href="css/bestiary.css"><script src="js/bestiary.js" defer></script></head>
<body><header><p class="eyebrow">Conclave Homebrew · First collection</p><h1>The Unfinished Dawn</h1><p>The heavens broke. Life found a way to grow around the pieces.</p><p class="draft">Three original creatures for revised fifth edition. Theme proposal and CR targets awaiting playtest.</p><nav>''' + "".join(links) + '''</nav><div class="toolbar"><label for="search">Find a creature</label><input id="search" type="search" placeholder="Name or CR" autocomplete="off"><a href="homebrew/unfinished-dawn.portable.json" download>Download 5etools pack with images</a></div></header><main>''' + "".join(cards) + '''<p id="no-results" hidden>No matching creatures.</p></main><footer>Artwork and matching transparent tokens generated for this collection. <a href="docs/theme.md">Setting proposal</a> · <a href="docs/design-notes.md">Playtest notes</a></footer></body></html>\n''')


def main():
    pack = read("homebrew/source.json")
    pack.update(read("data/bestiary/bestiary-ud.json"))
    pack.update(read("data/bestiary/fluff-bestiary-ud.json"))
    pack.update(read("data/items.json"))
    pack.update(read("data/spells/spells-ud.json"))
    validate(pack)
    write_json("homebrew/unfinished-dawn.json", pack)
    write_json("homebrew/unfinished-dawn.portable.json", embed_images(pack))
    preview(pack)
    print("Built standard and embedded-image homebrew packs and index.html")


if __name__ == "__main__":
    main()
