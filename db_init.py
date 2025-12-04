from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_db"]
characters = db["characters"]
monsters = db["monsters"]


personnages_data = [
    {"name": "Guerrier", "atk": 35, "def": 10, "hp": 100},
    {"name": "Mage", "atk": 40, "def": 5, "hp": 80},
    {"name": "Archer", "atk": 28, "def": 7, "hp": 90},
    {"name": "Voleur", "atk": 33, "def": 8, "hp": 85},
    {"name": "Paladin", "atk": 54, "def": 12, "hp": 110},
    {"name": "Sorcier", "atk": 55, "def": 3, "hp": 70},
    {"name": "Chevalier", "atk": 37, "def": 15, "hp": 120},
    {"name": "Moine", "atk": 19, "def": 9, "hp": 95},
    {"name": "Berserker", "atk": 53, "def": 6, "hp": 105},
    {"name": "Chasseur", "atk": 46, "def": 11, "hp": 100},
]


monstres_data = [
    {"name": "Gobelin", "atk": 10, "def": 5, "hp": 50, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Hobgobelin Warrior", "atk": 30, "def": 15, "hp": 150, "rarity": "RARE", "xp_drop": 150},
    {"name": "Hobgobelin Shaman", "atk": 30, "def": 15, "hp": 150, "rarity": "RARE", "xp_drop": 150},
    {"name": "Hobgobelin Champion", "atk": 90, "def": 45, "hp": 450, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Hobgobelin Assaillant", "atk": 90, "def": 45, "hp": 450, "rarity": "EPIC", "xp_drop":450},
    {"name": "Roi Hobgobelin", "atk": 270, "def": 135, "hp": 1350, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Hobgobelin Seigneur de Guerre", "atk": 270, "def": 135, "hp": 1350, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Hobgobelin Ancetre", "atk": 810, "def": 405, "hp": 4050, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Orc", "atk": 20, "def": 8, "hp": 120, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Orc Sauvage", "atk": 60, "def": 24, "hp": 360, "rarity": "RARE", "xp_drop": 150},
    {"name": "Orc Enrage", "atk": 60, "def": 24, "hp": 360, "rarity": "RARE", "xp_drop": 150},
    {"name": "Orc Champion", "atk": 180, "def": 72, "hp": 1080, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Orc Massacreur", "atk": 180, "def": 72, "hp": 1080, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Roi Orc", "atk": 540, "def": 216, "hp": 3240, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Seigneur de Guerre Orc", "atk": 540, "def": 216, "hp": 3240, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Orc Légendaire", "atk": 1620, "def": 648, "hp": 9720, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Dragonnet", "atk": 35, "def": 20, "hp": 300, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Wyverns Sauvage", "atk": 105, "def": 60, "hp": 900, "rarity": "RARE", "xp_drop": 150},
    {"name": "Salamandre sauvage", "atk": 105, "def": 60, "hp": 900, "rarity": "RARE", "xp_drop": 150},
    {"name": "Dragon Nagas", "atk": 315, "def": 180, "hp": 2700, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Dragon élémentaire", "atk": 315, "def": 180, "hp": 2700, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Archidragon", "atk": 945, "def": 540, "hp": 8100, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Dragon Fléau", "atk": 945, "def": 540, "hp": 8100, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Dragon Primordial", "atk": 2835, "def": 1620, "hp": 24300, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Zombie", "atk": 12, "def": 6, "hp": 70, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Zombie Rodeur", "atk": 36, "def": 18, "hp": 210, "rarity": "RARE", "xp_drop": 150},
    {"name": "Zombie Burner", "atk": 36, "def": 18, "hp": 210, "rarity": "RARE", "xp_drop": 150},
    {"name": "Zombie Armuré", "atk": 108, "def": 54, "hp": 630, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Zombie Mega-Walkers", "atk": 108, "def": 54, "hp": 630, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Zombie Variant", "atk": 324, "def": 162, "hp": 1890, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Zombie Titanesque", "atk": 324, "def": 162, "hp": 1890, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Titan Variant", "atk": 972, "def": 486, "hp": 5670, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Troll", "atk": 25, "def": 15, "hp": 200, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Troll des cavernes", "atk": 75, "def": 45, "hp": 600, "rarity": "RARE", "xp_drop": 150},
    {"name": "Troll Guerrier", "atk": 75, "def": 45, "hp": 600, "rarity": "RARE", "xp_drop": 150},
    {"name": "Troll Colossale", "atk": 225, "def": 135, "hp": 1800, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Troll Destructeur", "atk": 225, "def": 135, "hp": 1800, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Roi Troll", "atk": 675, "def": 405, "hp": 5400, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Seigneur Troll", "atk": 675, "def": 405, "hp": 5400, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Troll Ancien", "atk": 2025, "def": 1215, "hp": 16200, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Spectre", "atk": 18, "def": 10, "hp": 100, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Spectre Veillé", "atk": 54, "def": 30, "hp": 300, "rarity": "RARE", "xp_drop": 150},
    {"name": "Esprit Tourmenté", "atk": 54, "def": 30, "hp": 300, "rarity": "RARE", "xp_drop": 150},
    {"name": "Spectre Nocturne", "atk": 162, "def": 90, "hp": 900, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Spectre Maudit", "atk": 162, "def": 90, "hp": 900, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Archispectre", "atk": 486, "def": 270, "hp": 2700, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Seigneur des Ombres", "atk": 486, "def": 270, "hp": 2700, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Spectre Néantique", "atk": 1458, "def": 810, "hp": 8100, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Golem", "atk": 30, "def": 25, "hp": 250, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Golem de Pierre", "atk": 90, "def": 75, "hp": 750, "rarity": "RARE", "xp_drop": 150},
    {"name": "Golem Titan", "atk": 90, "def": 75, "hp": 750, "rarity": "RARE", "xp_drop": 150},
    {"name": "Golem Runique", "atk": 270, "def": 225, "hp": 2250, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Golem Royal", "atk": 270, "def": 225, "hp": 2250, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Golem Colossal", "atk": 810, "def": 675, "hp": 6750, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Golem Ancien", "atk": 810, "def": 675, "hp": 6750, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Golem Divin", "atk": 2430, "def": 2025, "hp": 20250, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Vampire", "atk": 22, "def": 12, "hp": 150, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Vampire Sanguinaire", "atk": 66, "def": 36, "hp": 450, "rarity": "RARE", "xp_drop": 150},
    {"name": "Vampire Déchu", "atk": 66, "def": 36, "hp": 450, "rarity": "RARE", "xp_drop": 150},
    {"name": "Vampire Noble", "atk": 198, "def": 108, "hp": 1350, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Seigneur Vampire", "atk": 198, "def": 108, "hp": 1350, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Archi-Vampire", "atk": 594, "def": 324, "hp": 4050, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Vampire Roi-Sang", "atk": 594, "def": 324, "hp": 4050, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Vampire Primordial", "atk": 1782, "def": 972, "hp": 12150, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Loup-garou", "atk": 28, "def": 18, "hp": 180, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Loup-garou Traqueur", "atk": 84, "def": 54, "hp": 540, "rarity": "RARE", "xp_drop": 150},
    {"name": "Loup-garou Sanguinaire", "atk": 84, "def": 54, "hp": 540, "rarity": "RARE", "xp_drop": 150},
    {"name": "Loup-garou Alpha", "atk": 252, "def": 162, "hp": 1620, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Loup-garou Ravageur", "atk": 252, "def": 162, "hp": 1620, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Seigneur Lupin", "atk": 756, "def": 486, "hp": 4860, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Titan-Garou", "atk": 756, "def": 486, "hp": 4860, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Ancêtre Lycan", "atk": 2268, "def": 1458, "hp": 14580, "rarity": "LEGENDAIRE", "xp_drop": 5000},

    {"name": "Squelette", "atk": 15, "def": 7, "hp": 90, "rarity": "NORMAL", "xp_drop": 30},
    {"name": "Squelette Armé", "atk": 45, "def": 21, "hp": 270, "rarity": "RARE", "xp_drop": 150},
    {"name": "Squelette Agile", "atk": 45, "def": 21, "hp": 270, "rarity": "RARE", "xp_drop": 150},
    {"name": "Squelette Champion", "atk": 135, "def": 63, "hp": 810, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Squelette Royal", "atk": 135, "def": 63, "hp": 810, "rarity": "EPIC", "xp_drop": 450},
    {"name": "Roi Squelette", "atk": 405, "def": 189, "hp": 2430, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Démon Squelette", "atk": 405, "def": 189, "hp": 2430, "rarity": "BOSS", "xp_drop": 1350},
    {"name": "Squelette Transcendant", "atk": 1215, "def": 567, "hp": 7290, "rarity": "LEGENDAIRE", "xp_drop": 5000},
]


if __name__ == "__main__":
    characters.delete_many({})
    monsters.delete_many({})

    characters.insert_many(personnages_data)
    monsters.insert_many(monstres_data)
    print("----- Initialisation de la base de données effectué -----")