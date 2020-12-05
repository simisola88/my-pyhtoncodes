#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 00:09:10 2019

@author: smile
"""

#script password validity

p = """ Password must meet the folloeing requirenets
\t-at least one capital and small letter
\t-at least one digit 0-9
\t-between 8-16 character long
\t-at least !,@,#,%,&,?"""
def num(wd):
    c=0
    for dd in wd:
        if dd.isnumeric():
            c+=1
    if c>=1:
        return True
    else:
        return False
def spe(wd):
    tt = ('!','@','#','%','&','?');c=0
    for jj in tt:
            if wd.find(jj) != -1:
                c+=1
    if c>=1:
        return True
    else:
        return False    
    
def lower(wd):
    c=0
    for dd in wd:
        if dd.islower:
            c+=1
    if c>=1:
        return True
    else:
        return False        
    
def upper(wd):
    c=0
    for dd in wd:
        if dd.isupper:
            c+=1
    if c>=1:
        return True
    else:
        return False    

def size(wd):
    if len(wd)>8 and len(wd)<=16:
        return True
    else:
        return False
def alpha(wd):
    if lower(wd) and upper(wd) and size(wd):
        return True
    else:
        return False
       
print("Please kindly provide a password to check")
print("Password must meet the following requirements:\n",p)

pwd = input("Kindly input a password "); 
wd = True
while wd:
    if alpha(pwd) and spe(pwd) and num(pwd):
        print("\n#########Password is Valid!!!!###########\n\t\tGoodBYE!!!")
        wd = False
        exit
    else:
        print("\n********Invalid Password********")
        print("\nPlease kindly provide a password to check\n",p)
        pwd = input("Kindly input a password ")
        