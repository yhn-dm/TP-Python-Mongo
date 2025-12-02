
# classe Character
# - attributs : name, atk, defn, hp
# - méthode pour attaquer

# classe Monster
# - attributs : name, atk, defn, hp
# - méthode pour attaquer

# classe Team
# - vérifier si tous sont morts

class Character:
    def __init__(self, name, atk, defn, hp):
        self.name = name
        self.atk = atk
        self.defense = defn
        self.hp = hp

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
    def __init__(self, name, atk, defense, hp):
        self.name = name
        self.atk = atk
        self.defn = defense
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0


class Team:
    def __init__(self, characters):
        self.characters = characters

    def all_dead(self):
        for perso in self.characters:
            if perso.is_alive() == True:
                return False
        return True

