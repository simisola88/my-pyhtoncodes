#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:02:06 2019

@author: smile
"""
#import the numpy package 
import numpy as np
list = range(6)
it = iter(list)
x =np.fromiter(it , dtype=int)
print (x)
