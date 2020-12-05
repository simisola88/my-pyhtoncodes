#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:31:40 2019

@author: smile
"""
"""
Library to install
pandas
matlib
urlib
scphy
mysqldb
numpy

"""
class Employee:
    'Employee count'
    empcount = 0
    
    def __init__(self, name, slry):
        self.name = name
        self.slry = slry
        Employee.empcount += 1
        
    def dispcount(self):
        print('Total employee count is $d'%Employee.empcount)
        
    def disslry(self):
        print('Name: '+self.name+'  Salary: ',self.slry)

"instantiating the class <<employee"

simi=Employee("Simisola", 900000)
sola=Employee("Ayodeji", 800000)
ayo =Employee('Tola', 5060600)
simi.disslry()
ayo.disslry()
simi.disslry()
print("Numbers of employees {}".format(Employee.empcount))


