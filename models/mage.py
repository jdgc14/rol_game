import random

from .attack import Attack
from .character import Character


class Mage(Character):
    """
    Clase hija de un rol de personaje, hereda de Character, el init se modifica para tener valores 'default' de este
    tipo de rol, y se agregan tres metodos nuevos para este tipo de rol.
    """
    healing = True
    intelligence = True

    def __init__(self, name, race, damage_base=3, hp=80, mana=50, **kwargs):
        super().__init__(name, race, damage_base, hp, mana, **kwargs)
        self.experience += 30

    def create(self):
        pass

    def recuperate_mana(self):
        self.experience += 2
        if self.healing:
            recuperated_mana = random.randint(1, 20)
            self.mana += recuperated_mana
            return f'Recuperated {recuperated_mana} mana'
        return "You don't have a healing spell"


    def magic_wall(self):
        self.experience += 2
        if self.intelligence and self.experience > 20:
            return chr(124)
        return "You don't can't do magic wall"
    

    def plasma_burst(self, target):
        if self.experience > 50 and self.mana > 10:
            self.experience += 4
            self.mana -= 10
            damage_dealt = random.randint(self.damage_base, self.damage_base * 2)
            return Attack(damage_dealt, target)

        elif self.experience <= 50:
            self.experience += 5
            return "You don't have enough experience"
            
        elif self.mana <= 10:
            self.experience += 2
            print("You don't have enough mana")
            return self.recuperate_mana()