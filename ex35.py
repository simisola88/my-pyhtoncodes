#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:03:40 2019

@author: smile
"""

from sys import exit
#this is a program to play with functions
def gold_room():
    print("This room is full of gold, How much  will you take?")
    print("Enter a number")
    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")
    
    if how_much < 50:
        print("Nice, you are not greedy, You win!!!")
        exit()
    else:
        dead("You greedy b******d")

def bear_room():
    print("There is a bear here. \nThe bear has a bunch of honey.")
    print("The fat bear is in front of another door.\nHow are you going to move the bear?")
    print("Enter 'Take honey'or 'Taunt bear' or 'Open door'")
    bear_moved = False
    
    while True:
        next = input("> ")
        
        if next == "Take honey":
            dead("The bear looks at you and slaps your face off")
        elif next == "Taunt bear" and not bear_moved:
            dead("The bear get pissed off and chew off your leg. ")
        elif next == "Open door" and not bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do flee for your life or eat your head")
    print("Enter - 'flee' or 'head'")
    next = input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
    
def dead(why):
    print(why, " Good Job!")
    exit()

def start():
    print("You are in a dark room.\nThere is a door to your right and left.")
    print("Which one do you take?\n Enter 'left' or 'right'")
    next =input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around until you serve")

start()
    