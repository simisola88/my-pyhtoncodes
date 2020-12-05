#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:29:50 2019

@author: smile
"""

#Functions and files script

from sys import argv
#we provide the argument to the scripts
script, file = argv
#prints the file contents
def filePrint (fild):
    print(fild.read()+"\n")
#reset the file to start reading from line 1
def fileReset (fil):
    fil.seek(0)
#prints the file contents line by line
def filePrintLns (ss,fill):
    print(ss,"::",fill.readline())
#close the file
def fileclose(fila):
    fila.close()
#open the file and save its content to a variable
s = open(file)
print("Lets print first the contents of file ", file+"\n")
#calls the function
filePrint(s)
print("Now lets rewind, kind of like a tape")
#calls the function
fileReset(s)
print("we are  printing 3 lines, one after the other")
#initialize a to be 1
a = 1
#calls the function
filePrintLns(a,s)
#increment a
a +=1
#calls the function
filePrintLns(a,s)
#increment a
a +=1
#calls the function
filePrintLns(a,s)
print("Close the file")
#calls the function
fileclose(s)