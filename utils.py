
# connexion bdd

# separateur()
# imprime "------------------------"

# afficher_personnages(liste)
# affiche les persos disponibles pour créer une équipe

# afficher_equipe(equipe)
#  affiche les 3 personnages choisis et leurs stats

# input_secure(message, liste_valide)
# sécurise le choix utilisateur

# input_nombre(message, min_val, max_val)
# vérifie que le monbre est dans la bonne plage

# get_random_monster(mongo)
# retourne un monstre aléatoire depuis la bdd

# afficher_classement(mongo)
# affiche les 3 meilleurs scores tiré de la bdd



# afficher_monstre()
# affiche les stats du monstre tiré de la bdd





from pymongo import MongoClient
import random

RARETE_LVL_MULT = {
    "NORMAL": 1,
    "RARE": 2,
    "EPIC": 4,
    "BOSS": 8,
    "LEGENDAIRE" : 16,
}

client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_db"]

def separateur():
    print("----------------------------------------")

def saut():
    print("\n")





def afficher_personnages(personnages): #depuis le dictionnaire
    """affiche les personnages disponible dans le menu"""
    separateur()
    print("Personnages disponibles :")
    separateur()

    numero = 1

    for p in personnages:
        """format : 1. Nom - ATK: 00 - DEF: 00 - PV: 00"""
        print(str(numero) + ". " + p["name"] + " - ATK: " + str(p["atk"]) + " - DEF: " + str(p["def"]) + " - PV: " + str(p["hp"]))
        numero = numero + 1

    separateur()




def afficher_equipe(equipe):
    """affiche les 3 personnages choisis dans le menu"""
    separateur()
    print("Ton équipe :")
    separateur()

    numero = 1
    for c in equipe.characters:
        """format : 1. Nom - ATK: 00 - DEF: 00 - PV: 00"""
        # DEBUG c = character de l'equipe <- creer l'équipe <- model constructeur (probleme update)
        print(str(numero) + ". " + c.name + " - ATK: " + str(c.atk) + " - DEF: " + str(c.defense) + " - PV: " + str(c.hp))
        numero = numero + 1

    separateur()



def input_secure(message, options_valides): #
    """vérifie que les input sont bien ["1", "2", "3"]"""
    choix = input(message)
    choix = choix.strip()

    while choix not in options_valides:
        print("Choix invalide, réessaie.")
        choix = input(message)
        choix = choix.strip()

    return choix




def input_nombre(message, min_val, max_val):
    """vérifie que le choix rentre dans la plage de 1 à x
    choix = input_nombre(message, 1, len(personnages_db))
    """
    while True:
        user_input = input(message)
    
        if user_input.isdigit():
            valeur = int(user_input)
    
            if valeur >= min_val and valeur <= max_val:
                return valeur

        print("Entrée invalide, réessaie.")



def get_random_monster(wave):
    """draw un monstre random parmis la bdd"""
    rarity = get_rarity_from_wave(wave)
    monsters = list(db["monsters"].find({"rarity": rarity}))

    if not monsters:
        monsters = list(db["monsters"].find())
    return random.choice(monsters)



def save_score(nom_joueur, vague):
    """enregistre le score dans la bdd classement"""
    classement = db["classement"]

    doc = {
        "joueur": nom_joueur,
        "vague": vague
    }
    classement.insert_one(doc)
    print(f"Score sauvegardé : {nom_joueur} - vague {vague}")
    saut()



def afficher_classement():
    """lis la table classement dans la bdd"""
    classement = db["classement"]

    separateur()
    print("Classement des meilleurs joueurs")
    separateur()

    top = classement.find().sort("vague", -1).limit(3)

    rang = 1
    for p in top:
        print(f"{rang}. {p['joueur']} - Vague {p['vague']}")
        rang += 1



def afficher_monstre(monstre):
    print(str(monstre.name) + " - LEVEL: " + str(monstre.level) + " - ATK: " + str(monstre.atk) + " - DEF: " + str(monstre.defense) + " - PV: " + str(monstre.hp))


def get_rarity_from_wave(wave):
    """Génère la rareté du mob random*wave"""
    r = random.random() * 100  # pourcentage sur 100


    if wave <= 30:
        if r < 98: return "NORMAL"
        elif r < 99: return "NORMAL"
        else: return "NORMAL"

    elif wave <= 60:
        if r < 50: return "NORMAL"
        elif r < 85: return "RARE"
        elif r < 97: return "EPIC"
        else: return "BOSS"

    elif wave <= 90:
        if r < 10: return "NORMAL"
        elif r < 60: return "RARE"
        elif r < 90: return "EPIC"
        elif r < 99: return "BOSS"
        else: return "LEGENDAIRE"

    elif wave <= 120:
        if r < 10: return "RARE"
        elif r < 75: return "EPIC"
        elif r < 95: return "BOSS"
        else: return "LEGENDAIRE"

    else:
        if r < 15: return "RARE"
        elif r < 65: return "EPIC"
        elif r < 90: return "BOSS"
        else: return "LEGENDAIRE"