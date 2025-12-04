
# - fonction afficher_menu()
# affiche le menu principal

# - fonction main()
# gère la saisie utilisateur (3 options simples)


from utils import input_secure, separateur, afficher_classement, saut
from game import start_game

def afficher_menu():
    saut()
    saut()
    separateur()
    print("MENU PRINCIPAL")
    separateur()
    print("1. Lancer une partie")
    print("2. Afficher le classement")
    print("3. Quitter")
    separateur()

    choix = input_secure("Choisis une option: ", ["1", "2", "3"])
    return choix



def main():
    while True:
        choix = afficher_menu()

        if choix == "1":
            separateur()
            nom = input("Entre un pseudo : ")

            while nom == "":
                print("Nom invalide.")
                nom = input("Entre un pseudo : ")

            start_game(nom)

        if choix == "2":
            afficher_classement()
            separateur()

        if choix == "3":
            break



if __name__ == "__main__":
    main()
