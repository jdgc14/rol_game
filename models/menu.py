from .gameplay import Gameplay, characters, guild_dic, arena
from .exceptions import GuildNotFound, InvalidOption, RaceNotFound, RolNotFoud
from .archer import Archer
from .mage import Mage
from .thief import Thief
from .character import Human, Elf, Dwarf


class Menu():
    """
    Para no incluir toda la logica del llamado a los metodos que el usuario puede hacer en nuetro app.py fue creada esta clase,
    su unico proposito es presentar las opciones de gameplay.py al usuario y con respecto a la opcion seleccionada llamar al metodo
    que corresponda de gameplay.py
    """
    @classmethod
    def read_menu(cls):
        print()
        print("""Choose an option
1. Create character
2. Fight the boss
3. See current characters
4. See members guild
0. Exit\n""")
        
        try:
            option = int(input('-> '))
        
            if option == 1:
                character = Gameplay.create_character()

            elif option == 2:
                if len(characters) > 1:
                    Gameplay.fight_boss()
                print('Need more characters to fight, create more')

            elif option == 3:
                if characters:
                    for character in characters: 
                        character.read()
                        print()
                else:
                    print("No characters created")

            elif option == 4:
                while True:
                    try:
                        for code_guild, guild in guild_dic.items():
                            print('{} ({})'.format(code_guild, guild.name))
                            print()
                        input_guild = input('Select guild code: ').upper()
                        print()
                        if input_guild in guild_dic.keys():
                            guild_dic[input_guild].read()
                            break
                        else:
                            raise GuildNotFound()
                    except GuildNotFound:
                        print('Guild not found, try again')

            elif option == 0:
                print('Bye...', '\U0001F44B')
                return False
            
            else:
                raise InvalidOption
            return True
        except (InvalidOption, ValueError):
            print('Invalid option, try again')
            return True

    @classmethod
    def demo_game(cls):
        """
        Este metodo es para simular una partida sin tener que poner todos los inputs para la creacion de personajes, se crean unos
        personajes predefinidos y se ejecuta el metodo de luchar contra el boss, luego limpio la lista de characters con el clear
        para que no hayan personajes repetidos si se vuelve a ejecutar este metodo, o en caso de que se vaya al juego normal la 
        lista de los personajes este vacia en un principio
        """
        characters.append(Archer('Link', Dwarf(), guild='C9'))
        characters.append(Thief('Danny Ocean', Human()))
        characters.append(Mage('Ryze', Elf(), guild='C9'))

        Gameplay.fight_boss()

        characters.clear()
