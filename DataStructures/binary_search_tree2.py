
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
        """
        self.key = key

        ## initially created node is always
        ## unattached to any others
        self.parent=None
        self.lchild=None
        self.rchild=None

        ## stores reference to tree if node is the root of a tree
        self.is_root_of = None

        ## height of unattached node is 1
        self.height = 1


    def __str__(self):
        s = str(self.key) 
        return s

    def getkey(self):
        return self.key


    def promote(self):
        """
        promotes self to the position occupied by its parent
        (if parent was the root, this means self becomes root)

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
            GP.adjust_height    # adjust height of new parent

        # if  P was root of a tree, transfer it to self
        tree = P.is_root_of
        if tree is not None:
            tree.set_root(self)
            P.is_root_of = None


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

        P.adjust_height()  # adjust height of parent and ancestors



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

    def rotate_right(self):
        """
        rotates the subtree rooted at self to the right:
        (to do this, self must have a left child)

        - promote self's left child L so that it becomes the child
          of self's parent P 

        - now self is detached from the tree and has no left child: 
          make self the right child of L,
          and make L's previous right child R the left child of self.
        """

        L = self.lchild

        # quit if no left child
        if L is None:
            print("cannot rotate right:", self, "has no left child")
            return

        # promote left child of self (if self was root, now L becomes root)
        L.promote()

        # now self is detached from tree and has no left child:
        # ---> move L's right child to be left child of self
        R = L.rchild
        if R is not None:  
            self.lchild = R   # fix pointer from self to child
            R.parent = self   # fix pointer from child to self

        # ----> and make self the right child of L
        L.rchild = self
        self.parent = L

    def adjust_height(self):
        """
        updates the height of self based on that of its children
        """

        ## figure out new height
        lheight = 0 if self.lchild is None else self.lchild.height
        rheight = 0 if self.rchild is None else self.rchild.height
        newheight = max(lheight, rheight) + 1

        ## BASE CASE height hasn't changed
        if newheight == self.height:
            return
        
        ## height has changed, update it in self
        self.height = newheight

        ## propagate change upwards
        if self.parent is not None:
            self.parent.adjust_height()  # RECURSIVE CALL




class SearchTree(object):
    def __init__(self, kvals=[]):
        """
        kvals is a list of ints, the key values we want to insert into
        the tree (in the provided order)
        """
        if len(kvals) == 0:                 # no key values provided
            self.root = Node(randint(1,99)) # make a random root
        else:
            self.root = Node(kvals[0])  # use first key value for root

        # tell root node it's the root of this tree
        self.root.is_root_of = self

        if len(kvals) > 1 :   
            for kval in kvals[1:]:  #insert any remaining keyvals
                self.insert(kval)



    def __str__(self):
        s = "Tree:\n"
        s = s+ str(self.root)

        return s

    def set_root(self, n):
        """
        n is a node object, sets it as the root of this tree

        note that the root essentially defines the entire tree
        """
        self.root = n   # tell this tree that n is the new root
        n.is_root_of = self  # tell n it's now root of this tree

    def insert(self, xval):
        """
        xval is an int, the key value we want to insert into the tree
        """

        ## find where xval  fits in the tree
        pos = self.root.find(xval)

        # no duplicate keys allowed
        if xval == pos.getkey(): 
            print("cannot insert key", xval, ", it is already present in tree")
            return

        # create node x with key xval
        x = Node(xval)  

        ## x is either left or right child of pos
        x.parent = pos
        if xval < pos.getkey():   # make it the left child
            pos.lchild = x
        elif xval > pos.getkey():  # make it the right child
            pos.rchild = x

        ## adjust height of pos and of its ancestors
        pos.adjust_height()

    def get_node(self, kval):
        """
        kval is an int, returns the node in the tree that matches that
        key value or, if not found, returns None
        """

        node = self.root.find(kval) # node will either have key kval or 
                                    # correspond to where kval ought to go

        if node.getkey()==kval:
            return node
        else:
            return None
        
    def split(self, kval):
        """
        splits the tree self at the node 
        """

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
    kvals = [randint(1, 99) for _ in range(n)]


    print("kvals: ", kvals)


    ## make a tree and draw it
    tr = SearchTree(kvals)
    tr.draw_tree()

    print("now test the next function")
    for kval in kvals:
        node = tr.get_node(kval)
        print("next node to", node, "is", node.next())


    print("now test rangesearch")
    start = randint(1,99)
    stop = randint(start,99)

    print("nodes in range between", start, "and", stop)
    result = tr.rangesearch(start, stop)

    for node in result:
        print(node)

    print("now test heights")
    for kval in kvals:
        node = tr.get_node(kval)
        print("height of node", node, "is", node.height)

    return tr  ##return the tere