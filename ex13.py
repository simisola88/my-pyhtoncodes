#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 00:12:15 2019

@author: smile
"""

#This unpacks the arguments you pass to the script
#You must pass 5 arguments 

from sys import argv
script, first, second, third  = argv
fourth  = input("Enter the fourth argument: ")
print("Script ", script)
print("first ", first)
print("Second ", second)
print("Third ", third)
print("Fourth ", fourth)