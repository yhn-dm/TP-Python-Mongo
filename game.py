import random
from models import Character, Team
from utils import db ,separateur, afficher_personnages, afficher_equipe, input_nombre, saut
from wave import create_monster_for_wave, character_atk_turn, monster_atk_turn, monster_defeated, team_defeated


# ==============================================================
# Initialisation
# ==============================================================

def creer_equipe():
    personnages_db = list(db["characters"].find())
    equipe_personnages = []

    print("")
    print("=== CREE TON EQUIPE ===")
    print("")

    i = 1
    while i <= 3:

        afficher_personnages(personnages_db)
        message = "Choisis ton personnage "
        choix = input_nombre(message, 1, len(personnages_db))
        choix = choix - 1

        perso_db = personnages_db.pop(choix)
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



# ==============================================================
# Game logic
# ==============================================================

def combat(equipe, wave):
    print(f"===== VAGUE {wave} =====")
    monstre = create_monster_for_wave(wave, equipe)
    while monstre.is_alive() and not equipe.all_dead() :
        character_atk_turn(equipe, monstre)
        
        if not monstre.is_alive() :

            print("Victoire")
            monster_defeated(monstre, wave, equipe)
            return True
        
        if monstre.is_alive() :
            monster_atk_turn(monstre, equipe)
            
        if equipe.all_dead() :
            print("Défaite")
            return False

    return False

def start_game(nom_joueur):
    separateur()
    print(nom_joueur + "débute la partie !! Souhaitez-lui bon chance !!")
    separateur()
    equipe = creer_equipe()
    wave = 1

    while True:
            victoire = combat(equipe, wave)    

            if victoire :
                wave += 1
            else :
                team_defeated(wave, nom_joueur)
                break
