#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 10:37:54 2019

@author: smile
"""
#program to play with list
i = 0
nn= []
while i < 6:
    print("At the top i is ",i)
    nn.append(i)
    i+=1
    print("Numbers now:",nn)
    print("At the bottom i is",i)

print("The numbers:")
for tr in nn:
    print(tr)
    
c = 0;s=6
ne = []
for df in range(0,s,2):
    print("At the top c is ",c)
    ne.append(df)
    print("Numbers now:",ne)
#    print("At the bottom c is",c)

print("The numbers:")
for tr in ne:
    print(tr)