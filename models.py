
# classe Character
# - attributs : name, atk, defn, hp
# - méthode pour attaquer

# classe Monster
# - attributs : name, atk, defn, hp
# - méthode pour attaquer

# classe Team
# - vérifier si tous sont morts

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

    #def xp_to_nextlvl(self): xp_to_nextlvl = 50 + (niveau*30)
    def xp_to_nextlvl(self):
        """défini l'xp nécessaire pour monter de lvl"""
        return 50 + (self.level*30)
    
    # def get_xp(self)
    def get_xp(self, amount):
        """récupère l'xp et gère automatiquement le lvlup, amount récupéré de fonc combat"""
        self.xp += amount
        while self.xp >= self.xp_to_nextlvl():
            self.xp -= self.xp_to_nextlvl()
        
            self.level += 1
            self.update_stats()


    #def update_stats(self): scalling joueur : ATK +4% / DEF +3% / HP +10% par niveau
    def update_stats(self):
        """update les stats du joueur  incrémentalement d'après les valeurs basales selon le niveau"""
        self.atk = int(self.base_atk *(1 + 0.04 *(self.level)))
        self.defense = int(self.base_defense *(1 +0.03 *(self.level)))
        self.hp = int(self.base_hp *(1 +0.10 *(self.level)))



    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def take_damage(self, amt):
        self.hp = self.hp - amt
        if self.hp < 0:
            self.hp = 0



class Monster:
    def __init__(self, name, atk, defense, hp, rarity="normal", level=0, xp_base=0): #initialisé à normal
        """initialise les stats -> rareté/level/xp initialisé dans le vide"""
        self.name = name
        self.base_atk = atk
        self.base_defn = defense
        self.base_hp = hp

        self.rarity = rarity
        self.level = level
        self.base_xp = xp_base
        self.update_stats()
        
        

    #def xp_drop(self) xp_base * (1 + niveau_mob *0.1) * (1 + wave*0.05)
    def xp_drop(self,wave):
        """défini l'xp du mob seulement""" # = fonction de récup d'xp nécessaire coté joeuur
        xp = int(self.base_xp * (1 + self.level *0.1) * (1 + wave *0.05))
        return xp
    
    ##def update_stats(self): scalling mob : ATK +6% / DEF +4% / HP +15% par niveau
    def update_stats(self):
        """update les stats du mob d'après les valeurs basales incrémentalement selon le niveau"""
        self.atk = int(self.base_atk * (1 + 0.06 *(self.level)))
        self.defense = int(self.base_defn * (1 + 0.04 *(self.level)))
        self.hp = int(self.base_hp * (1 + 0.15 *(self.level)))



    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0


class Team:
    def __init__(self, characters):
        self.characters = characters
    
    #def team_level(self): = int((p1 + p2 + p3) / 3)
    def team_level(self):
        return int((self.p1 + self.p2 + self.p3) / 3)


    def all_dead(self):
        for perso in self.characters:
            if perso.is_alive() == True:
                return False
        return True
    
    def call_alive_characters(self): # appel des personnages vivants uniquement
        return [c for c in self.characters if c.is_alive()]
    

