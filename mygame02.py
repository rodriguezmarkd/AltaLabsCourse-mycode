#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

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

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    ## Added movement history vv
    print('History:', history)
    ## Added number of moves vv
    print('Number of moves: ', movecount)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []
## Two new variables to track movecount and history
movecount = 0
history = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster',
                },
            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
                },
            'Garden' : {
                'north' : 'Dining Room',
                'south' : 'Shed'
                },
            'Shed' : {
                'north' : 'Garden',
                'item' : 'hammer'
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

    ##Added new check for teleport functionality, checks to see if room exists, and then changes
    ##current room, appends the move to history and adds a movement penalty of 10
    if move[0] == 'teleport':
        if move[1].title() in rooms.keys():
            currentRoom = move[1].title()
            history.append(move[1])
            movecount = movecount + 10

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            ## If successful move, history is appended and movecount is increased one
            history.append(move[1])
            movecount = movecount + 1
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

    ## If a player enters a room with a monster
    ## If player enters room with monster, checks to see if hammer is in inventory, causing monster to not end game
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'hammer' in inventory:
        print('A monster sees your hammer and flees the room')
    ## If monster is in room and hammer not in inventory, ends game
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        ## Added movement count as final score
        print('Final Score: ', movecount)
        break

