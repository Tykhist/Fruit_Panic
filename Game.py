# This will display instructions and story for the game, like a title screen
def title_screen():
    print('FRUIT PANIC!!!')
    print('You accidentally scattered fruit throughout your house while hungrily sleepwalking.')
    print('Eat fruit before bed to win! It will spoil if left out overnight...')
    print('Going into your bedroom will make you sleepy. Don\'t sleep until all 7 fruits are eaten!')
    print('Commands: go North, go South, go East, go West, eat fruit')

# A few of the mechanics will have to be initialized as global variables
move = ''
valid_moves = []
room = 'Broom Closet'
fruit = 'nothing at all'
stomach = []              # Inventory
on_floor = False          # Checks for fruit on the floor

# This function will give the player a status of where they are and what they have done after every move
def status():

    global valid_moves
    global room
    global fruit
    global stomach
    global on_floor

    print('')
    print('~' * 16)
    print(f'You are in the {room}. You can {valid_moves}.')
    if stomach == []:
        print('Your stomach is empty, and you are starving.')
    else:
        print(f'Your stomach is full of {stomach}!')
    if on_floor:
        print(f'You see {fruit} in front of you.')
    print('~'*16)
    print('')
    print('Enter command: ')

# This is the main function of the game that makes it playable
def main():

    """Dictionary that links all rooms together and links items to
    all rooms except the Start room  and the room containing the villain"""
    all_rooms = {
        'Broom Closet': {'East': 'Hallway'},   # Start
        'Hallway': {'South': 'Living Room', 'East': 'Entrance', 'West': 'Broom Closet', 'item': 'Kiwi'},
        'Entrance': {'West': 'Hallway', 'item': 'Passion Fruit'},
        'Living Room': {'South': 'Bedroom', 'North': 'Hallway', 'East': 'Office', 'West': 'Kitchen', 'item': 'Mango'},
        'Kitchen': {'South': 'Dining Room', 'East': 'Living Room', 'item': 'Lychee'},
        'Office': {'South': 'Bathroom', 'West': 'Living Room', 'item': 'Pomegranate'},
        'Dining Room': {'North': 'Kitchen', 'East': 'Bedroom', 'item': 'Dragon Fruit'},
        'Bathroom': {'North': 'Office', 'West': 'Bedroom', 'item': 'Citron'},
        'Bedroom': {'North': 'Living Room', 'East': 'Bathroom', 'West': 'Dining Room', 'item': 'Bed'}  # Villain
    }

    north_room = ''
    east_room = ''
    south_room = ''
    west_room = ''
    in_bedroom = False  # Check made to end game when player is in final area
    global move
    global valid_moves
    global room
    global fruit
    global stomach
    global on_floor

    while in_bedroom == False:

        if room == 'Broom Closet':
            valid_moves = ['go East']
            north_room = ''
            east_room = 'Hallway'
            south_room = ''
            west_room = ''

            on_floor = False

        elif room == 'Hallway':
            north_room = ''
            east_room = 'Entrance'
            south_room = 'Living Room'
            west_room = 'Broom Closet'

            fruit = 'Kiwi'
            if fruit in stomach:
                on_floor = False
                valid_moves = ['go South', 'go East', 'go West']
            else:
                on_floor = True
                valid_moves = ['go South', 'go East', 'go West', f'eat {fruit}']

        elif room == 'Entrance':
            north_room = ''
            east_room = ''
            south_room = ''
            west_room = 'Hallway'

            fruit = 'Passion Fruit'
            if fruit in stomach:
                on_floor = False
                valid_moves = ['go West']
            else:
                on_floor = True
                valid_moves = ['go West', f'eat {fruit}']

        elif room == 'Living Room':
            north_room = 'Hallway'
            east_room = 'Office'
            south_room = 'Bedroom'
            west_room = 'Kitchen'

            fruit = 'Mango'
            if fruit in stomach:
                on_floor = False
                valid_moves = ['go South', 'go North', 'go East', 'go West']
            else:
                on_floor = True
                valid_moves = ['go South', 'go North', 'go East', 'go West', 'eat Mango']

        elif room == 'Kitchen':
            north_room = ''
            east_room = 'Living Room'
            south_room = 'Dining Room'
            west_room = ''

            fruit = 'Lychee'
            if fruit in stomach:
                on_floor = False
                valid_moves = ['go South', 'go East']
            else:
                on_floor = True
                valid_moves = ['go South', 'go East', f'eat {fruit}']

        elif room == 'Office':
            north_room = ''
            east_room = ''
            south_room = 'Bathroom'
            west_room = 'Living Room'

            fruit = 'Pomegranate'
            if fruit in stomach:
                on_floor = False
                valid_moves = ['go South', 'go West']
            else:
                on_floor = True
                valid_moves = ['go South', 'go West', f'eat {fruit}']

        elif room == 'Dining Room':
            north_room = 'Kitchen'
            east_room = 'Bedroom'
            south_room = ''
            west_room = ''

            fruit = 'Dragon Fruit'
            if fruit in stomach:
                on_floor = False
                valid_moves = ['go North', 'go East']
            else:
                on_floor = True
                valid_moves = ['go North', 'go East', f'eat {fruit}']

        elif room == 'Bathroom':
            north_room = 'Office'
            east_room = ''
            south_room = ''
            west_room = 'Bedroom'

            fruit = 'Citron'
            if fruit in stomach:
                on_floor = False
                valid_moves = ['go North', 'go West']
            else:
                on_floor = True
                valid_moves = ['go North', 'go West', f'eat {fruit}']

        elif room == 'Bedroom':
            valid_moves = ['sleep']
            if len(stomach) >= 8:
                print('\nYou cannot resist the temptation to sleep.')
                print('Congratulations! Now you can sleep\n with a clean house and a full stomach!')
                in_bedroom = True
                break
            else:
                print('\nYou cannot resist the temptation to sleep.')
                print('Sorry! You went to sleep still hungry. \nAll of the remaining fruit spoiled, making your house stink')
                in_bedroom = True
                break

        status()
        move = input()
        if True:
            if move not in valid_moves:
                print(f'\nCan\'t {move}! :[')

            elif move in valid_moves:
                if move == 'go North':
                    room = north_room
                    continue

                elif move == 'go South':
                    room = south_room
                    continue

                elif move == 'go East':
                    room = east_room
                    continue

                elif move == 'go West':
                    room = west_room
                    continue

                elif 'eat' in move:
                    stomach.append(fruit)
                    continue





title_screen()
main()
print('\nThank you for playing Fruit Panic! I hope that you enjoyed it!')
