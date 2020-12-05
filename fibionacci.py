#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 09:16:26 2019

@author: smile
"""
def fib(cc):
    a=0 #first term
    b=1 #second term
    c=0
    term=[]
    term.append(a)
    term.append(b)
    c=a+b #3rd term
    while cc>2:
        a=b
        b=c
        c=a+b
        term.append(c)
        cc-=1
    return term
    
#this is a fibionacci generator
while True:
    try:
        n=int(input('Enter a number: '))
    except ValueError:
        print("Integers values only")    
    else:
        break
    
    
    
print("the %d term are "%n,fib(n))

#sum of the first 50 
s=fib(50)
sum =0
for aa in s:
    sum+=aa
print("sum of the first 50 terms: ",sum)