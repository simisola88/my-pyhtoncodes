#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:16:53 2019

@author: smile
"""
stuff = "Yam beans Egg plantain Coke"
morestuff = "Bread Akara Dodo Rice sausage meat-pie"
stuff = stuff.split()#split the variable into a list
morestuff = morestuff.split()#split the variable into a list
print(stuff)
while len(stuff)< 10:
    print("There are less than 10 things in the lsit")
    s = morestuff.pop()
    print("Adding: ",s)
    stuff.append(s)
    print("there are now %d items"%len(stuff))
print("There we go: ",stuff)
print ("Let's do some stuffs with the list")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff[3:8]))#print the list contents joined with a space 
print('-'.join(stuff[3:8]))#print the list contents joined with a space 