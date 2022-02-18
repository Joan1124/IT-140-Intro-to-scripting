# Joan Estepan

# This is a text based game. Read the instructions and win the game!


# function definitions

def instructions():
    print("Welcome to the asylum text game!")
    print("To move around enter: South, North, West, East or Quit to exit game")
    print("To get an item, enter: Get [name of the item]")
    print("Enter instructions to show instructions anytime")
    print("***********************************************")
#display intro text
def intro():
    print('** Intro **')
    print(
        "After a stupid dare, you ended up at a haunted mental asylum that’s being abandoned for years.\nYou remember going and suddenly hear a noise, then everything went dark. \nYou are at an unknown location and you need to find your way out")
    print("**")

# display information current room

def room_info(currentRoom):
    if currentRoom == rooms['reception']:
        print(
            "There’s no electricity in the building, you see the receptionist has an emergency backpack under her desk.")
        print("Maybe you can find something in there to see your way around.")
    elif currentRoom == rooms['main floor']:
        print(
            "Theres a signed baseball bat hung up as decoration on the wall.\nOdd decoration choice for a mental asylum, but it might come in handy...")
    elif currentRoom == rooms['doctors office']:
        print(
            'The doctors desk is full of his personal items. Maybe you can find something that tells you what happened here.(maybe some records?)')
    elif currentRoom == rooms['secret room']:
        print('This room is creepy. Theres something on the floor, looks like a key. You should pick that up.')
    elif currentRoom == rooms['patients room']:
        print("OMG!So many dead bodies! their remains look kinda deformed tho... its like they were barely humans.")
        print("Seems like that guy was writing something...")
    elif currentRoom == rooms['padded room']:
        print("WHAT IS THAT? That crazy man is coming to kill you with a knife! The door locked! YOU MUST FIGHT!")
        if 'bat' in currentInventory:
            print("**One long mini boss fight later...")
            print("Pheww I knew that bat was gonna come in handy. You crushed that guy!\nlooks like he dropped something sharp...")
        else:
            print("He is too strong for you! You should've brought a weap-...")
            print("GAME OVER!\nTry again?")
            quit()
    elif currentRoom == rooms['entrance']:
        print("You are almost out, you can see the exit but then..oh no! its the crazy doctor!")
        print("Looks like he did experiments on himself, yuck. YOU MUST DEFEAT HIM!")
        if 'knife' in currentInventory:
            print("One long boss fight later...\n ***")
            print("Damn kid.. You used that knife gutted that man like your life depended on it. I mean it did.\nMaybe smashing the head with the bat was overkill but it looked cool. ")
            print("Congrats! Head east to leave the asylum for good!")
        else:
            print("One long boss fight later...\n ***")
            print("You're dead dude. come back prepared and try again.")
            quit()
    elif currentRoom == rooms['exit']:
        print("You did it! You Escaped! Congratulations!")
        quit()
#display current status
def show_status(currentRoom):
    print("You currently are at the", currentRoom['room'])  # print room and inventory
    print("Inventory:", currentInventory)
    print("**")

if __name__ == '__main__':

    # Create a dictionary linking the rooms and items in them
    rooms = {
        'basement': {'room': 'basement', 'east': 'reception', 'contents': 'nada'},
        'reception': {'room': 'reception', 'north': 'main floor', 'east': 'entrance', 'west': 'basement',
                      'contents': 'flashlight'},
        'main floor': {'room': 'main floor', 'east': 'doctors office', 'north': 'patients room', 'contents': 'bat', 'south': 'reception'},
        'doctors office': {'room': 'doctors office', 'west': 'main floor', 'north': 'secret room',
                           'contents': 'records'},
        'patients room': {'room': 'patients room', 'south': 'main floor', 'east': 'padded room', 'contents': 'journal'},
        'entrance': {'room': 'entrance', 'west': 'reception', 'east': 'exit', 'contents':'nada'},
        'padded room': {'room': 'padded room', 'west': 'patients room', 'contents': 'knife'},
        'secret room': {'room': 'secret room', 'south': 'doctors office', 'contents': 'key'},
        'exit': {'room': 'exit', 'contents' : "nada"}
    }

    directions = ['north', 'south', 'east', 'west']
    currentRoom = rooms['basement']  # Start player at basement room
    currentInventory = []
    user_move = ''

    # *************Print instructions and Intro **************

    instructions()
    intro()

    while user_move != "quit":

        show_status(currentRoom)
        if currentRoom['contents'] not in currentInventory:
            room_info(currentRoom)

        user_move = input("Enter your move:").strip()  # Get user input and strip whitespaces
        user_move = user_move.lower()  # Lowercases input
        print("*************")

        # *************move between room************

        if user_move in directions:
            if user_move in currentRoom:
                currentRoom = rooms[currentRoom[user_move]]  # sets new room to the users current room
                if currentRoom == rooms['padded room'] and 'key' not in currentInventory:
                    print("Oops you need a key to enter this rooms! Maybe look around the doctors office..")
                    currentRoom = rooms['patients room']
            else:
                print('Cant go in that direction!')  # invalid input validator
                print("Try again.")

        if user_move == 'instructions': #display instuctions
            instructions()

        # *************Pick up item ***************
        elif user_move.split()[0] == 'get':  # gets user item
            item = user_move.split()[1]
            if item in currentRoom['contents']:
                if item not in currentInventory:
                    currentInventory.append(item)  # place item at the end of list
            else:
                print("**** \nI don't see that here.")

        elif user_move not in directions and user_move.split()[0] != 'get':
            print('Invalid input,try again.')