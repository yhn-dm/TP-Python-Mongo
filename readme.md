# Jeu RPG Console - Wave survival

Un jeu RPG en Python où vous devez survivre à un nombre infini de vagues de monstres. Construisez l'équipe, combattez automatiquement et par chance tentez d'atteindre la vague la plus élevée possible !

---

Au lancement, le joueur choisit 3 personnages parmi une liste.
Chaque personnage possède des statistiques uniques (ATK, DEF, PV) et peut simplement monter de niveau au fil de la partie.

À chaque vague :
Un monstre aléatoire est tiré depuis la base MongoDB d'après sa rareté et la vague (Normal → Légendaire), ce qui influence sa puissance.
Son niveau est généré en fonction du niveau moyen de l’équipe et de la vague actuelle.

Le combat est automatique :
Tous les personnages vivants attaquent le monstre.
Si le monstre survit, il attaque un personnage choisi au hasard.
Lorsqu’un monstre meurt, l’équipe gagne de l’XP et peut monter en niveau.
La partie continue jusqu’à ce que l’équipe entière soit vaincue.

---

Tenez le plus longtemps possible et atteignez ainsi la vague la plus élevée.
