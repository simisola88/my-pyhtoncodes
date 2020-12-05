

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:52:02 2019

@author: smile
"""

# A is the list of arrays
# I is the value whose positions is to be found
# l is the lower boundary i.e starting index 
# u is the upper boundary i.e ending index
# m is the midpoint between the upper boundary and lower boundary

def binary_search(A, I):
	#set l = 0
	l = 0
	# set u to index of length of array 
	u = len(A) -1
	
	#check if lower boundary <= upper boundary
	while l <= u:
		#then set midpoint 
		m = int((l+u)/2)
        #check if midpoint in array = item
		if A[m] == I:
			#return if found and the position
            dd = str(I)+' found at position '+ str(m)
			return  dd
		#check if midpoint in array > item
		elif A[m] > I:
		#set another midpoint
			u = m - 1
		#check if midpoint in array < item
		elif A[m] < I:
			l = m + 1
		#return if there is no match
		else:
			return '{%s} not found in the list'%(I)

A = [0,1,2,3,4,5,6,7,8,9]
print(binary_search(A,8))
		