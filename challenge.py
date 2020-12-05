



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 22:35:35 2019

@author: smile
"""

ss =input("Input a number: ")

while True:
    try:
        int(ss)
    except ValueError:
        print("Only integers are allowed")
        ss =input("Input a number: ")
    else:
        break

ss=int(ss)
if ss % 2 == 1 and ss < 20:
    print("Odd-Weird")
elif ss in range(2,5):
    print("even Not weird", ss)
elif ss in range(6,20):
    print("Weird ",ss)
elif ss > 20:
    print("Weird too",ss)
else:
    print("We are doing nothing")