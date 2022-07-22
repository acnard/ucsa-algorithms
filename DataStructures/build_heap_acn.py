# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:35:43 2022

@author: Anna
"""
import math
import random



class BinaryTree(object): 
    def __init__(self, nodes, Max=True):
        """
        nodes is a list of ints, representing a complete binary tree 
        i.e all levels completely filled, except possibly the lowest one, 
        which must still be filled from left to right.
        
        the list contains the nodes top-down (root first, then level 1, etc.) 
        and within each level, listed left to right.
        
                
        if Max = True the parents are bigger than their children, otherwise the
        opposite
        
        when storing the nodes, 
        index=0 empty is left empty and the root node starts at index=1. 
        So that the children of the node at index=k are at 2k and 2k+1.
        Also, the parent of the node at index j will be at j//2. 
        """
 
        self.nodes = [None]+nodes    # to leave index 0 empty
        self.Max = Max               #set whether maxtree or mintree
        self.swops = []              #for storing the swops
        
    def countnodes(self):
        """
        returns number of nodes in the tree
        """
        
        return len(self.nodes)-1  # pos 0 not used
        
    
    def countlevels(self):
        """
        returns the number of levels in the tree
        """
        num_nodes = self.countnodes()
        
        ## throw away the decimal then add one to get right result, 
        ## eg 7 nodes is a full three levels
        ## 8 nodes is four levels (the 8th node goes to level 4)
        if num_nodes > 0:
            return int( math.log2(num_nodes) ) + 1
        else:
            return 0
        
    def __str__(self):
         s = "binary tree made from:\n" + str(self.nodes) + "\n"
         s+= "number of nodes = " + str(self.countnodes()) + "\n"
         s+= "number of levels =" + str(self.countlevels()) + "\n"
         s+= "type ="
         if self.Max==True:
             s+=" maxtree"
         else:
             s+=" mintree"
         s+= "\ntree representation:\n"
         
         s+= self.drawtree()
                 
         return s
         
    def build_heap(self):
        """
       changes self.nodes in-place via swaps to make it into a heap.
        """
        
        # the last node in tree is at i = countnodes()
        # and its parent is at i//2
        # so last node that is a parent is at countnodes()//2
        
        # loop backward from last parent towards top of tree
        
        self.swops = []  # reset the swops storage
        
        for i in range(self.countnodes()//2, 0, -1):
            self.sift_down(i)
            
        # print swops info
        # print(len(self.swops))
        
        # for i1,i2 in self.swops:
        #     print(i1-1, i2-1)  #subtract 1 to get real 0 based index
            
    def heap_sort(self):
        """
        to do a heap sort, first turn self.nodes into a heap in-place
        then swop the first node with the last, reduce the array size by one, 
        and sift down the first node
        """
        # last_i = self.countnodes()
        
        # while( last_i) > 1 )
        # for i in range( 1, len(self.nodes) ) :
        pass
        
            

    def sift_up(self, i):
        """ 
        checks child node i versus its parent
        if the ith node is problematic (higher value than its parent if Max=True,
        or lower value than its parent for Max =False), moves it up via swaps until
        the heap property is preserved.
        """
        if i == 1:          #root node has no parent, do nothing
            return

        valchild = self.nodes[i]
        iparent= i//2
        
        valparent = self.nodes[iparent]
        
        if (valchild > valparent and self.Max==True) or (valchild < valparent and self.Max==False):
            
            ## swop the values
            self.swop(i, iparent)
            self.sift_up(iparent)
            


    def swop(self, i1, i2):
        """
        swops the two nodes at i1 and i2
        indexes are assumed to be in range
        
        """
        assert i1<len(self.nodes)
        assert i2<len(self.nodes)
        
        val1 = self.nodes[i1]
        val2 = self.nodes[i2]
        
#        print("swopping", val1, "and", val2)
        
        self.nodes[i1] = val2
        self.nodes[i2] = val1
        
        self.swops.append( (i1,i2) )
        

    def sift_down(self, i):
        """
        checks node i versus its children
        if the ith node is problematic (has a child that is bigger than it, if Max=True,
        or has a child that is smaller than it, for Max =False), moves it down via swaps until
        the heap property is preserved.
        
        Always swop with the most advantageous child: for Max = True swap with the biggest child
        """

        bestindex = i   # initially assume parent is better than its children
        
        if 2*i < len(self.nodes):  # check left child, if exists
            if (self.Max==True and self.nodes[2*i] > self.nodes[bestindex]) or (self.Max==False and self.nodes[2*i] < self.nodes[bestindex]):
                bestindex = 2*i   # left child is better than parent
                
        
        if 2*i +1 < len(self.nodes):  # check right child, if exists
            if (self.Max==True and self.nodes[2*i+1] > self.nodes[bestindex]) or (self.Max==False and self.nodes[2*i+1] < self.nodes[bestindex]):
                bestindex = 2*i+1  # right child is better than previous best node
                
        if bestindex != i:
            self.swop(i, bestindex)
            self.sift_down(bestindex)
            

    def insert(self, p):
        """
        inserts a node with priority p into the tree, does this by first inserting
        it into the last available position (to keep the complete shape of the tree) and
        then sifting it up
        """
        
        self.nodes.append(p)        #append node to end
        
        print("insert", p)
        
        i_new_node = len(self.nodes) - 1
        
        self.sift_up(i_new_node)  # and sift it up
        print(self.drawtree())
        
        

    def sift_down_alt(self, i, Max=True):
        """ 
        checks node i versus its children
        if the ith node is problematic (has a child that is bigger than it, if Max=True,
        or has a child that is smaller than it, for Max =False), moves it down via swaps until
        the heap property is preserved.
        
        Always swop with the most advantageous child: for Max = True swap with the biggest child
        """
      
    
        i_children = [2*i, 2*i+1]
        i_valid_children = [j for j in i_children if j<=self.num_nodes]  #filter out-of-range ones
        
        if Max == True:
            i_better_children = [j for j in i_valid_children if self.nodes[j] > self.nodes[i] ]
        else:
            i_better_children = [j for j in i_valid_children if self.nodes[j] < self.nodes[i]  ]   
            
        # print("better children for", self.nodes[i], "are:")
        # for index in i_better_children:
        #     print(self.nodes[index], end=" ")

        if len(i_better_children) == 0:      #no better children, nothing to do
            return
        
        if len(i_better_children) ==1:                   #only one better child
            best_child_i = i_better_children[0]
        else:                                   # two better children, sort ascending by val
            i_better_children = sorted(i_better_children, key=lambda x: self.nodes[x])
            
            # print("\nSORTED better children for", self.nodes[i], "are:")
            # for index in i_better_children:
            #     print(self.nodes[index], end=" ")
            
            if Max == True:
                best_child_i = i_better_children[1]  # best child is biggest
            else:
                best_child_i =i_better_children[0]
                
        # print("-->best child is", self.nodes[best_child_i])    
        self.swop(i,best_child_i)
       
        ## repeat the sift from the new position
        self.sift_down_alt(best_child_i, Max)
                    

    def drawtree(self):
        """
        draws the binary tree with proper spacing
        
        """
        
        # num items in lowest level, if full is: bottom_items = 2**(num_levels-1) 
        # we allow 2 spaces per item, plus one space before and after, so 
        # bottom_width = bottom_items * 4 = bottom_items * 2**2
        #              = 2**(num_levels-1) * 2**2 
        #              = 2**(num_levels+1)
        #
        # bottom_width = 2**(num_levels +1)
        
        # now on any given level we have numitems = 2**level
        # where the topmost level is 0. So, one item at root, two at level 1, etc.
        # And the width available for each item = bottom_width/numitems
        # so that:
        #     itemwidth= bottom_width/numitems = 2**(num_levels+1) / 2**level
        #                                       = 2**(num_levels+ 1 - level)

        s = ""   #string for the entire binary tree

        num_levels = self.countlevels()              #get number of levels in tree
        
        level=0                                      #start at root level
        itemwidth = 2**(num_levels+ 1 - level)
        level_s = ""
        for i in range(len(self.nodes)):
            if i==0:
                continue
            item_s = str(" "+ str(self.nodes[i]) +" ") # item with spaces before and after
            item_s = item_s.center(itemwidth)
            level_s+= item_s
            if (math.log2(i+1))%1 == 0:    #was last node of a level
                s+= level_s
                s+="\n\n"
                level_s = ""
                level+=1
                itemwidth = 2**(num_levels+ 1 - level)
        s+= level_s #in case final level not complete        
        
        return s+"\n"
    
    
   
def test(n, Max=True):
    
    """ generate a list of n random ints
        then construct a heap from it
    """
    
    MAX = 99  # ints in list will be between 1 and this
    vals = list( [random.randint(1, MAX) for i in range(n)]  )
    
    # create binary tree from vals
    bt = BinaryTree(vals, Max)
    print("starting tree: \n")
    print(bt.drawtree())
    
    bt.build_heap()
    print("final tree: \n")
    print(bt.drawtree())
    
    # print("swops\n")
    # print(bt.swops)
    

    
def test_1():
    nodes = [9, 15, 24, 18, 86, 65, 35, 53, 34, 62, 52, 25, 38, 22, 13, 50]
    bt = BinaryTree(nodes)
   
    print(bt)
    #sift down the root node
    bt.sift_down (1)
    
    print("\n finished tree")
    print(bt.drawtree())
    


def main():
    """
    The first line contains an integer 𝑛, 
    the second line contains 𝑛 integers 𝑎1, . . . , 𝑎𝑛 separated
    by spaces
    """
    n = int( input( )) # not used

    vals = [int(s) for s in input().split() ]
    #print(nums)
    
    bt = BinaryTree(vals, False)  #use a mintree
    bt.build_heap()
    
    
    
    


if __name__ == "__main__":
    pass
   # main()    
   

