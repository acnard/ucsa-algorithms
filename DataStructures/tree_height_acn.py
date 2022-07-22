# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:41:02 2022

@author: Anna
"""
import sys

class Tree(object):
    def __init__(self, tree):
        """
        nodes is a list of ints, describing the tree
        for each node i, tree[i] is the index of the node's parent, 
        or -1 if that node is the root
        """
        self.tree = tuple(tree)
        
        self.n = len(tree)
        
        self.depths = [None]*self.n  # memo for storing depth of ith node
        
        self.max = 0 #max depth of tree found so far
        
        
    def __str__(self):
        s = "tree:\n" + str(self.tree) +"\n"
        
        s = s + "\ndepths:\n" + str(self.depths)
        
        return s
        
        
    def get_depth(self, i):
        """
        i is the index of a node in self.tree
        returns the depth of the node, = the number of vertices on the path
        to node i (so that the root has depth 1, the next level has depth 2, etc)
        
        also memoizes the value in self.depths
        """

        ## check memo
        if self.depths[i] != None:
            return self.depths[i]

        ## get ith node's parent and find parent's depth
        parent = self.tree[i]    
        if parent == -1 :                      # base case, this node is root
            depth = 1
        else:
            depth = 1 + self.get_depth(parent) # recursive call
            
        ## memoize and return the result    
        self.depths[i] = depth
        if depth > self.max:
            self.max = depth
        return depth                 
        
        
    def max_depth(self):
        """
        traverse the entire tree and return the max depth found
        """
        for i in range( len(self.tree) ):
            if self.depths[i] == None:
                self.get_depth(i) 

                    
        return self.max    

 
def test():
    
    test_12 = "3 57 29 54 29 94 88 57 40 16 72 16 80 63 89 4 77 77 16 65 72 14 94 82 80 49 69 54 1 99 50 18 52 36 49 50 80 42 89 31 4 52 52 77 88 42 97 73 73 82 88 37 69 63 40 99 36 76 1 37 28 57 82 93 54 63 76 14 18 -1 76 42 14 72 97 28 37 65 99 29 97 3 3 93 65 93 89 40 31 36 73 18 4 49 28 69 1 50 31 94"
    a_12 = 34
    
    test_08 = "66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 -1 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66"
    a_08 = 2
    
    tree = [int(s) for s in test_08.split() ]
    tr = Tree(tree)
    
    print(tr)
    print( tr.max_depth() )
    print(tr)


        
        

def main():
    """
    The first line contains an integer 𝑛, the number of nodes in the tree
    The second line contains 𝑛 integer numbers from −1 to 𝑛 − 1 — parents of nodes.
    If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
    otherwise it’s 0-based index of the parent of 𝑖-th node. 
    It is guaranteed that there is exactly one root. It is guaranteed that 
    the input represents a tree.

    """
    
    n = int( input( )) # not used

    tree = [int(s) for s in input().split() ]
    
    tr = Tree(tree)
        
    print( tr.max_depth() )
    #print(tree)
    


    
    


if __name__ == "__main__":
    
    sys.setrecursionlimit(10**7)  # max depth of recursion

    main()