MVP
- logique attaque/défense/hp
-> defense fixe ou % ?
-> atk to def = ??? 
(50 - 18) + (48 - 18) + (47 - 18) = 91dmg sur une moyenne de 170pv
logique trop plate

[boucle while](
- tirage de monstre parmis la bdd
- équipe attaque le mob
- mob attaque un membre de l'équipe
- membre mort = perd son tour
- équipe mort = fin du jeu
- affichage du score
- envoie du score en bdd (classement)
- affichage du menu
)

- ajout selection menu "classement" = affichage bdd (classement) (trie des 3 meilleurs)




V1
- ajout de format (color, font, gras/italique)
- ajout de temporisation 1.5s-2s "..."

- ajout de stat rareté [normal, rare, épique, boss, légendaire] avec multiplication directe de stats x1->x3->x9>-x27->x81
- ajout de stat mob xp drop
- ajout d'un systeme de niveau des entités (joueur = gain d'xp selon mob*niveau) (mob = lvl d'apparition selon (lvl d'équipe*wave) * randomisation (1-100%))
- système de stats selon niveau (atk 15%, def 10%, hp 25%)
-> comment établir stats ? (joueur = (BASE*(x1.15atk, x1.1def, x1.25 cumulation composé/lvl))) (mob = (BASE*(x1.15atk, x1.1def, x1.25 cumulation fixe/lvl)))
- randomisation taux d'apparition rareté selon (niveau de l'équipe * vague)
- drop d'xp selon ((base * niveau de l'équipe) + randomisation (2-30%))



FORMULE TROP PROGRESSIVE
Correction :
niveau_team = (p1 + p2 + p3) / 3
niveau_mob = niveau_team * wave * rarete * random(0.02, 2.0)
xp drop = xp_base * (1 + niveau_mob * 0.1) * (1 + wave * 0.05)
xp_to_nextlvl = 50 + (niveau * 30)

scalling joueur : ATK +4% / DEF +3% / HP +10% par niveau
scalling mob : ATK +6% / DEF +4% / HP +15% par niveau

vague 1-20 : Normal 80% Rare 15% Epic 5% oss 0% Legend 0%
vagie 21-40 : Normal 50% Rare 35% Epic 12% oss 3% Legend 0%
vague 41-60 : Normal 10% Rare 50% Epic 30% oss 9% Legend 1%
vague 61-80 : Normal 0% Rare 10% Epic 65% oss 20% Legend 5%
vague 81-100 : Normal 0% Rare 15% Epic 50% oss 25% Legend 10%

-> comment faire tirage randomisé dans la bdd d'après rareté/vague puisque la classe de rareté se trouve dans la bdd
Tirer au sort directement la classe puis selectionner dans la bdd d'après rareté


