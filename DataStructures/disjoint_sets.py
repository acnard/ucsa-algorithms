# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:32:01 2022

@author: Anna
"""
import itertools


class Set(object):
    id_iter = itertools.count()
    def __init__(self, vals):
        """
        vals is a list of ints, can be empty, representing the 
        initial values contained in the set
        """
        self.id = next(Set.id_iter)
        self.vals = vals
        
    def __str__(self):
        s = "id:"+str(self.id)+" - " + str(self.vals)
        return s
        
    def append(self, s):
        """
        appends values of the Set s to self
        """
        
        self.vals += s.vals
        
        
class DisjointSets(object):
    def __init__(self, vals):
        """
        vals is a list of ints, no duplicates allowed initially we create a separate 
        set for each value
        """ 
        self.sets = [Set([val]) for val in vals]
        
    def __str__(self):
        s=""
        for st in self.sets:
            s += str(st)
            s += "\n"
            
        return s
    
    def find(self,val):
        """
        returns the set containing val, or None if none
        of the sets includes it
        """
        
        for st in self.sets:
            if val in st.vals:
                return st
        return None
            
    
    def union(self, val1, val2):
        """
        unites the sets containing val1 and val2 
        into the lowest-value id
        if one or both values not found does nothing
        if both values already in same set, does nothing
        """
        s1 = self.find(val1)
        s2 = self.find(val2)
        if s1 == None or s2==None or s1==s2:
            return
        
        lowest_i_set, otherset = (s1, s2) if s1.id <= s2.id else (s2, s1)
        
        lowest_i_set.append(otherset)
        
        self.sets.remove(otherset)
        
     
 
        
        
        
        
    
    