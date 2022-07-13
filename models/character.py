class Character:
    """
    Clase padre para la creacion de los roles de personajes, tenemos modificamos su init para que adquiera ciertos 
    'modificadores' con respecto a su raza, raza que es una clase ingresada por composicion.
    """
    def __init__(self, name, race, damage_base=2, hp=100, mana=10 , **kwargs):
        self.name = name
        self.mana = mana
        self.race = race
        self.hp = hp
        self.experience = 0
        self.damage_base = damage_base

        #Estos son los 'modificadores' puestos en el init para validar apenas es creada una instancia nueva.
        if isinstance(self.race, Elf):
            self.mana = mana * 2

        if isinstance(self.race, Human):
            self.hp += 20
        
        if isinstance(self.race, Dwarf):
            self.experience += 20
            self.damage_base += damage_base

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name.title()} the {self.__class__.__name__}'

    def __repr__(self):
        return f'{self.name.title()} the {self.__class__.__name__}'

    def read(self):
        #Metodo para leer la informacion de los personajes.
        print('Class: -----{}-----'.format(self.__class__.__name__).upper())
        print('Name:', self.name)
        print('Race:', self.race)
        if self.guild:
            print('Guild:', self.guild)
        print('Health points:', self.hp)
        print('Mana:', self.mana)
        print('Experiencie:', self.experience)
        print('Damage base:', self.damage_base)

#Aca tenemos las clases de las razas que los personajes pueden tener por composicion
class Human():
    def __str__(self):
        return 'Human \U0001F64B'


class Elf():
    def __str__(self):
        return 'Elfo \U0001F9DD'
    

class Dwarf():
    def __str__(self):
        return 'Dwarf \U0001F9CC'
