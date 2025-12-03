

# creer l'équipe
# lance le jeu et c'est tout start_game contient le plateau de jeu complet et donc le systeme automatique de combat 
# d'après les règles de models.py donc des 3 classes





from pymongo import MongoClient
import random

from models import Character, Monster, Team
from utils import db, separateur, afficher_personnages, afficher_equipe, input_nombre, get_random_monster, save_score, afficher_classement, saut, afficher_monstre

RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

YELLOW = "\033[33m"
RED = "\033[31m"



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

def combat(equipe, vague):
    print(f"===== VAGUE {vague} =====")

    #récum mob
    monstre_data = get_random_monster()
    monstre = Monster(monstre_data["name"], monstre_data["atk"], monstre_data["def"], monstre_data["hp"])
    afficher_monstre(monstre)

    #while monstre isalive and not equip.alldead
        #for char in equip
            #monstre.takedmg(char.atk)
            #print "char" a infligé "dmg" au monstre, il lui rest "monster.hp"
        
        #if not monster.isaline
            #print victoire
            #?? return true = retour et continue la boucle principale
        
        #if monster.isalive
            #cible = random(equip.alive char)
            #cible takedamage (monster.atk)
            #print "monster" a infligé "dmg" au char, il lui rest "char.hp"

        #if equip is alldead
            #print l'équipe a été vaincu
            #?? return false = fin de boucle principale
        
    while monstre.is_alive() and not equipe.all_dead() :
        for perso in equipe.call_alive_characters() :
            monstre.take_damage(perso.atk - monstre.defn)
            print(
                f"{YELLOW}{BOLD}{perso.name}{RESET} a infligé "
                f"{ITALIC}{monstre.atk- monstre.defn}{RESET} au "
                f"{RED}{BOLD}{monstre.name}{RESET}, il lui reste "
                f"{ITALIC}{monstre.hp}{RESET}"
            )
        
        if not monstre.is_alive() :
            print("Victoire")
            saut()
            return True
        
        if monstre.is_alive() :
            cible = random.choice(equipe.call_alive_characters())
            cible.take_damage(monstre.atk-monstre.defn)
            print(
            f"{RED}{BOLD}{monstre.name}{RESET} a infligé "
            f"{ITALIC}{monstre.atk- monstre.defn}{RESET} à "
            f"{YELLOW}{BOLD}{cible.name}{RESET}, il lui reste "
            f"{ITALIC}{cible.hp}{RESET}"
            )
        
        if equipe.all_dead() :
            print("Défaite")
            return False


    return False


def start_game(nom_joueur):
    separateur()
    print("Debut de la partie pour " + nom_joueur)
    separateur()

    equipe = creer_equipe()

    vague = 1

    while True:
            #combat()
            #victoire = vague(vague)

            #if victoire
                #vague += 1

            #else
                #break

            #combat(equipe, vague)
            victoire = combat(equipe, vague)    

            if victoire :
                vague += 1
            else :
                save_score(nom_joueur, vague)
                #print vous avez survécu jusqu'à la vague (vague)
                print (f"Vous avez survécu jusqu'a la vague {vague}")
                afficher_classement()
                break



    

