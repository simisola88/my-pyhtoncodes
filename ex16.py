#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 07:12:18 2019

@author: smile
"""
#script to play with files
from sys import argv
script, filename  =  argv

print("We are going to erase the content of this files")
print ("If you dont want that, hit CTRL+C")
print ("hit the RETURN key to proceed")
input("?")
txt = open(filename, 'w')
print("Opening the file....")
txt.truncate()
print("Truncating the file")
print("Now I'm going to ask you for 3 lines")
line1 = input("Line 1:\t")
line2 = input("Line 2:\t")
line3 = input("Line 3:\t")
print("I'm writing this files lines in the script")
txt.write(line1)
txt.write('\n')
txt.write(line2)
txt.write('\n')
txt.write(line3)
txt.write('\n')

print("And finally close it")
txt.close()

print("We are now using write line")
filename = input("Enter the name of the file")
txt = open(filename, 'w')
print("Opening the file....")
txt.truncate()
print("Truncating the file")
print("Now I'm going to ask you for 3 lines")
line1 = input("Line 1:\t")
line2 = input("Line 2:\t")
line3 = input("Line 3:\t")
print("I'm writing this files lines in the script")
txt.writelines(line1+'\n'+line2+'\n'+line3+'\n')

print("And finally close it")
txt.close()
