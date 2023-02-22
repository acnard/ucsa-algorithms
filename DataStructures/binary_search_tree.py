
## search tree property: 
## for any node X in the tree
##  the right subtree of X has all bigger keys than x
##  the left subtree of X has all smaller keys than x
## (keys are unique)

import math
from random import randint

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


    def __str__(self):
        s = str(self.key) 
        return s

    def getkey(self):
        return self.key


    def promote(self):
        """
        promotes self to the position occupied by its parent

        note that in practice this detaches the subtree rooted at parent
        from the tree, and attaches the subtree roted at self in its place
        """
        P = self.parent
        if P is None:
            print("cannot promote", self, ", it has no parent")
            return

        GP = P.parent       # grandparent is new parent (may be None if parent is root)
        self.parent = GP        # fix pointer from self to new parent

        if GP is not None:      # fix pointer from new parent to self
            if P == GP.lchild:
                GP.lchild = self
            elif P == GP.rchild:
                GP.rchild = self

        ## and detach P from its parent
        P.parent = None


    def detach(self):
        """
        detaches self from its parent

        in practice this detaches the subtree rooted at self from the tree
        """
        P = self.parent
        if P is None:
            print("cannot detach", self, ", it has no parent")
            return

        if self == P.lchild:  # clear pointer from parent to self
            P.lchild = None
        elif self == P.rchild:
            P.rchild = None

        self.parent = None   #clear pointer from self to parent


    def find(self, kval):
        """
        kval is an int -- we want to return a Node (in the subtree rooted at self) 
        that matches this key value or, if not present, 
        the Node under which it ought to go.

        if self doesn't match, we pass it on recursively 
        to the right or left subtree

        Note: This function does not search *upward* in the tree, only from 
        self and downward, so to search an entire tree you must call it on the 
        root of the tree
        """

        if self.key == kval:
            return self         ## I am the matching node!

        elif kval > self.key and self.rchild is not None:  ## kval is bigger, look in right subtree
            return self.rchild.find(kval)
        
        elif kval < self.key and self.lchild is not None:  ## kval is smaller, look in left subtree
            return self.lchild.find(kval)
        
        else:           ## was bigger or smaller but no corresponding subtree
            return self  ## I am the node under which kval should go!

    def left_descendant(self):
        """
        returns the leftmost leaf of the subtree rooted at self
        (ie left child of left child of left child....)

        if self has no leftchild, returns self
        """

        if self.lchild is None:  # I am the leftmost leaf!
            return self

        else:                    # go down recursively
            return self.lchild.left_descendant()


    def next(self):
        """
        returns the node in the tree with the next largest key to self.
        (looking both up and down the tree)

        Note: 
        - everything in self's left subtree will be smaller than self, so we don't look there
        - everything in its right subtree will be greater,
             so we want to return the leftmost descendant of self's right child
        - if there is no right child, go up checking parents until you find the 
            first one greater than self
        """
  
        ## if right child exists return its left descendant
        if self.rchild is not None:
            return self.rchild.left_descendant()

        ## othewise find first parent with larger key
        else:
            k = self.key
            parent = self.parent
            while (parent is not None) and (parent.getkey() < k):
                parent = parent.parent   #try the next parent up

            return parent   #this will be none if no larger key foudn

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
            return

        ## find where the key of x  fits in the tree
        kval = x.getkey()
        pos = self.root.find(kval)


        if kval == pos.getkey(): # no duplicate keys allowed
            print("cannot insert node", x, "key already present in tree")
            return

        ## x is either left or right child of pos
        x.parent = pos
        x.lchild = None
        x.rchild = None
        if kval < pos.getkey():   # make it the left child
            pos.lchild = x
        elif kval > pos.getkey():  # make it the right child
            pos.rchild = x

    def get_node(self, kval):
        """
        kval is an int, returns the node in the tree that matches that
        key value or, if not found, returns None
        """
        assert self.root is not None

        node = self.root.find(kval) # node will either have key kval or 
                                    # correspond to where kval ought to go

        if node.getkey()==kval:
            return node
        else:
            return None

    def rangesearch(self, start, stop):
        """
        start and stop are integers, returns a list of the nodes in the tree
        which have keys between start and stop, endpoints excluded
        """    
        ## search for the first element
        ## node will either have kval = start or will be 
        ## the parent under which start ought to go

        assert stop > start

        node = self.root.find(start)
        results = []

        while node is not None:
            if node.getkey() > start and node.getkey() < stop:
                results.append(node)
            node = node.parent
        
        return results

    def delete(self, xval):
        """
        xval is the key value of a node object X that we want to delete from the tree.

        We find the node X matching xval in the tree, and then 
        apply delete algorithm as follows (do checks in order):

        - if X is a leaf (no left or right child) then can just delete it.

        - elif X has *only a left child*, can just promote the left child. 
          (even if that left child has a right subtree, this will cause no conflict
           since we are promoting it to a position with no right subtree) 

        - elif X has a right child (either only a right child, or both a left and right child)
            1) find the "next" node N in that right subtree 
               (leftmost descendant of right child),
            2) swop into X the key value of N
            3) delete N (it will either be a leaf or have only a right child)
            4) if N had a right child R, promote R to the position previously
               occupid by N

        Note: since N is the successor of X, it is guaranteed to be bigger than
        anything in the left subtree of X, and also smaller than anything else in the
        right subtree of X, so the value of N can go in the position occupied by X
        
        """
        # find the node in the tree
        X = self.get_node(xval)
        if X is None:
            print("key value", xval, "not found in tree")
            return
        
        # case if X has a right child (may or may not also have left child)
        if X.rchild is not None:
            N = X.next()            # N = leftmost descendant of X's right child
            X.key = N.getkey()      # swop into X key value of N

            R = N.rchild     
            if R is not None:       # if N has a right child R, promote it
                R.promote()
            else:
                N.detach()          # otherwise just detach N

        # case if X has only a left child    
        elif X.lchild is not None:
            X.lchild.promote()     # just promote the left child

        # case if X has neither left nor right child
        else:
            X.detach()               # just detach



    def draw_tree(self):
        """
        compiles a list of the nodes in the tree top-down (starting
        from root level) and within each level left-to-right
        The 0th item is  None, then at index=1 is the root,
        at index=2 and 3 are its left and right children
        
        And generally the children of the node at 
        index=k are at 2k and 2k+1

        Insert None in any unoccupied positions

        Then uses this to print the tree
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

        print("kvals: ", kvals)

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




def test(n=8):
    """
    n is an int, the number of nodes you want to have in the tree
    """
    nodes = [Node(randint(1, 99)) for _ in range(n)]

    print("nodes: ")
    for node in nodes:
        print(node, end=", ")
    print()

    ## make a tree
    tr = SearchTree()


    ## insert nodes into the tree
    for node in nodes:
        tr.insert(node)
  
    tr.draw_tree()

    print("now test the next function")
    for node in nodes:
        print("next node to", node, "is", node.next())


    print("now test rangesearch")
    start = randint(1,99)
    stop = randint(start,99)

    print("nodes in range between", start, "and", stop)
    result = tr.rangesearch(start, stop)

    for node in result:
        print(node)

    return tr  ##return the tere