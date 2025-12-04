import random
from pymongo import MongoClient
from models import  Monster
from utils import db, saut, afficher_monstre_stats, save_score, afficher_classement

# ==============================================================
# Formatage font
# ==============================================================

RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
YELLOW = "\033[33m"
RED = "\033[31m"

# ==============================================================
# Monster/wave logic
# ==============================================================

RARETE_LVL_MULT = {
    "NORMAL": 1,
    "RARE": 1.3,
    "EPIC": 2,
    "BOSS": 2.5,
    "LEGENDAIRE" : 3,
}

def get_random_monster(wave):
    """draw un monstre random parmis la bdd"""
    rarity = get_monster_rarity_from_wave(wave)
    monsters = list(db["monsters"].find({"rarity": rarity}))

    if not monsters:
        monsters = list(db["monsters"].find())
    return random.choice(monsters)

def get_monster_rarity_from_wave(wave):
    """Génère la rareté du mob random*wave"""
    r = random.random() * 100  # pourcentage sur 100


    if wave <= 100:
        if r < 80: return "NORMAL"
        elif r < 95: return "NORMAL"
        else: return "NORMAL"

    elif wave <= 250:
        if r < 80: return "NORMAL"
        elif r < 90: return "RARE"
        elif r < 97: return "EPIC"
        else: return "BOSS"

    elif wave <= 500:
        if r < 60: return "NORMAL"
        elif r < 85: return "RARE"
        elif r < 90: return "EPIC"
        elif r < 99: return "BOSS"
        else: return "LEGENDAIRE"

    elif wave <= 1000:
        if r < 10: return "RARE"
        elif r < 75: return "EPIC"
        elif r < 95: return "BOSS"
        else: return "LEGENDAIRE"

    else:
        if r < 15: return "RARE"
        elif r < 65: return "EPIC"
        elif r < 90: return "BOSS"
        else: return "LEGENDAIRE"

def generate_monster_level(monstre, equipe, wave):
    rarity = get_monster_rarity_from_wave(wave)
    monstre.rarity = rarity

    mult = RARETE_LVL_MULT[rarity]
    team_lvl = equipe.team_level()
    monstre.level = max(1, int(team_lvl * wave * mult * random.uniform(0.01, 0.03)))
    monstre.update_stats()
    return monstre

def create_monster_for_wave(wave, equipe):
    monstre_db = get_random_monster(wave)
    monstre = Monster(monstre_db["name"], 
                    monstre_db["atk"], 
                    monstre_db["def"], 
                    monstre_db["hp"],
                    monstre_db["rarity"],
                    level=0,
                    xp_base=monstre_db["xp_drop"])
    generate_monster_level(monstre, equipe, wave)
    afficher_monstre_stats(monstre)
    return monstre

def character_atk_turn(equipe, monstre):
    for perso in equipe.call_alive_characters() :
        monstre.take_damage(perso.atk - monstre.defense)
        print(
            f"{YELLOW}{BOLD}{perso.name}{RESET} a infligé "
            f"{ITALIC}{perso.atk - monstre.defense}{RESET} au "
            f"{RED}{BOLD}{monstre.name}{RESET}, il lui reste "
            f"{ITALIC}{monstre.hp}{RESET}"
        )

def monster_atk_turn(monstre, equipe):
        cible = random.choice(equipe.call_alive_characters())
        cible.take_damage(monstre.atk - cible.defense)
        print(
        f"{RED}{BOLD}{monstre.name}{RESET} a infligé "
        f"{ITALIC}{monstre.atk - cible.defense}{RESET} à "
        f"{YELLOW}{BOLD}{cible.name}{RESET}, il lui reste "
        f"{ITALIC}{cible.hp}{RESET}"
        )

def monster_defeated(monstre, wave, equipe):
    xp_gain = monstre.xp_drop(wave)#send également la vague
    for perso in equipe.call_alive_characters():
        perso.get_xp(xp_gain)
    print(f"Le monstre drop {xp_gain} d'XP ! L'équipe reçoit ainsi {xp_gain} XP !")

    for perso in equipe.call_alive_characters():
        print(f"{perso.name} - lvl {perso.level} nécessite pour le prochain niveau {perso.xp_needed_to_nextlvl()} XP")
    saut()

def team_defeated(wave, nom_joueur):
    print (f"Vous avez survécu jusqu'a la vague {wave}")
    save_score(nom_joueur, wave)
    afficher_classement()
