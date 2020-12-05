#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:33:38 2019

@author: smile
"""

#Program to genreate the factorial of any positive integers
print("Input a postive integer Number")

def goto():#function to ensure input is integer
    while True:
        try:
            x=int(input(">: "))
        except ValueError:
            print("integers only")
 #       x = input("> ")
        else:
            return x
    
fa=1
x=goto()
while x<=0 :#check if the input is less than 0
    print("Input a postive integer Number greater than zero(0)")
    x=goto()

for c in range(1,x+1):#factorial generator
    fa=fa*c

print(fa)