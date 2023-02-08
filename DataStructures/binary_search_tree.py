
## search tree property: 
## for any node X in the tree
##  the right subtree of X has all bigger keys than x
##  the left subtree of X has all smaller keys than x
## (keys are unique)

class Node(object):
    def __init__(self, key, parent=None, lchild=None, rchild=None):
        """
        key is an int, the value of this node
        parent, lchild and rchild are other Node objects
        """
        self.key = key
        self.parent=parent
        self.lchild=lchild
        self.rchild=rchild

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
        of its left or right subtree, whicever is larger
        """
        left_levels = 0
        right_levels = 0

        if self.lchild is not None:
            left_levels = 1 + self.lchild.count_levels()
        if self.rchild is not None:
            right_levels = 1 + self.rchild.count_levels()

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


    def drawtree(self):
        """
        similar (but not the same) to method used in build_heap.py
        draws the tree with proper spacing

        """
        assert self.root is not None

        # count number of levels in the tree
        # this gives the rows needed to draw the tree
        num_levels= self.root.count_levels()

        # num items in bottom level, if full, is 2**(num_levels-1)
        # eg if only 1 level in tree, bottom row has 2^0= 1 items
        # if 2 levels in tree, bottom row has 2 items, etc.
        bottom_items = 2**(num_levels-1) 

        # for each item we allow 4 spaces (to cover "None") plus
        # one space before and after, for a total of 6 spaces
        bottom_width = 6*bottom_items 

        






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
    print(tr.root)
 
    print (n1.get_level())
    print (n2.get_level())
    print (n3.get_level())

