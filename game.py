

# creer l'équipe
# lance le jeu et c'est tout start_game contient le plateau de jeu complet et donc le systeme automatique de combat 
# d'après les règles de models.py donc des 3 classes





from pymongo import MongoClient
import random

from models import Character, Monster, Team
from utils import db, separateur, afficher_personnages, afficher_equipe, input_nombre





def creer_equipe():
    personnages_db = list(db["characters"].find())

    equipe_personnages = []

    print("")
    print("=== CREE TON EQUIPE ===")
    print("")

    i = 1
    while i <= 3:

        afficher_personnages(personnages_db)

        message = "Choisis ton personnage " #vérifie combien il reste de personnages
        choix = input_nombre(message, 1, len(personnages_db))

        choix = choix - 1

        perso_db = personnages_db.pop(choix) #retire le personnage choisi de la liste des personnages dispo

        perso = Character(
            perso_db["name"],
            perso_db["atk"],
            perso_db["def"],
            perso_db["hp"]
        )


        equipe_personnages.append(perso)

        i = i + 1

    equipe = Team(equipe_personnages)
    afficher_equipe(equipe)

    return equipe


def start_game(nom_joueur):
    separateur()
    print("Debut de la partie pour " + nom_joueur)
    separateur()

    equipe = creer_equipe()


    while True:

        break
