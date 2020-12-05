#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:39:56 2019

@author: smile
"""

print("You enter a dark room with two doors, Do you go through door #1 or #2")
s = int(input("> "))
if s == 1:
    print("Door #1 choosen")
    print("There's a giant bear eating a cake!!!, what will you do")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    d = int(input("> "))
    if d == 1:
        print("The bear eats your legs off. Good job!")
    elif d == 2:
        print("The bear growls at you and eat your legs off. Good job!")
    else:
        print("You did'nt do anything... wise choice, you are safe")
elif s==2:
    print("Door #2 choosen")
    print("Cograts you are free")
else:
   print ("You stumble around and fall on a knife and die. Good job!!!")
