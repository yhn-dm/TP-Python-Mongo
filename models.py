# ==============================================================
# ==============================================================
# class Character
# ==============================================================
# ==============================================================

class Character:
    def __init__(self, name, atk, defn, hp, level=0, xp=0):
        """initialise les stats -> rareté/level/xp initialisé dans le vide"""
        self.name = name
        self.base_atk = atk
        self.base_defense = defn
        self.base_hp = hp
        self.level = level
        self.xp = xp
        self.update_stats()

    def get_xp(self, amount):
        """récupère l'xp et gère automatiquement le lvlup, amount récupéré de fonc combat"""
        self.xp += amount
        while self.xp >= self.xp_to_nextlvl():
            self.xp -= self.xp_to_nextlvl()
        
            self.level += 1
            self.update_stats()

    def xp_to_nextlvl(self):
        """défini l'xp nécessaire pour passer au prochain lvl"""
        return 5 + (self.level*2)

    def xp_needed_to_nextlvl(self):
        """défini combien d'xp il manque au character pour lvl up"""
        return self.xp_to_nextlvl() - self.xp

    def update_stats(self):
        """update les stats du joueur  incrémentalement d'après les valeurs basales selon le niveau"""
        self.atk = int(self.base_atk *(1 + 0.16 *(self.level)))
        self.defense = int(self.base_defense *(1 +0.14 *(self.level)))
        self.hp = int(self.base_hp *(1 +0.30 *(self.level)))

    def is_alive(self):
        """vérifie si le character est mort"""
        if self.hp > 0:
            return True
        else:
            return False

    def take_damage(self, amt):
        """calcul les dégats subits en flat"""
        reduction = self.defense // 5 
        damage = amt - reduction
        if damage < 1:
            damage = 0
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0





# ==============================================================
# ==============================================================
# class Monstre
# ==============================================================
# ==============================================================

class Monster:
    def __init__(self, name, atk, defense, hp, rarity="normal", level=0, xp_base=0):
        """initialise les stats -> rareté/level/xp initialisé dans le vide"""
        self.name = name
        self.base_atk = atk
        self.base_defn = defense
        self.base_hp = hp

        self.rarity = rarity
        self.level = level
        self.base_xp = xp_base
        self.update_stats()


    def xp_drop(self,wave):
        """défini l'xp du mob seulement"""
        xp = int(self.base_xp * (1 + self.level *0.1) * (1 + wave *0.05))
        return xp
    
    def update_stats(self):
        """update les stats du mob d'après les valeurs basales incrémentalement selon le niveau""" #à patch
        self.atk = int(self.base_atk * (1 + 0.06 *(self.level)))
        self.defense = int(self.base_defn * (1 + 0.04 *(self.level)))
        self.hp = int(self.base_hp * (1 + 0.15 *(self.level)))

    def is_alive(self):
        """vérifie si le mob est mort"""
        return self.hp > 0

    def take_damage(self, amount):
        """calcul les dégats subits en flat"""
        reduction = self.defense // 5 
        damage = amount - reduction
        if damage < 1:
            damage = 0
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0





# ==============================================================
# ==============================================================
# class Team
# ==============================================================
# ==============================================================

class Team:
    def __init__(self, characters):
        self.characters = characters
    
    def team_level(self):
        """calcul et retourne le niveau de la team"""
        return int(sum (c.level for c in self.characters) / len(self.characters))

    def all_dead(self):
        """vérifie si tous les joueurs sont morts"""
        for perso in self.characters:
            if perso.is_alive() == True:
                return False
        return True
    
    def call_alive_characters(self):
        """appel des personnages vivants uniquement"""
        return [c for c in self.characters if c.is_alive()]
    

