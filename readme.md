# Console RPG — Wave survival

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![MongoDB](https://img.shields.io/badge/MongoDB-Database-green) ![PyMongo](https://img.shields.io/badge/PyMongo-Driver-orange)

A Python RPG where you try to survive as many waves of monsters as possible. Pick a team of 3 characters, fight monsters pulled from MongoDB (rarity and level scale with the wave), and see how high you can get—then try to crack the **top 3** leaderboard.

Started as a school project (TP) for Python + MongoDB: CLI game with everything stored in the DB.

---

## Table of contents

- [How to run](#how-to-run)
- [Project structure](#project-structure)
- [User flow](#user-flow)
- [Game mechanics](#game-mechanics)
- [Formulas](#formulas)
- [MongoDB data](#mongodb-data)

---

## How to run

### Prerequisites

- **Python** 3.8+
- **MongoDB** installed and running (default: `mongodb://localhost:27017`)
- **PyMongo**:

```bash
pip install pymongo
```

### Setup and launch

1. **Seed the database** (characters + monsters). Do this once, or again if you’ve wiped the DB:

   ```bash
   python db_init.py
   ```

2. **Start the game**:

   ```bash
   python main.py
   ```

Main menu: **1** Start a run, **2** View leaderboard (top 3), **3** Quit. Inputs are validated (menu 1–3, non-empty nickname, character pick within range).

---

## Project structure

```
TP-Python-Mongo/
├── main.py       # Entry point, main menu
├── db_init.py    # Seeds MongoDB with 10 characters and all monsters (9 families × rarities)
├── game.py       # Team creation (3 chars out of 10), wave combat loop
├── wave.py       # Monster spawn (rarity by wave, level by team/wave), combat turn, XP, score save
├── models.py     # Character, Monster, Team (stats, damage, levels, XP)
├── utils.py      # DB connection (jeu_db), display helpers, safe input, top 3 leaderboard
├── readme.md     # This file
└── consigne.md   # Original TP instructions (French)
```

DB name: `jeu_db`. Collections: `characters`, `monsters`, `classement`.

---

## User flow

1. **Main menu** — 1: Start game, 2: Leaderboard, 3: Quit.
2. **Start game** — Enter a **nickname** (required).
3. **Build your team** — You see the list of remaining characters (number, name, ATK, DEF, HP). Pick **3** one by one (each character can only be chosen once). Your team is shown at the end.
4. **Wave loop** — Each wave:
   - “WAVE N” + one monster appears (name, level, ATK, DEF, HP).
   - **Your turn:** every living character hits the monster (damage shown).
   - If the monster is still alive, **its turn:** it hits **one** random living character.
   - Monster dies → whole living team gains XP, levels/XP-to-next are shown, next wave.
   - Whole team dead → **game over** → score (last wave) is shown, saved to DB, top 3 is displayed, back to main menu.
5. **Leaderboard** (menu 2) — Top 3 scores (nickname + wave).

---

## Game mechanics

### Characters (your team)

There are **10 characters** in the DB: Guerrier, Mage, Archer, Voleur, Paladin, Sorcier, Chevalier, Moine, Berserker, Chasseur. Each has base ATK, DEF, HP stored in MongoDB; when you pick them they start at level 0 with 0 XP. Stats **scale with level** (see [Formulas](#formulas)). XP is earned on each kill; when a character reaches the next level threshold they level up and stats are updated. Every **living** character gets the same XP per monster.

### Monsters

Monsters belong to **families** (e.g. Goblin/Hobgoblin, Orc, Dragon, Zombie, Troll, Spectre, Golem, Vampire, Werewolf, Skeleton) with **rarity variants**: NORMAL, RARE, EPIC, BOSS, LEGENDARY. Each DB entry has base name, ATK, DEF, HP, rarity, and base **XP drop**. For a given wave we (1) roll a **rarity** from the wave-based table, (2) pick a random monster of that rarity from `monsters`, (3) compute its **level** from team level, wave number, and a rarity multiplier, (4) scale its ATK/DEF/HP with that level.

### Combat

**Order:** all living characters attack first; then, if the monster is still up, it attacks **one** random living character. **Damage:** raw = attacker ATK − target DEF; the target then gets a **flat reduction** (DEF ÷ 5); final damage is non-negative (see [Damage](#damage)). A character at 0 HP doesn’t attack or earn XP. Game ends when **everyone** is at 0 HP.

### Score and leaderboard

Your **score** is the **last wave number** you reached before wiping. On game over it’s written to the `classement` collection (`joueur`, `vague`). The **top 3** is just the three highest `vague` values, descending.

---

## Formulas

### Character (level and stats)

- **XP to next level:** `5 + (level × 2)`.
- **Stats at level N** (integer):
  - ATK = `base_atk × (1 + 0.16 × N)`
  - DEF = `base_def × (1 + 0.14 × N)`
  - HP  = `base_hp × (1 + 0.30 × N)`

### Monster (level and stats)

- **Monster level** (integer ≥ 1):  
  `level = max(1, team_level × wave × rarity_mult × random(0.01, 0.03))`  
  Rarity mult: NORMAL 1, RARE 1.3, EPIC 2, BOSS 2.5, LEGENDARY 3.
- **Monster stats at level N:**
  - ATK = `base_atk × (1 + 0.06 × N)`
  - DEF = `base_def × (1 + 0.04 × N)`
  - HP  = `base_hp × (1 + 0.15 × N)`
- **XP drop** (per living character):  
  `base_xp × (1 + monster_level × 0.1) × (1 + wave × 0.05)` (integer).

### Rarity by wave

| Wave       | NORMAL | RARE | EPIC | BOSS | LEGENDARY |
|------------|--------|------|------|------|-----------|
| 1–100      | 100%   | —    | —    | —    | —         |
| 101–250    | 80%    | 10%  | 7%   | 3%   | —         |
| 251–500    | 60%    | 25%  | 5%   | 4%   | 1%        |
| 501–1000   | —      | 10%  | 65%  | 20%  | 5%        |
| 1001+      | —      | 15%  | 50%  | 25%  | 10%       |

One random roll picks the rarity; then we pick a random monster of that rarity from the DB.

### Damage

- **Raw damage:** `attacker_ATK - target_DEF` (can be negative).
- **Reduction:** `target_DEF // 5` (integer division).
- **Final damage:** `max(0, raw - reduction)`.
- Target’s HP goes down by that amount (floor 0).

---

## MongoDB data

### `characters`

**10 documents** from `db_init.py`. Fields: `name`, `atk`, `def`, `hp` (base values). Examples: Guerrier (35 ATK, 10 DEF, 100 HP), Mage (40, 5, 80), Paladin (54, 12, 110), Sorcier (55, 3, 70), etc.

### `monsters`

Lots of documents (per family × rarity), also from `db_init.py`. Fields: `name`, `atk`, `def`, `hp`, `rarity`, `xp_drop`. Families: Hobgoblin, Orc, Dragon, Zombie, Troll, Spectre, Golem, Vampire, Werewolf, Skeleton—each with NORMAL through LEGENDARY variants.

### `classement`

Created on first score save. Fields: `joueur` (string), `vague` (number). Top 3 is `find().sort("vague", -1).limit(3)`.

---

**Goal:** survive as long as you can and climb the leaderboard. Difficulty ramps with wave (rarity + monster level); your team’s levels and XP help you keep up.
