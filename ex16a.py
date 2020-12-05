#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:33:24 2019

@author: smile
"""
#script to read file and print out the contents
from sys import argv
script, filename =  argv
txt =  open(filename, 'r')
print(txt.read())
txt.close()