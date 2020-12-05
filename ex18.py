#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:26:28 2019

@author: smile
"""

#this is a function example
#this works like script argv
def print1(*args):
    arg1, arg2 = args
    print("arg1: "+arg1 , "arg2: "+arg2)

#this takes in three arguments
def print2(a,b,c):
    print("a  =",a ,"b =",b , "c = ",c)
    
#this takes no arguments
def print0():
    print("This takes no argument")
print1("Ade","Simi")
print2(3,"Simi", 4)
print0()