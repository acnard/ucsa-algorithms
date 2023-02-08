
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

    def find(self, kval):
        """
        kval is an int -- we want to return a Node in the tree that matches this key value, or None
        if self doesn't match, we pass it on recursively to the right or left subtree
        """
        if self.key == kval:
            return self         ## I am the matching node!

        elif kval > self.key and self.rchild is not None:  ## kval is bigger, look in right subtree
            return self.rchild.find(kval)
        
        elif kval < self.key and self.lchild is not None:  ## kval is smaller, look in left subtree
            return self.lchild.find(kval)
        
        else:           ## was bigger or smaller but no corresponding subtree
            return None

    def insert(self, x):
        """
        x is a node object
        """

    



class SearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, x):
        """
        x is a Node object, to be inserted into the tree
        """
        if self.root == None:
            self.root = x 

        elif x.getkey() > self.root.getkey():
            pass
    def find(self, kval):
        """
        kval is an int, returns the Node in the tree with matching val, if found,
        otherwise returns None
        """


