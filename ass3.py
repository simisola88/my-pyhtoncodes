#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 23:46:29 2019

@author: smile
"""

#Program to print out number divisible by 7 and 5 between 1-3000
lst= []
for i in range(1,3000):
    if i % 7 == 0 and i % 5 ==0:
        lst.append(i)

print("Numbers divisible by 7 and 5 in 1 - 3000 are: \n",lst)