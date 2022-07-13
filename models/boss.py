import random

from .attack import Attack


bosses_name = [
    'La reina Valkyria',
    'Gill',
    'General RAAM',
    'Nemesis',
    'Dark Samus',
]

class Boss():
    #Clase del enemigo que nuestros 'heroes' enfentraran, el nombre sera al azar como referencia a bosses de algunos videojuegos.
    def __init__(self):
        self.name = random.choice(bosses_name) + '\U0001F9B9'
        self.hp = 60
        self.damage_base = 2
    
    def __str__(self):
        return f'{self.name.title()} the {self.__class__.__name__}'

    def attack(self, target):
        damage_dealt = random.randint(self.damage_base, self.damage_base * 2)
        print('{} attacks {}'.format(self.name, target.name))
        return Attack(damage_dealt, target)
