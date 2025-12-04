
# INITIALISATION DE LA BASE DE DONNÉES
# - Connexion à MongoDB
# - Insertion des entités prédéfinies
# - Ececution supprésion insertion


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
    #normal x1
    {"name": "Gobelin", "atk": 10, "def": 5, "hp": 50, "rarity": "NORMAL", "xp_drop": 5},
    #rare x3
    {"name": "Hobgobelin Warrior", "atk": 30, "def": 15, "hp": 150, "rarity": "RARE", "xp_drop": 15},
    {"name": "Hobgobelin Shaman", "atk": 30, "def": 15, "hp": 150, "rarity": "RARE", "xp_drop": 15},
    #epic x9
    {"name": "4", "atk": 90, "def": 45, "hp": 450, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 90, "def": 45, "hp": 450, "rarity": "EPIC", "xp_drop": 45},
    #boss x27
    {"name": "6", "atk": 270, "def": 135, "hp": 1350, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 270, "def": 135, "hp": 1350, "rarity": "BOSS", "xp_drop": 135},
    #legendaire x81
    {"name": "8", "atk": 810, "def": 405, "hp": 4050, "rarity": "LEGENDAIRE", "xp_drop": 405},



    # normal x1
    {"name": "Orc", "atk": 20, "def": 8, "hp": 120, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 60, "def": 24, "hp": 360, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 60, "def": 24, "hp": 360, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 180, "def": 72, "hp": 1080, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 180, "def": 72, "hp": 1080, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 540, "def": 216, "hp": 3240, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 540, "def": 216, "hp": 3240, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 1620, "def": 648, "hp": 9720, "rarity": "LEGENDAIRE", "xp_drop": 405},



    # normal x1
    {"name": "Dragon", "atk": 35, "def": 20, "hp": 300, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 105, "def": 60, "hp": 900, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 105, "def": 60, "hp": 900, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 315, "def": 180, "hp": 2700, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 315, "def": 180, "hp": 2700, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 945, "def": 540, "hp": 8100, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 945, "def": 540, "hp": 8100, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 2835, "def": 1620, "hp": 24300, "rarity": "LEGENDAIRE", "xp_drop": 405},




    # normal x1
    {"name": "Zombie", "atk": 12, "def": 6, "hp": 70, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 36, "def": 18, "hp": 210, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 36, "def": 18, "hp": 210, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 108, "def": 54, "hp": 630, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 108, "def": 54, "hp": 630, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 324, "def": 162, "hp": 1890, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 324, "def": 162, "hp": 1890, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 972, "def": 486, "hp": 5670, "rarity": "LEGENDAIRE", "xp_drop": 405},




    # normal x1
    {"name": "Troll", "atk": 25, "def": 15, "hp": 200, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 75, "def": 45, "hp": 600, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 75, "def": 45, "hp": 600, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 225, "def": 135, "hp": 1800, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 225, "def": 135, "hp": 1800, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 675, "def": 405, "hp": 5400, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 675, "def": 405, "hp": 5400, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 2025, "def": 1215, "hp": 16200, "rarity": "LEGENDAIRE", "xp_drop": 405},




    # normal x1
    {"name": "Spectre", "atk": 18, "def": 10, "hp": 100, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 54, "def": 30, "hp": 300, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 54, "def": 30, "hp": 300, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 162, "def": 90, "hp": 900, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 162, "def": 90, "hp": 900, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 486, "def": 270, "hp": 2700, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 486, "def": 270, "hp": 2700, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 1458, "def": 810, "hp": 8100, "rarity": "LEGENDAIRE", "xp_drop": 405},




    # normal x1
    {"name": "Golem", "atk": 30, "def": 25, "hp": 250, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 90, "def": 75, "hp": 750, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 90, "def": 75, "hp": 750, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 270, "def": 225, "hp": 2250, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 270, "def": 225, "hp": 2250, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 810, "def": 675, "hp": 6750, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 810, "def": 675, "hp": 6750, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 2430, "def": 2025, "hp": 20250, "rarity": "LEGENDAIRE", "xp_drop": 405},




    # normal x1
    {"name": "Vampire", "atk": 22, "def": 12, "hp": 150, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 66, "def": 36, "hp": 450, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 66, "def": 36, "hp": 450, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 198, "def": 108, "hp": 1350, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 198, "def": 108, "hp": 1350, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 594, "def": 324, "hp": 4050, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 594, "def": 324, "hp": 4050, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 1782, "def": 972, "hp": 12150, "rarity": "LEGENDAIRE", "xp_drop": 405},



    
    # normal x1
    {"name": "Loup-garou", "atk": 28, "def": 18, "hp": 180, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 84, "def": 54, "hp": 540, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 84, "def": 54, "hp": 540, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 252, "def": 162, "hp": 1620, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 252, "def": 162, "hp": 1620, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 756, "def": 486, "hp": 4860, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 756, "def": 486, "hp": 4860, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 2268, "def": 1458, "hp": 14580, "rarity": "LEGENDAIRE", "xp_drop": 405},




    # normal x1
    {"name": "Squelette", "atk": 15, "def": 7, "hp": 90, "rarity": "NORMAL", "xp_drop": 5},
    # rare x3
    {"name": "2", "atk": 45, "def": 21, "hp": 270, "rarity": "RARE", "xp_drop": 15},
    {"name": "3", "atk": 45, "def": 21, "hp": 270, "rarity": "RARE", "xp_drop": 15},
    # epic x9
    {"name": "4", "atk": 135, "def": 63, "hp": 810, "rarity": "EPIC", "xp_drop": 45},
    {"name": "5", "atk": 135, "def": 63, "hp": 810, "rarity": "EPIC", "xp_drop": 45},
    # boss x27
    {"name": "6", "atk": 405, "def": 189, "hp": 2430, "rarity": "BOSS", "xp_drop": 135},
    {"name": "7", "atk": 405, "def": 189, "hp": 2430, "rarity": "BOSS", "xp_drop": 135},
    # legendaire x81
    {"name": "8", "atk": 1215, "def": 567, "hp": 7290, "rarity": "LEGENDAIRE", "xp_drop": 405},

]






if __name__ == "__main__":
    # supprime ce qu'il se trouve
    characters.delete_many({})
    monsters.delete_many({})

    # insère précisément les 2 dictionnaires
    characters.insert_many(personnages_data)
    monsters.insert_many(monstres_data)
    print("----- Initialisation de la base de données effectué -----")