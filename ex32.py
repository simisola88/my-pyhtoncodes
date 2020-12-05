#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 01:18:54 2019

@author: smile
"""
ct = [1,2,3,4,5]
fruit = ['apples','oranges','peers','apricots']
tt = [1,'pennies',2,'dimes',3,'quaters']

#printing the contents of each list

for c in ct:
    print("This is count",c)
    
for f in fruit:
    print(f,' is a type of fruit')

for d in tt:
    print("I got ",d)    

nw =[]
for a in range(1,6):
    print("Adding %d to the list"%a)
    nw.append(a)
for fd in nw:
    print("Element was: ",fd)