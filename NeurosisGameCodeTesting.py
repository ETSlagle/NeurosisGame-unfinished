#Notes: finish function for room_intro (text describing each room as you enter)
#       fix the room options, it's a hash right now for no reason
#       re-work the introduction code from the extreme beta version
#       also maybe change up the story a little bit, that can be done at any point though
#       figure out how the main game mechanic (the recall watch) is going to work, cuz i have no idea rn other than I know it needs a counter
#       research how i should format my code to work when applied to a user interface (polished game)
#       add enemies, obstacles, items




from sys import exit
import random
import time
from random import randint


#class player:
    #max_health
    #current_health
    #inventory

#class item:
    #name
    #use

class room:

    def __init__(self, load_text, parent_room, child_room, room_options):
        self.load_text = load_text
        self.parent_room = parent_room
        self.child_room = child_room
        self.room_options = room_options

    def navigate(self):
        if self.choice == "Straight":
            return self.child_room
        elif self.choice == "Back":
            return self.parent_room

    def get_input(self):
        self.choice = input("> ")

    #def room_intro(self):

# I had to reorder the rooms from last, down to first in order to get the child_room
# attribute to work appropriately because when it was the other way the child_room was being seen as undefined
# this allows me to move forward through the rooms, but not back so I need to fix that
# Also this is guaranteed to have issues when there are multiple parent or child rooms


# The idea im working on below is to possibly solve the above issue, I believe if i sandwich
# the rooms, I can have the 'B' rooms as the ones that you are going back to
# therefore the B rooms define the parent rooms and the regular rooms define the child room_options
# other than that the code will mirror each other between R2 and R2B, R3 and R3B, and so on
# this will appear that it is the same room. However this may prove problematic with the addition of more
# complex things such as adding items into the mix because then that will have to be tracked over each pair


# also wondering if maybe i should make a whole new class for the B rooms rather than re-using
# the original 'room' class. Not sure if that would be beneficial or cause more problems


#### The above method has failed as you navigate back and forth you eventually end up in one of the 'B' rooms
#### and these may not have a child or parent room as described above and therefore the input to navigate
#### to a new room fails......................ugh


R1B = room('load_text', 'parent_room', 'child_room', 'room_options')
R1B.load_text = "This is the beginning."
R1B.parent_room = 0
R1B.child_room = 0
R1B.room_options = {'Straight': 1, 'Left': 2, 'Right': 3}


R2B = room('load_text', 'parent_room', 'child_room', 'room_options')
R2B.load_text = "This is the second room."
R2B.parent_room = R1B
R2B.child_room = 0
R2B.room_options = {'a': 1, 'c': 2, 'b': 3}

R3 = room('load_text', 'parent_room', 'child_room', 'room_options')
R3.load_text = "This is the third room."
R3.parent_room = R2B
R3.child_room = 0
R3.room_options = {'a': 1, 'c': 2, 'b': 3}


R2 = room('load_text', 'parent_room', 'child_room', 'room_options')
R2.load_text = "This is the second room."
R2.parent_room = R1B
R2.child_room = R3
R2.room_options = {'a': 1, 'c': 2, 'b': 3}


R1 = room('load_text', 'parent_room', 'child_room', 'room_options')
R1.load_text = "This is the beginning."
R1.parent_room = 0
R1.child_room = R2
R1.room_options = {'Straight': 1, 'Left': 2, 'Right': 3}



# game loop----------------------------------------------------------

current_room = R1

while True:
    print(current_room.load_text)
    print(current_room.room_options)
    current_room.get_input()
    current_room = current_room.navigate()

# game loop-----------------------------------------------------------





    # fix list of ingredients so that the brackets and quotation marks dont show up


    # the premise of the game is to have 3 different paths from which you can choose your adventure
    # currently the intro is the only functioning portion
    # the first path is the one I am working on currently, but i havent continued forward in the dungeon part
    # because I want to improve or get suggestions on the formatting
