#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:36:35 2019

@author: smile
"""

import pandas as p
import numpy as n

var=(1,2,3,4,5,6,7,8,9,10)
ar=n.ones((3,4))
len(ar)

v3={'Team A':['Nigeria','USA','Germany'],'Team B':['Ghana','Croatia','France']}
dr=p.DataFrame(data=v3,index=[1,2,3])
print (dr)
ans=[]
ans=[2+i for i in range(4)]
#for i in range(4):val=2+i;ans.append(val)

print(ans)


import matplotlib.pyplot as pl
lt=([1,4,7,8],[5,6,7,6])
pl.plot(lt[0],lt[1])
pl.show()

pl.hist(lt[0])
pl.show()