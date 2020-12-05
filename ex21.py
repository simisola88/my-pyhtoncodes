#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:20:40 2019

@author: smile
"""

def add(a,b):
    print("Addindg ",a," + ",b)
    return a + b
def subtra(a,b):
    print("Subtracting ",a," - ",b)
    return a - b
def multiply(a,b):
    print("Multiplying ",a," * ",b)
    return a * b
def divide(a,b):
    print("Dividing ",a," / ",b)
    return a/b
age = add(30,5)
height = subtra(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: %d, Height: %d, Weight: %d, iq: %d"%(age,height,weight,iq))

print("Here is a puzzle")
what =add(age,subtra(height,multiply(weight,divide(iq,2))))
print("That becomes: ",what,"can you do it by hand??")