#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:41:00 2019

@author: smile
"""
#this script will copy contenets of one file to another file

from sys import argv
from os.path import exists

script, from_file, to_file  = argv

print ("We are copying {a} to {b}".format(a=from_file, b=to_file))
txt = open(from_file)
data = txt.read()

print("The input file has {a} bytes long".format(a=len(data)))

print("Does the output file exist?\t",exists)
print("Ready!!!!, Hit the RETURN key to continue or CTRL+C to abort")
input("???")

txt2 = open(to_file, 'w')
txt2.write(data)

print("Operation Complete")
txt.close(); txt2.close()