#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 10:05:09 2019

@author: smile
"""

#create a mapping of state to abbrevaition
states ={
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':'NY',
        'Michigan':'MI'
        }
#create a basic set of states cities
cities={
        'CA':'Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
        }
#add some more cities
cities['NY']='New York'
cities['OR']='Portland'

#print out some cities
print('*'*11)
print ("NY states has: "+cities['NY'] )
print ("OR states has: "+cities['OR'] )

#print out cities by using states
print('*'*11)
print ("Michigan has: "+cities[states['Michigan']] )
print ("Florida has: "+cities[states['Florida']] )

#print every states in states
print('*'*11)
for state,abr in states.items():
    print("%s is abreviaites %s"%(state,abr))

#print every cities in cities
print('*'*11)
for city,abr in cities.items():
    print("%s is abreviaites %s"%(abr,city))

#print boths states and
print('*'*11)
for state,abr in states.items():
    print("%s is abreviaites %s with city %s"%(state,abr,cities[abr]))

#print every states in states
print('*'*11)
state = states.get('Texas')
#print(state)
#check if a state is in the dictionary
if not state:
    print("Sorry, no Texas")
city = cities.get('Texas','Does not exist')
print("Texas city is %s"%city)
