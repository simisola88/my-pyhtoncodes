#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 06:46:02 2019

@author: smile
"""

#scripts to play with files
def breakword(ss):
    """This function will break words for us"""
    word = ss.split(' ')
    return word

def sortword(words):
    """sort the words"""
    return sorted(words)

def printfirstword(words):
    """Prints the first word after popping it off"""
    wd = words.pop(0)
    return wd

def printlastword(words):
    """print out the lase word after popping it off"""
    wd = words.pop(-1)
    return wd

def sortsentence(sentence):
    """Takes a full list of sentense and returns its word sorted"""
    word = breakword(sentence)
    return sortword(word)

def printfirstandlastsentence(sentence):
    words = breakword(sentence)
    printfirstword(words)
    printlastword(words)
    
    