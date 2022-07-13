import random
from .attack import Attack
from .attributes import Sigilo
from .character import Character


class Thief(Character, Sigilo):
    """
    Clase hija de un rol de personaje, hereda de Character y Sigilo todos sus metodos y atributos, el init se modifica
    para tener valores 'default' de este tipo de rol, y se agregan tres metodos nuevos para este tipo de rol.
    """

    def __init__(self, name, race, damage_base=2, hp=50, mana=20, **kwargs):
        super().__init__(name, race, damage_base, hp, mana , **kwargs)

    def slash(self, target):
        recharge = random.randint(0,2)
        print('Slashing')
        if recharge:
            print('You are tired')
            return Attack((self.damage_base /2 ), target)
        print('Power up activate, x4 of damage!!! \U0001F4A5')
        return Attack((self.damage_base * 4 ), target)

    def robar(self):
        if self.sigilo:
            return bool(random.randint(0, 1))
        return False
