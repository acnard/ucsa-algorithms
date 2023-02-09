
## search tree property: 
## for any node X in the tree
##  the right subtree of X has all bigger keys than x
##  the left subtree of X has all smaller keys than x
## (keys are unique)

import math

class Node(object):
    def __init__(self, key):
        """
        key is an int, the value of this node
        parent, lchild and rchild are other Node objects
        """
        self.key = key

        ## initially created node is always
        ## unattached to any others
        self.parent=None
        self.lchild=None
        self.rchild=None

        ## horizontal position of the node within 
        ## its level in a Tree
        ## (also counting unoccupied positions) 
        ## 0 is the leftmost node, 1 the next one along, etc. 
        self.hpos =None 

    def __str__(self):
        s = str(self.key) 
        return s

    def getkey(self):
        return self.key

    def isleaf(self):
        """
           returns True if this node is a leaf 
           (has no children), otherwise False
        """
        if self.lchild is None and self.rchild is None:
            return True
        else:
            return False

    def find(self, kval):
        """
        kval is an int -- we want to return a Node in the tree that matches this key value or, if not present, the Node under which it ought to go.

        if self doesn't match, we pass it on recursively to the right or left subtree
        """

        if self.key == kval:
            return self         ## I am the matching node!

        elif kval > self.key and self.rchild is not None:  ## kval is bigger, look in right subtree
            return self.rchild.find(kval)
        
        elif kval < self.key and self.lchild is not None:  ## kval is smaller, look in left subtree
            return self.lchild.find(kval)
        
        else:           ## was bigger or smaller but no corresponding subtree
            return self  ## I am the node under which kval should go!

    def count_levels(self):
        """
        returns the number of levels of the subtree rooted at
        self, where self counts as 1 level, then add to this 
        0 if self is a leaf, otherwise add to it the levels
        of its left or right subtree, whichever is larger
        """
        left_levels = 0
        right_levels = 0

        if self.lchild is not None:
            left_levels = self.lchild.count_levels()
        if self.rchild is not None:
            right_levels = self.rchild.count_levels()

        return 1 + max(left_levels, right_levels)

    def get_level(self):
        """
        returns the level at which self is located within its tree,
        if it has no parent (ie is the root) the level is 1,
        if its parent is the root its level is 2, and so on.
        """

        if self.parent == None:
            return 1

        else:
            return 1 + self.parent.get_level()




class SearchTree(object):
    def __init__(self):
        self.root = None


    def __str__(self):
        s = "Tree:\n"
        s = s+ str(self.root)

        return s

    def insert(self, x):
        """
        x is a Node object, to be inserted into the tree
        """
        if self.root == None:  #make x the root of this tree
            self.root = x 
            x.parent = None
            x.lchild = None
            x.rchild = None
            x.hpos = 0    ## is the 1st (and only) node in its level 
            return

        ## find where the key of x  fits in the tree
        kval = x.getkey()
        pos = self.root.find(kval)


        if kval == pos.getkey(): # no duplicate keys allowed
            print("cannot insert node", x, "key already present in tree")
            return

        ## x is either left or right child of pos
        ## note: position of left child is 2*parent position
        ##       position of right child is 2*parent position + 1
        x.parent = pos
        x.lchild = None
        x.rchild = None
        if kval < pos.getkey():   # make it the left child
            pos.lchild = x
            x.hpos = 2*pos.hpos
        elif kval > pos.getkey():  # make it the right child
            pos.rchild = x
            x.hpos = 2*pos.hpos + 1

    def get_nodes(self):
        """
        returns a list of the nodes in the tree top-down (starting
        from root level) and within each level left-to-right
        The 0th item is  None, then at index=1 is the root,
        at index=2 and 3 are its left and right children
        
        And generally the children of the node at 
        index=k are at 2k and 2k+1

        Insert None in any unoccupied positions
        """
        assert self.root is not None


        # count number of levels in the tree
        # only root is one level, root + children is two levels
        num_levels= self.root.count_levels()

        print("there are", num_levels, "levels in the tree")

        ## total number of nodes in the binary tree 
        ## if it were complete would be 2^num_levels - 1
        ## eg 2 levels -> 3 nodes
        ##    3 levels -> 7 nodes, etc.
        ## 
        ## but we also want the index=0 position to be unused, so
        ## in total need 2**num_levels slots in the array
        nodes = [None]*(2**num_levels)

        print("the tree can fit", 2**num_levels-1, "nodes if filled")

        nodes[1] = self.root  # put root in index=1 position

        # now traverse the array, putting in the children of each
        # node encountered, or None if nonexistent
        for i in range( len(nodes)//2 ):
            if nodes[i] is not None: 
                #we can do this because children set to None if nonexistent
                    nodes[2*i] = nodes[i].lchild
                    nodes[2*i +1] =nodes[i].rchild                    

        ## for printing
        kvals = []
        for node in nodes:
            if node is None:
                kvals.append("-")
            else:
                kvals.append( str(node.getkey()) )

        ## split kvals into row strings
        rows = []
        s = ""
        for i in range(1, len(kvals)):
            s = s + " " + kvals[i] + " "
            if (math.log2(i+1))%1 == 0:  #is last node of a level
                s = s + "\n"
                rows.append(s)
                s = ""

        ## get width of longest (bottom) string
        bottom_width = len(rows[-1])

        ##and center all other strings upon it
        ## no need to center last string
        for i in range( len(rows)-1 ):
            rows[i] = rows[i].center(bottom_width)


        for row in rows:
            print(row)
        return nodes




    def drawtree(self):
        """
        similar (but not the same) to method used in build_heap.py
        draws the tree with proper spacing

        we assume that placing the root 20 characters along from
        left margin is sufficient for tree to fit

        """
        assert self.root is not None

 


        # count number of levels in the tree
        # this gives the rows needed to draw the tree
        num_levels= self.root.count_levels()

        # num items in bottom level, if full, is 2**(num_levels-1)
        # eg if only 1 level in tree, bottom row has 2^0= 1 items
        # if 2 levels in tree, bottom row has 2 items, etc.
        bottom_items = 2**(num_levels-1) 

        # for each item we allow 2 spaces plus
        # one space before and after, for a total of 4 spaces
        bottom_width = 4*bottom_items 

        






def test():

    ## make some free nodes
    n1 = Node(3)
    n2 = Node(12)
    n3 = Node(4)
    n4 = Node(7)



    ## make a tree
    tr = SearchTree()


    ## insert nodes
    tr.insert(n1)
    tr.insert(n2)
    tr.insert(n3)
    tr.insert(n4)
    tr.insert(Node(2))
    tr.insert(Node(5))
  
    tr.get_nodes()

