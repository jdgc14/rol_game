from models.menu import Menu
from models.exceptions import InvalidOption

if __name__== '__main__':
    print('Welcome to the game Final Fantasy\n')

    while True:
        try:
            print('Select...\n1. Demo game\n2. Singleplayer')
            game = int(input(''))
            if game == 1:
                Menu.demo_game()

            elif game == 2:
                option = True
                while option:
                    option = Menu.read_menu()

            else:
                raise InvalidOption()
        except (ValueError, InvalidOption):
            print('Invalid option, try again')




