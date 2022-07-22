# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:26:44 2021

@author: Anna
"""

def find_midpoint(first, last):
    """
    first, last are integers defining an interval from first to last inclusive
    returns the midpoint of the interval [first,last] 
    computed as first + (last-first)//2
    eg first=1, last=5, returns 3
       first =1, last=6 returns 3 
        first=3, last= 7 returns 5
        

    """
    
    return first + (last-first)//2

    
