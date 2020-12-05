#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 06:29:01 2019

@author: smile
"""

#This sript opens a file and displays the output
#you have to pass in the argv

from sys import argv
#expands the argv
script, filename  = argv
#opens the file and send the output to var txt
txt = open(filename)
#print out the filename
print ("The file opened is: ", filename)
#print out the openned file
print (txt.read())
#close the file
txt.close()

print ("Type the filename again")
filename1 = input(":>")

txtagain = open(filename1, mode= 'a')
txtagain.write("Opps hope i didn't mess things up")
#print(txtagain.read())
txtagain.close()