# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 16:31:51 2022

@author: Anna
"""

class Id(object):
    def __init__(self, set_id):
        """ 
        set_id is an int, a unique identifier for a set
        """
        self.id = set_id
        
    def __str__(self):
         return str(self.id)
     
 

    

class DisjointSets(object):
    def __init__(self, n):
        """
        n is an int, the number of elements we want to have.
        Initially we create 'n' sets with id from  0 --- > n-1,
        each containing a single element (with values from 0 --- > n-1)
        
         - the value 0 has set id = 0, 
         - the value 1 has set id = 1,
         - the value n-1 has set id = n-1
         
         so that: self.ids[value]
         lets you look up the set identifier of any value

        """
        self.ids = [Id(i) for i in range(n)]  # set identifiers 0--> n-1
                                 
        

    def __str__(self):
        s = ""
        for i in range(len(self.ids)):
            s+="val:"+str(i)+" set:"+str(self.ids[i].id)+", "
            
        return s

    def get_id(self, val):
        """ 
         returns the Id object for val
        """
        if val >= 0 and val < len(self.ids):
            return self.ids[val]
        else:
            return None        
        
    def find(self, val):
        """returns the integer set_id for val
        """
        
        if val >= 0 and val < len(self.ids):
            return self.ids[val].id
        else:
            return None
        
        
    def union(self, val1, val2):
        """
        unites the sets containing val1 and val2 
        into the lowest-value id
        if one or both values not found does nothing
        if both values already in same set, does nothing
        """
        id1 = self.get_id(val1)
        id2 = self.get_id(val2)
        
        if id1 == None or id2==None or id1.id==id2.id:
            return        
        
        highid, lowid = (id1, id2) if id1.id>=id2.id else (id2, id1)
            
        highid.id = lowid.id
        
        
        