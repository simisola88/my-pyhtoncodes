#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:03:58 2019

@author: smile
"""
#script to read baby names from html and save the result in a database

#improt the regular expression module
import re
#open and read the baby name file located in our current working dir
s=(open('baby2008.html')).read()
s
#use regex to fikter out the name and return the answer in a list of tuples
i = re.findall(r"<td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>", s)
#get each item of the list
for c in i:
    print(c[0])
    
