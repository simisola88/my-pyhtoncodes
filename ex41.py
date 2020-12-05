#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 11:54:14 2019

@author: smile
"""

class song(object):
    def __init__(self, lyrics):
        self.lyrics=lyrics
        
    def sing_sing(self):
        for line in self.lyrics:
            print (line)

happybday = song(['Happy Birthday to you\n'*2,"I don't want to get sued",
                  "So I'll stop right there\n"])

bullsparade = song(["They rally around the family",
                    "With pockets full of shells"])
happybday.sing_sing()
bullsparade.sing_sing()

ss=['\n\nI write Name',
    'Not for shame',
    'But for Fame',
    'All the same',
    'I sign ny NAME']

song(ss).sing_sing()
