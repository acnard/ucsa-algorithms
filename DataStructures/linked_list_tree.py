# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:02:12 2022

@author: Anna
"""

class Element(object): 
    
    def __init__(self, value, parent=None):
        """ 
        value is an int, the value of this element
        parent_el is an Element, the parent of this one in the tree, or None
        if this is the root of the tree
        """
        self.value = value
        self.parent = parent
        self.rank = 0              #always a leaf when created
        
        # rank is no of nodes to bottom

        
    def __str__(self):
        """
        the string representation of an element is its value
        <child of: parent>
        """
        s = str(self.value)+" rank:"+ str(self.rank) +" <child of:" 
        if self.parent != None:
            s+= str(self.parent.value)
        else:
            s+= str(None)
        s+= ">"    
        return s
    
    def get_root(self):
        """
        returns an Element, the root of this element
        if element itself is a root, returns itself
        """            
        el = self
        while el!= None:
            if el.parent == None:
                return el
            el = el.parent
        
    def traverse_to_root(self):
        """
        returns the list of elements from self to root:
            self, el, el, el, ... root
        """
        elements = []
        el = self
        while el != None:
            elements.append(el)
            el = el.parent
            
        for element in reversed(elements):
            print(element.value)
            
        
    def set_parent(self, el):
        """
        changes the parent of this node
        
        note: rank is not altered by changing the parent because it is the 
        number of nodes from this one to the bottom
        """        
        self.parent = el
        
        
        
    
    
class LinkedTree(object):
    def __init__(self, vals):
        """
        creates a linked list representing a tree
        vals is a list of ints (can be empty), the 
        initial values in the list.
        the tail is the root of the node
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
        while el.parent_el != None:
            el = el.parent_el
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
            
        
class Forest(object):
    def __init__(self, vals):
        """
        vals is a list of ints, no duplicates allowed initially we create a  
        root element for each value
        """ 
        self.els = [Element(val) for val in vals]
        
          
        
    def __str__(self):
        s=""
        for el in self.els:
            s += str(el)
            s += "\n"
            
        return s
    
    def find_el(self,val):
        """
        if the forest contains an element = val, returns 
        that element, or None if the value not found
        """
        
        for el in self.els:
            if el.value == val:
                return el
        return None
            
    
    def union(self, val1, val2):
        """
        unites the trees containing val1 and val2 
        by hanging the shallowest of the two onto the other
        if one or both values not found does nothing
        if both values already in same tree, does nothing
        """
        el1 = self.find_el(val1)
        el2 = self.find_el(val2)
        if el1 == None or el2==None:   #value(s) not found
            return        

        ## get the roots        
        r1 = el1.get_root()
        r2 = el2.get_root()
        if r1==r2:                     #already same root
            return
        
        if r1.rank > r2.rank:   #r2 shallower, hang it on r1 (its rank won't change)
            r2.set_parent(r1)  
        elif r1.rank < r2.rank: # r1 shallower, hang it on r2 (its rank won't change)
            r1.set_parent(r2)
        else:
            r2.set_parent(r1)   # equal ranks, rank of recipient changes by one
            r1.rank+=1
            
            
    def showgroups(self):
        """
        visualize the elements that have a common root together
        """
        groups = {}  #dict maps root --> [list of elements that share it]
        for el in self.els:
            root = el.get_root()
            if root not in groups:
                groups[root]= []
            groups[root].append(el)
            
        for root in groups:
            print("group with root", root.value)
            for el in groups[root]:
                print(el)
            print("\n")
  

            
            
            
        

                