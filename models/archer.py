from random import randint
from .attack import Attack
from .attributes import Agil
from .character import Character


class Archer(Character, Agil):
    """
    Clase hija de un rol de personaje, hereda de Character y Agil todos sus metodos y atributos, el init se modifica
    para tener valores 'default' de este tipo de rol y se le ingresa un nuevo atributo para la cantidad de flechas, 
    se agregan 3 metodos nuevos que estan relacionados entre si.
    """
    def __init__(self, name, race, damage_base=4, hp=70, mana=10, arrows=10, **kwargs):
        super().__init__(name, race, damage_base, hp, mana, **kwargs)
        self.bow = {'load': True}
        self.arrows = arrows


    def shoot_arrow(self, target):
        if self.bow["load"]:
            self.experience += 2
            print('Shooting arrow')
            self.bow["load"] = False
            damage_dealt = randint(self.damage_base, self.damage_base * 2)
            return Attack(damage_dealt, target)

        elif not self.bow["load"]:
            print("Bow not loaded")
            return self.reload_bow()


    def reload_bow(self):
        if self.bow["load"]:
            return 'Bow already loaded'
        else:
            if self.arrows:
                self.experience += 1
                self.arrows -= 1
                self.bow["load"] = True
                print('Reloading bow')
                return 'Bow reloaded'
            else:
                print("You don't have arrows")
                return self.search_arrows()


    def search_arrows(self):
        print('Searching arrows')
        arrows_found = randint(1, 10)
        self.experience += arrows_found
        self.arrows += arrows_found
        return f'Found {arrows_found} arrows'