import time
from random import choice
from .exceptions import GuildNotFound, InvalidOption, RaceNotFound, RolNotFoud
from .guild import Guild
from .character import Human, Elf, Dwarf
from .archer import Archer
from .mage import Mage
from .thief import Thief
from .boss import Boss


races = ['Human \U0001F64B', 'Elf \U0001F9DD', 'Dwarf \U0001F9CC']

roles = ['Archer \U0001F3F9', 'Mage \U0001F9D9', 'Thief \U0001F977']

characters = []

rng = Guild('RNG', 'Royal Never Give Up', 'We never give up')
fnc = Guild('FNC', 'Fnatic', 'We create legends')
c9 = Guild('C9', 'Cloud9', 'Reaches for the sky')
navi = Guild('NAVI', 'Natus Vincere', 'Born to win')

guild_dic = {
    'RNG' : rng,
    'FNC' : fnc,
    'C9' : c9,
    'NAVI' : navi,
}

arena = {'boss' : {}, 'players' : []}


class Gameplay():
    """
    Esta clase es creada para limpiar un poco el codigo, los metodos que tiene son de clase y cada uno son las acciones
    que el usuario puede hacer como; crear un personaje, luchar contra el boss.
    Tenemos algunos metodos privados (__select_guild, __select_rol, __select_race) con los que el usario no deberia interactuar
    para no romper el programa, cabe resaltar que estos metodos son llamados automaticamente en la creacion de un personaje por
    lo cual no es necesario que un usuario tenga acceso.
    """
    @classmethod
    def create_character(cls):
        print('-------------------------Creating Character-------------------------\n')
        print('Please, create your character:')
        time.sleep(0.5)
        name = input('Name: ')
        race = cls.__select_race()
        guild = cls.__select_guild()
        character = cls.__select_rol(name, race, guild)
        characters.append(character)
        print()
        print('-------------------------Character created successfully-------------------------')
        character.read()
        if guild:
            guild_dic[guild].members.append(character)
        return character


    @classmethod
    def __select_guild(cls):
        print()
        print('-------------------------Guild-------------------------\n')
        print('You can join a guild: \n1. Select guild\n2. Create guild\n0. Exit')
        try:
            option = int(input('-> '))
            print()
            if option == 1:
                for code_guild, guild in guild_dic.items():
                    print('{} ({})'.format(code_guild, guild.name))
                    time.sleep(0.5)
                print()
                input_guild = input('Select guild code: ').upper()

                if input_guild in guild_dic.keys():
                    return input_guild
                else:
                    raise GuildNotFound()

            elif option == 2:
                print('Create guild')
                code_guild = input('Guild code: ').upper()
                guild_name = input('Name: ')
                guild_slogan = input('Slogan: ')
                guild_dic[code_guild] = Guild.create(id = code_guild, name = guild_name, slogan= guild_slogan)
                return code_guild

            elif option == 0:
                print("You don't want to join a guild")
                return None

            else:
                raise InvalidOption()

        except GuildNotFound:
            print('Guild not found, try again')
            return cls.__select_guild()

        except (ValueError, InvalidOption):
            print('Invalid option, try again')
            return cls.__select_guild()

    @classmethod
    def __select_rol(cls, name, race, guild):
        print()
        print('-------------------------Rol-------------------------\n')
        for rol in roles:
            print(rol)
            time.sleep(0.5)
        print()
        try:
            input_rol = input('Select rol: ').capitalize()

            if input_rol == 'Archer':
                return Archer(name, race, guild=guild)

            elif input_rol == 'Mage':
                return Mage(name, race, guild=guild)

            elif input_rol == 'Thief':
                return Thief(name, race, guild=guild)

            elif input_rol not in roles:
                raise RolNotFoud
        except RolNotFoud:
            print('Rol not found, try again')
            return cls.__select_rol(name, race, guild=guild)


    @classmethod
    def __select_race(cls):
        print('-------------------------Race-------------------------\n')
        
        for race in races:
            print(race)
            time.sleep(0.5)
        print()
        try:
            input_race = input('Select race: ').capitalize()

            if input_race == 'Human':
                return Human()

            elif input_race == 'Elf':
                return Elf()

            elif input_race == 'Dwarf':
                return Dwarf()
            
            elif input_race not in races:
                raise RaceNotFound
        
        except RaceNotFound:
            print('Race not found, try again')
            return cls.__select_race()


    @classmethod
    def fight_boss(cls):
        print('Welcome to the combat arena!!!')
        arena['boss'] = Boss()

        print('The characters that will fight vs {} are:'.format(arena['boss'].name))
        for character in characters: print(character), time.sleep(1), arena['players'].append(character)
        print()
            
        while arena['boss'].hp > 0:
            print()
            target_boss = choice(arena['players'])
            print(arena['boss'].attack(target_boss))
            print()
            if target_boss.hp < 1:
                print('Game finished {} has been slain'.format(target_boss.name))
                print('{} wins'.format(arena['boss'].name))
                print('Better luck next time')
                break

            for character in arena['players']:
                print()
                time.sleep(0.5)
                if arena['boss'].hp < 1:
                    print('Game finished {} has been slain'.format(arena['boss'].name))
                    print('Players wins congratultions')
                    break
                else:
                    print('Turn of ', character)
                    if (isinstance(character, Archer)):
                        print(character.shoot_arrow(arena['boss']))

                    elif (isinstance(character, Mage)):
                        print(character.plasma_burst(arena['boss']))

                    else:
                        print(character.slash(arena['boss']))