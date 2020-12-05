#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:14:55 2019

@author: smile
"""

#this is a function script
#it accepts two integer vairiables and sums it up
def simi(a,b):
    c = a + b
    print("Result is ",c)

v1 = input ("enter the first variable\t")
v2 = input ("enter the second variable\t")
#converts the vairiables to integers
v1 = int(v1); v2 = int(v2)
simi(v1, v2)