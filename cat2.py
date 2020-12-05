
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:19:12 2019

@author: smile
"""
#The cat function of linux for any number of files
from sys import argv
a=argv

for w in a[1:]:
    print(w)
    ff = open(w)
    print(ff.read())
    ff.close()