from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","South of you, doors becon", []),

    'foyer':    Room("Foyer", """Dim light filters in from the North. Dusty
passages run west and east.""",[Item("torch","the glow from this torch can light up a room")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
    
    'library': Room("#       Library          #", """you have found a place for reading. Unfortunately in
    your adventures you never learned the Dewey Decimal System so finding books is very 
    difficult""", []),

    'storageroom': Room("#        storageroom       #", """This room contains crates of foodstuffs
    and spices, in addition to cleaning rags, brooms, broken chairs, and tools for repairing 
furniture""", []),

    'lounge': Room("#       lounge      #", """Although smooking is allowed anywhere in the Tavern, this
lounge is a favorite hangout for memebers of a local smokers' club called the Puffers Fishers. Most of
the club members are local fishers and crab catchers.""", []),

    'kitchen': Room("#        Kitchen        #", """There are three cooks employed to prepare 
    meals: a cheery executive chef named Chenna Fatrabbit, a testy sous chef named Azar Valsheem, and a 
    blind pastry chef named Klav Martilmur. They work from highsun to midnight. Their specialties are 
    fish cakes, crab cakes, a thick cheese-and-potato soup, and loaf pudding soaked in syrup and 
    decorated with lightly salted almonds. """, [] ),
    
   'staircase': Room("#        Staircase         #", """You walk up an iron railing staircase. to your 
   right are assorted pictures of a family. You dont recognize any of them. but they look 
   happy """, []),
    
   'secretroom': Room("#        An unplaned room which has no name       #", """you find a secret room of 
   someones design. outfitted with a small collection of books and a desk. you wonder if anything here
   is worth keeping a secret? you see a dimmly lit staircase going down""", []),

   'sprialstaircase': Room("#       ~Sprial Staircase~        #", """a large sprial staircase decends 
    into darkness lit only by the light of a single torch on the wall""", []),
    
   'landing': Room("#        Staircase Landing       #", """the staircase ends on a landing to the west 
   a large room. to the east you see streaks of light from a window at the end, rooms on both sides of 
   the hallway""", []),

    'longhallway1': Room("#      Hallway      #", """a room door on to the north, a room door to the
    south. East the hallway continues""", []),

    'longhallway2': Room("#     Hallway     #", """a room door on the north, a room door to the south, 
    the hallway continues to a door to what looks like a balcony""", []),

    'fancyguestsuite': Room("#      Bedroom       #", """This room is currently unoccupied, the richly 
    appointed room contains velvet curtains framed painting of ships, a canopied bed, a night table, a 
    sea chest, and a wardrobe.""", []),

    'largeguestroom': Room("#      Bedroom       #",  """This room contains an unusual guest: a 
    preistess named Oshalla. She wears a cloak made from fishing nets. She was exiled from the depths for
    plotting a coup against her king. Oshalla keeps to herself and has her meals brought to her three
    times per day. The door to her room is locked, and she wears the key on a cord around her neck. In 
    addition to a bed, night table, and a chest, this room contains a desk, a chair, several paintings 
    of coastal and underwater scenes, a portable bathtub, and a 10 foot long, 8 foot tall bookcase that
    holds Oshalla's collection of trinkets collected from the ocean (shells, barnacle-covered skulls, and 
    the like) Oshalla doesn't allow the tavern staff to clean her room or refresh water in the tub, so
    both are filthy. """, []),

    'plainguestroom ': Room("#       Bedroom      #", """This room contains a cozy bed, and empty wooden
    chest, and curtains on the window. """, []),
    
   'balcony': Room("Balcony", """you find a door to a balcony, stepping out fresh air greets you. West 
   to go back inside""", [])


}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['staircase']
room['foyer'].w_to = room['lounge']
room['lounge'].n_to = room['kitchen']

room['kitchen'].e_to = room['storageroom']
room['storageroom'].w_to = room['kitchen']
room['staircase'].n_to = room['landing']
room['foyer'].e_to = room['library']
room['staircase'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['foyer']
room['treasure'].s_to = room['narrow']


#upstairs
room['landing'].e_to = room['longhallway1']
room['longhallway1'].e_to = room['longhallway2']
room['longhallway1'].w_to = room['landing']
room['longhallway1'].s_to = room['largeguestroom']
room['largeguestroom'].n_to = room['longhallway1']
room['longhallway1'].n_to = room['fancyguestsuite']
room['fancyguestsuite'].s_to = room['longhallway1']

room['longhallway2'].e_to = room['balcony']
room['balcony'].w_to = room['longhallway2']
room['longhallway2'].n_to = room['bedroom3']
room['plainguestroom'].s_to = room['longhallway2']

room['library'].key_to = room['secretroom']
room['secretroom'].s_to = room['sprialstaircase']
room['secretroom'].n_to = room['library']
room['sprialstaircase'].n_to = room['secretroom']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Jessica = Player(
    name = "Jessica",
    room = room['outside']
)

cmd = input("Enter a direction ")

def print_room_info():
    print(Jessica.room.name + ":")

    print(Jessica.room.description)

    Jessica.room.view_items()


action = cmd    
parsed_cmd = cmd.split()

if action == "g" or action =="grab":
    for i in Jessica.room.items:
        if cmd[1] == i.item:
            print("grabbing item")
            Jessica.items.append(i)
            Jessica.room.items.remove(i)


if len(parsed_cmd) > 1:
    action = parsed_cmd[0]


    for i in range(1, len(parsed_cmd)):
        item += parsed_cmd[i] + " "
    item = item.strip()

    if action == "g" or action == "grab":
        if parsed_cmd[1].name in Jessica.room.items:
            print("...grabbing item")


dir = ""

while not dir == "q":
    print(Jessica.room.name)
    print(Jessica.room.description)
    if Jessica.room.items != None:
        print(Jessica.room.items)
    



    dir = input('please enter a direction...n, s, e, w, or q to quit the game')
    parsed_cmd = dir.split()
    if len(parsed_cmd) == 2:
        if parsed_cmd[0].lower() == "get":
            print(f"{parsed_cmd[1]} picked up")
            # put item name
            Jessica.items.append(Jessica.room.items[0])
            print(Jessica.items)

    if dir == "n":
        if hasattr(Jessica.room, "n_to"):
            Jessica.room = Jessica.room.n_to

        print('#BAM!~~~~~ a wall finds your forehead. Try another path')
        
    elif dir =="s":
        if hasattr(Jessica.room, "s_to"):
            Jessica.room = Jessica.room.s_to
        
        print('#BAM!~~~~~ a wall finds your forehead. Try another path')

    elif dir == "e":
        if hasattr(Jessica.room, "e_to"):
            Jessica.room = Jessica.room.e_to

        print('#BAM!~~~~~ a wall your forehead. Try another path')

    elif dir == "w":
        if hasattr(Jessica.room, "w_to"):
            Jessica.room = Jessica.room.w_to

        print('#BAM!~~~~~ a wall finds your forehead. Try another path')

    elif dir != "w" and "e" and "s" and "n":
        print('#BAM!~~~~~ a wall finds your forehead. Try another path')


print("Game Exited .... or did the game exit you?")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
