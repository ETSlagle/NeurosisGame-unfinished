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

# character code-------------------------------------------------------------
class character:

    def __init__(self, name, hp, items):
        self.name = name
        self.hp = 100
        self.items = []

# character code-------------------------------------------------------------

# items code-------------------------------------------------------------

class item:
    def __init__(self, name, use):
        self.name = name
        self.use = use

recall_watch = item('name', 'use')
recall_watch.name = "Recall Watch"
recall_watch.use = "Create a function for use"


    #def recall():
        #print("Idk yet.") #this is the primary function of the game in which you will
        #be able to recall your action to your last decision, it will need to be able to take you
        #back to that last decision and have a counter of three that decreases by 1 per use
        #and upon reaching 0 should not be able to be used anymore


# items code-------------------------------------------------------------


# rooms code-------------------------------------------------------------
class room:

    def __init__(self, load_text, parent_room, straight_room, left_room, right_room, room_options):
        self.load_text = load_text
        self.parent_room = parent_room
        self.straight_room = straight_room
        self.left_room = left_room
        self.right_room = right_room
        self.room_options = room_options

    def navigate(self):
        if self.choice == "Straight":
            return self.straight_room
        elif self.choice == "Left":
            return self.left_room
        elif self.choice == "Right":
            return self.right_room
        elif self.choice == "Back":
            return self.parent_room

    def get_input(self):
        self.choice = input("> ")

    #def room_intro(self):



R1 = room('load_text', 'parent_room', 'straight_room', 'left_room', 'right_room', 'room_options')
R1.load_text = "This is the beginning."
R1.room_options = {'Straight': 1, 'Left': 2, 'Right': 3}

R2 = room('load_text', 'parent_room', 'straight_room', 'left_room', 'right_room', 'room_options')
R2.load_text = "This is the second room."
R2.room_options = {'a': 1, 'c': 2, 'b': 3}

R3 = room('load_text', 'parent_room', 'straight_room', 'left_room', 'right_room', 'room_options')
R3.load_text = "This is the third room."
R3.room_options = {'a': 1, 'c': 2, 'b': 3}

R4 = room('load_text', 'parent_room', 'straight_room', 'left_room', 'right_room', 'room_options')
R4.load_text = "This is the fourth room."
R4.room_options = {'a': 1, 'c': 2, 'b': 3}


R1.straight_room = R2
R1.left_room = R3
R1.right_room = R4

R2.parent_room = R1

R3.parent_room = R1

R4.parent_room = R1



# rooms code--------------------------------------------------------



# primitive intro code----------------------------------------------
def deathintro():
   Best_Friend = input("> ")
   print("You awaken, slightly delirious, to find yourself standing amongst a sea of headstones.")
   time.sleep(2)
   print(f"The headstone directly in front of you reads, {Best_Friend}.")
   time.sleep(1)
   print(f"You look down at the watch that {Best_Friend}, had given you long ago.")
   time.sleep(1)
   print("The watch has long stopped working, but you cherish it all the same.")
   time.sleep(1)
   print("The sun is setting, and a thought crosses your mind.\nShould I leave the watch behind as a final goodbye or keep it for myself.")

   choice = input("> ")

   if "l" or "L" in choice:
       greetings()


   elif "k" or "K" in choice:
       print("The watch starts to burn your skin, and you frantically remove it to set it on the headstone.")
       greetings()

   else:
       print("That is not an option. Your fear consumes you.")
       start()

def greetings():
   ingredients = ['Water 35 Liters', 'Carbon 20 Kilograms', 'Ammonia 4 Liters']
   print("As you set the watch on your friend's headstone, a shadowy figure slowly comes into view.")
   time.sleep(1)
   print("He wears a long black cloak, however it doesn't appear to be solid.\nHis face can not be seen as if a shroud of gray mist cloaks his identity.\nHe extends a gaunt hand and gently removes the watch from the headstone.")
   print("He lifts his head in your direction and asks: Was this individual important to you?")

   choice = input("> ")

   if choice == "yes" or choice =="Yes":
       print(f"Well then, I have a proposition for you. If you can bring me these ingredients\n{ingredients}, then I will return the friend you so dearly miss.")
       print("However, be warned these ingredient can not be obtained in this world.\nInstead you must venture into the underworld, to aid you on your journey I will grant you the power of time.")
       print("He then reaches out a gaunt hand, takes the watch and lightly taps the face with 2 slender fingers.\nHe looks to you and says:\n'You need only command it to recall to get yourself out of a bind, but be cautious, you see, it's uses are limited to 3.'")
       print("Now get going, time stops for no one.\nWith a sarcastic grin he cloaks you in darkness as he casts you to the underworld.")
       underworld_intro()

   elif choice == "no" or choice == "No":
       print("You wish to deceive me then? No matter, I can see your true intentions.\nBring me these ingredients {ingredients}, and only then will your friend be returned to you.")
       print("However, be warned these ingredient can not be obtained in this world.\nInstead you must venture into the underworld, to aid you on your journey I will grant you the power of time.")
       print("He then reaches out a gaunt hand, takes the watch and lightly taps the face with 2 slender fingers.\nHe looks to you and says:\nYou need only command it to recall to get yourself out of a bind, but be cautios, you see, it's uses are limited to 3.")
       print("Now get going, time stops for no one.\nWith a sarcastic grin he cloaks you in darkness as he casts you to the underworld.")
       underworld_intro()

   else:
       greetings()

def underworld_intro():
   print("You awaken, covered in a shrouded cloak much like the one the slender man had been wearing.\nLooking around you seem to be in an extensive cavern, with many passageways in all directions.\n1.Straight\n2.Left\n3.Right\n4.Back")

def start():
   print("Welcome to NEUROSIS.\nWhat you are afraid to do is a clear indication of what must be done next.")
   print("Now, what do you fear most?\n1.Death\n2.The Unknown\n3.A Sense of Purpose")

   choice = input("> ")

   if choice == "1" or choice == "Death":
       print("So, death is what you fear is it?\nThen let us journey together, will you conquer your fear, or will you let it swallow you?")
       print("But first, what is the name of your best friend?")
       deathintro()

   elif choice == "2" or choice == "The Unknown":
       print("So, the unkown is what you fear is it?\nThen let us journey together, will you conquer your fear, or will you let it swallow you?")

   elif choice == "3" or choice == "A Sense of Purpose":
       print("So, purpose is what you fear is it?\nThen let us journey together, will you conquer your fear, or will you let it swallow you?")

   else:
       print("You can not run from your fears!")
       start()


# primitive intro code----------------------------------------------


# game loop----------------------------------------------------------

current_room = R1

start()
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
