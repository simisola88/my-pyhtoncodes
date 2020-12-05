#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:38:36 2019

@author: smile
"""

print("Let's pratice everything")
print("You\'d need to know \'bout escapes with"+
      "\\ that do\nnewlines and \t tabs.")
poem = """ This lovely world
with logic so firmly planted
cannot discern\n\tthe eeds if love
nor comprehend passion from intuition
and reruires an expalnation
\n\t where there is none."""

print("------------------------")
print(poem)
print("------------------------")

def sampleProd(ad):
    abbeans = ad * 1000
    abjars  = ad * 500
    abcrates = ad * 5
    return(abbeans,abjars,abcrates)
starting = 12
bean, jars,crates = sampleProd(starting)
print("with a starting point of :", starting)
print("We'd have ",bean," beans, ",jars," jars, and ",crates," crates")
print("We can also do it like this")
starting *=2
print("We'd have %d beans, %d jars, and %d crates"%sampleProd(starting))