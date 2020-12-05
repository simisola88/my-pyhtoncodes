#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:57:52 2019

@author: smile
"""

import psycopg2 as pg
conn = pg.connect(database="testdb",user="simi",password="simisola", host="127.0.0.1", port="5432")
print("connection successfull")

cur = conn.cursor()
cur.execute("INSERT INTO NAMES (ID,MALENAME,FEMALENAME) \
            VALUES (2,'Ayodejis','Simibola')")
#a= cur.execute("SELECT * FROM NAMES;")
#print('result = ',a)
conn.commit()
conn.close()

2**38