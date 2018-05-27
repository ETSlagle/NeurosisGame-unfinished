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

    def __init__(self, load_text, parent_room, room_options, choice):
        self.load_text = load_text
        self.parent_room = parent_room
        self.room_options = room_options
        self.choice = choice

    def navigate(current_room):
        if current_room.choice == "Straight":
            current_room = room.R2
        elif current_room.choice == "Back":
            current_room = current_room.parent_room



R1 = room('load_text', 'parent_room', 'room_options', 'choice')
R1.load_text = "This is the beginning."
R1.parent_room = 0
R1.room_options = {'Straight': 1, 'Left': 2, 'Right': 3}
R1.choice = input("> ")

R2 = room('load_text', 'parent_room', 'room_options', 'choice')
R2.load_text = "This is the second room."
R2.parent_room = R1
R2.room_options = {'a': 1, 'c': 2, 'b': 3}
R2.choice = input("> ")


R3 = room('load_text', 'parent_room', 'room_options', 'choice')
R3.load_text = "This is the third room."
R3.parent_room = R2
R3.room_options = {'a': 1, 'c': 2, 'b': 3}
R3.choice = input("> ")





current_room = R1

#while True:
print(current_room.load_text)
print(current_room.room_options)
print(current_room.choice)
room.navigate(current_room)

#game loop

    #fix list of ingredients so that the brackets and quotation marks dont show up


    #the premise of the game is to have 3 different paths from which you can choose your adventure
    #currently the intro is the only functioning portion
    #the first path is the one I am working on currently, but i havent continued forward in the dungeon part
    #because I want to improve or get suggestions on the formatting
