#!/usr/bin/env python3
"""Anime suggestions | Julian Rosa
:'("""

from sre_constants import JUMP
from unittest.mock import mock_open

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game 
    ========
    Commands:
        go [direction]
        get [item]
    ''')
    print('Remember you MUST type go before a direction to move and you MUST type get before putting an item into inventory')

# start counter at 0 because no moves have been made yet
move_count = 0

# get user name
name_input = input("What is you name?: ")\

#welcome user
print(f'{name_input}, Welcome to Spongebob\'s Pineapple Manchine')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print(f'{name_input}, you are in the {currentRoom}')
    print(f'{name_input}, You can go in these directions: ' + rooms[currentRoom]['description'] + '!' )
    # print what the player is carrying
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print(f"You have made {move_count} moves!")
    print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'north' : 'Theatre', 
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west' : 'Bathroom',
                  'description' : 'north, south, east or west'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Pantry',
                  'description' : 'north or south'
                },
            'Bathroom' : {
                'north': 'Gameroom',
                'south': 'Bedroom',
                'east' : 'Hall',
                'description' : 'north, south or east. Be careful where you go. Pete is lurking!!'
                },
            'Bedroom' : {
                'north' : 'Bathroom',
                'item' : 'Pete The Fish, NO MORE!',
                'description' : 'north'
            },
            'Gameroom' : {
                'south' : 'Bathroom',
                'east' : 'Theatre',
                'item' : 'spatula',
                'description' : 'south or east'
            },
            'Theatre' : {
                'south' : 'Hall',
                'west' : 'Gameroom',
                'east' : 'Gym',
                'description' : 'south or west'
            },
            'Gym' : {
                'north' : 'Artillery',
                'west' : 'Theatre',
                'description' : 'north or west'
            },
            'Artillery' : {
                'south' : 'Gym',
                'item' : 'weapon',
                'description' : 'south'
            },
            'Pantry' : {
                'north' : 'Kitchen',
                'item' : 'formula',
                'description' : 'north'
            },
             'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garage',
                  'east' : 'Study',
                  'description' : 'south, east or west'
             },
             'Study' : {
                'south' : 'Living Room',
                'east' : 'Dining Room',
                'item' : 'spongebob',
                'description' : 'south or east. Be careful where you go. Pete is lurking!!'
             },
             'Living Room' : {
                'north' : 'Study',
                'west' : 'Garage',
                'item' : 'Pete The Fish',
                'description' : 'nowhere, Pete Ate You!'
             },
             'Garage' : {
                'north' : 'Dining Room',
                'south' : 'Basement',
                'east' : 'Living Room',
                'description' : 'north, south or east'
             },
             'Basement' : {
                'north' : 'Garage',
                'east' : 'Secret Kitchen',
                'description' : 'north or east'
             },
             'Secret Kitchen' : {
                'west' : 'Basement',
                'description' : 'west'
             }

         }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # directional move was made and count goes up
            move_count += 1
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    # If a player enters a room with a monster and has a weapon Pete defeated and continue
    if 'item' in rooms[currentRoom] and 'Pete The Fish' in rooms[currentRoom]['item'] and 'weapon' in inventory:
        print('You defeated one of the Pete the Fish with your weapon, that was close!')
        ## If a player enters a room with a monster and has no weapon end game
    elif 'item' in rooms[currentRoom] and 'Pete The Fish' in rooms[currentRoom]['item'] and 'weapon' not in inventory:
        print('Pete The Fish has got you... GAME OVER')
        break
    # If spongebob not in inventory, you can't win, let user know
    if currentRoom == 'Secret Kitchen' and 'spongebob' not in inventory and 'formula' in inventory and 'spatula' in inventory:
        print('You found the secret Kitchen but YOU MUST FIND SPONGEBOB, DON\'T LET PETE THE FISH GET YOU')
    # If formula not in inventory, you can't win, let user know
    if currentRoom == 'Secret Kitchen' and 'formula' not in inventory and 'spongebob' in inventory and 'spatula' in inventory:
        print('You found the secret Kitchen but YOU MUST FIND THE SECRET FORMULA, DON\'T LET PETE THE FISH GET YOU')
    # If spatula not in inventory, you can't win, let user know
    if currentRoom == 'Secret Kitchen' and 'spatula' not in inventory and 'spongebob' in inventory and 'formula' in inventory:
        print('You found the secret Kitchen but YOU MUST FIND THE SPATULA, DON\'T LET PETE THE FISH GET YOU')
    # If spatula and Spongebob not in inventory, you can't win, let user know
    if currentRoom == 'Secret Kitchen' and 'spatula' not in inventory and 'spongebob' not in inventory and 'formula' in inventory:
        print('You found the secret Kitchen but YOU MUST FIND THE SPATULA AND SPONGEBOB, DON\'T LET PETE THE FISH GET YOU')
    # If spatula and formula not in inventory, you can't win, let user know
    if currentRoom == 'Secret Kitchen' and 'spatula' not in inventory and 'formula' not in inventory and 'spongebob' in inventory:
        print('You found the secret Kitchen but YOU MUST FIND THE SPATULA AND FORMULA, DON\'T LET PETE THE FISH GET YOU')
    # If Spongebob and formula not in inventory, you can't win, let user know
    if currentRoom == 'Secret Kitchen' and 'spongebob' not in inventory and 'formula' not in inventory and 'spatula' in inventory:
        print('You found the secret Kitchen but YOU MUST FIND THE FORMULA AND SPONGEBOB, DON\'T LET PETE THE FISH GET YOU')
    # If nothing in inventory, you can't win, let user know
    if currentRoom == 'Secret Kitchen' and 'spongebob' not in inventory and 'formula' not in inventory and 'spatula' not in inventory:
        print('You found the secret Kitchen but YOU MUST FIND THE FORMULA, SPATULA AND SPONGEBOB, DON\'T LET PETE THE FISH GET YOU')
    ## Define how a player can win
    if currentRoom == 'Secret Kitchen' and 'spongebob' in inventory and 'formula' in inventory and 'spatula' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break