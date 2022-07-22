# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:00:01 2022

@author: Anna


For python lists, the largest costs come from growing beyond the current 
allocation size (because everything must move), or from inserting or deleting 
somewhere near the beginning (because everything after that must move).

"""
import bisect


    
class Stack(object):
    def __init__(self, q):
        """
        q is the number of queries, we will perallocate this as 
        the largest possible size of the list (in the worst-case 
        scenario that all queries are push operations).
        """
        self.stack = [None]*q  
        self.num_items = 0              # how many items currently in stack
        self.sortedstack = []
        
    def __str__(self):
        s = "stack: " + str(self.stack)
        
        s = s+ "\nsortedstack:" + str(self.sortedstack)
        
        s = s+ "\nnum_items:" + str(self.num_items)
        
        return s
        
    
    def push(self, n):
        """
        n is an int, pushes its value onto the stack
        note that append() has time-complexity O(1)
        but on our preallocated stack we must place 
        the value in the next free position, then shift the
        index one position to the right
        """
        #add n to end of stack 
        self.stack[self.num_items] = n
        
        #insert it into sorted stack
        #bisect.insort(self.sortedstack, n, 0, self.num_items)
        bisect.insort(self.sortedstack, n)
        
        #move index to the right
        self.num_items+=1
       
    
    def pop(self):
        """
        removes the last-inserted item from the stack
        pop() on the last element has time complexity O(1)
        but on our preallocated stack we just need to shift 
        our index one position to the left
        
        L.remove(X) will scan the whole list until it finds X. 
        Use del L[bisect.bisect_left(L, X)] instead 
        (provided that X is indeed in L).
        """
        # remove value from sorted stack
        val = self.stack[self.num_items-1]
        #pos = bisect.bisect_left(self.sortedstack, val, 0, self.num_items)  
        pos = bisect.bisect_left(self.sortedstack, val)  
        del self.sortedstack[pos]

        # remove value from end of stack
        self.num_items -= 1
        


        
    def max(self):
        """
        returns max value of the stack
        
        """
        return self.sortedstack[-1]
        


    
def main():

    
    q = int( input() ) #number of queries
    stk = Stack(q)
 
    for i in range(q):
        query = input().split()  # list of strings, eg ["max"] or ["push", "1"] 
        
        if query[0] == "pop":
            stk.pop()
           # print(stk)
        elif query[0] == "push":
            stk.push( int(query[1]) )
            #print(stk)
            
        elif query[0] == "max":
            print( stk.max() )
            
 


if __name__ == "__main__":
    main()