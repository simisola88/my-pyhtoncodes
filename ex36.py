#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 22:49:48 2019

@author: smile
"""
#This takes in 3 argument before running
#Run from the terminal by 
#python ex36.py arg1 arg2 arg3
from sys import argv
script, f1, f2, f3  = argv

print("We have 3 types of fruits in the basket\n Kindly guesss one")

c = input("> ")
c = c.lower()
c