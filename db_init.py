
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
    {"name": "Gobelin", "atk": 10, "def": 5, "hp": 50},
    {"name": "Orc", "atk": 20, "def": 8, "hp": 120},
    {"name": "Dragon", "atk": 35, "def": 20, "hp": 300},
    {"name": "Zombie", "atk": 12, "def": 6, "hp": 70},
    {"name": "Troll", "atk": 25, "def": 15, "hp": 200},
    {"name": "Spectre", "atk": 18, "def": 10, "hp": 100},
    {"name": "Golem", "atk": 30, "def": 25, "hp": 250},
    {"name": "Vampire", "atk": 22, "def": 12, "hp": 150},
    {"name": "Loup-garou", "atk": 28, "def": 18, "hp": 180},
    {"name": "Squelette", "atk": 15, "def": 7, "hp": 90},
]



if __name__ == "__main__":
    # supprime ce qu'il se trouve
    characters.delete_many({})
    monsters.delete_many({})

    # insère précisément les 2 dictionnaires
    characters.insert_many(personnages_data)
    monsters.insert_many(monstres_data)
    print("----- Initialisation de la base de données effectué -----")