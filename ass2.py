 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 23:52:29 2019

@author: smile
"""
def test(d):
    even = 0
    odd = 0
    jeven=[];jodd=[]
    for i in d:
        if i % 2 == 0:
            even+=1
            jeven.append(i)
        else:
            odd+=1
            jodd.append(i)
    return even,odd,jeven,jodd

#Program to count even and odd number from a list
odd=[]
even=[]
lst = [1,2,3,4,5,6,8,7,5]
a,b,even,odd = test(lst)
print("List: ", lst,"\n")
print("Even numbers are: ",even,"\nOdd numbers are :",odd,"\n")

#Program to count even and odd number from a tupple
qodd=[]
qeven=[]
tpl = (1,2,3,4,5,6,8,7,5)
c,b,qeven,qodd = test(tpl)
print("Tupple: ", tpl,"\n")
print("Even numbers are: ",qeven,"\nOdd numbers are :",qodd,"\n")
