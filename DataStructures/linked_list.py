# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:02:12 2022

@author: Anna
"""

class Element(object): 
    
    def __init__(self, value, next_el=None):
        """ 
        value is an int, the value of this element
        next_el is an Element, the next one in the linked list, or None
        if this is the tail of the list
        """
        self.value = value
        self.next_el = next_el
        
    def __str__(self):
        """
        the string representation of an element is its value
        --> next value
        """
        s = str(self.value)+"-->"
        if self.next_el != None: 
            s +=str(self.next_el.value)
        return s
    
    def setnext(self, el):
        """
        changes the next-element pointer
        """
        self.next_el = el
        
    
    
class LinkedList(object):
    def __init__(self, vals=[]):
        """
        creates a linked list
        vals is a list of ints (can be empty), the 
        initial values in the list
        """
        self.head = None
        self.tail = None
        
        for val in vals:
            self.insert(val)
        
    def __str__(self):
        """
        prints out the values of the list, from head to tail
        """
        if self.head == None:
            return "list empty"
        
        el = self.head
        s = str(el)+"\n"
        while el.next_el != None:
            el = el.next_el
            s += str(el)+"\n"
            
        return s
            
        
        
    def insert(self, val):
        """
        inserts an element with value val 
        places it at the tail of the list
        """
        el = Element(val, None)  # create element to insert

        if self.head == None :   # list was empty: new element is also head
            self.head = el
        else :                     # list contains at least one element:
            self.tail.setnext(el)    #old tail now points to new tail
        
        self.tail = el           # new element  becomes new tail
                              
        
    def append(self, ll):
        """
        appends the LinkedList ll to self. Does this by making the tail of self
        point to the head of ll, and setting the tail of ll as the new tail of self.
        """
        if ll.head == None:
            return           #do nothing if list to append is empty
        
        if self.head == None:           # if self empty copy the head
            self.head = ll.head
        else:
            self.tail.setnext(ll.head)  #point tail of self to head of new list
        
        self.tail = ll.tail    #update tail of combined list
        
    def contains(self, val):
        """
        val is an int
        returns True if the linked list contains val, otherwise False
        """

        el = self.head
        while el != None:
            if el.value == val:
                return True
            el = el.next_el
        return False
            
        
class DisjointSets(object):
    def __init__(self, vals):
        """
        vals is a list of ints, no duplicates allowed initially we create a separate 
        set (implemented as linked list) for each value
        """ 
        self.sets = [LinkedList([val]) for val in vals]
        
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
            if st.contains(val):
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
        
        # lowest_i_set, otherset = (s1, s2) if s1.id <= s2.id else (s2, s1)
        
        # lowest_i_set.append(otherset)
        s1.append(s2)   
        self.sets.remove(s2)

                