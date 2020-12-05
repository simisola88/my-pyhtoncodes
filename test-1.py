#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:54:14 2019

@author: smile
"""
import re
#open and read the baby name file located in our current working dir
s=(open('testbeginners/python_class_test.html')).read()
s
#use regex to filter out the name and return the answer in a list of tuples
#days = re.findall(r"<td>(\w*)</td>", s)
data= re.findall(r"<td>([\w, ]+)</td>", s)
days = [];colours=[]
a=0
while a < len(data):
    days.append(data[a])
    colours.append(data[a+1])
    a+=2
#get each item of the list
#print(days)
print(colours)
print(days)
len(colours)    
allcolours='';
for i in colours:allcolours=allcolours + i 
allcolours.count()
allcolours.find("PINK")
colfreq={}
colfreq['BLUE']=allcolours.count("BLUE")
colfreq['GREEN']=allcolours.count("GREEN")
colfreq['YELLOW']=allcolours.count("YELLOW")
colfreq['BROWN']=allcolours.count("BROWN")
colfreq['PINK']=allcolours.count("PINK")
colfreq['ORANGE']=allcolours.count("ORANGE")
colfreq['CREAM']=allcolours.count("CREAM")
colfreq['RED']=allcolours.count("RED")
colfreq['WHITE']=allcolours.count("WHITE")
colfreq['ARSH']=allcolours.count("ARSH")
allcolours
colfreq