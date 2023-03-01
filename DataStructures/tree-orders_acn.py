# python3
class Tree(object):
    def __init__(self, keys, lchilds, rchilds):
        """
        keys, lchilds and rchils are lists of ints where
        - keys[i] is the key value of the ith node (root i=0)
        - lchilds[i] is the left child of the ith node
        - rchilds[i] is the right child of the ith node

        """
        self.keys = keys
        self.lchilds = lchilds
        self.rchilds = rchilds

    def __str__(self):
        s = "Tree: \n"
        s = s + "keys: " + str(self.keys) +"\n"
        s = s + "lchilds: " + str(self.lchilds) + "\n"
        s = s + "rchilds: " + str(self.rchilds) + "\n"
        return s

    def get_root(self):
        return self.keys[0]

    def get_lchild(self, key):
        """
        key is an int, the key of a node in the tree
        returns the key value of left child of that node
        or None if node has no left child
        """
        assert key in self.keys

        i = self.keys.index(key)
        i_left = self.lchilds[i]

        if i_left == -1:
            return None
        else:
            return self.keys[i_left]

    def get_rchild(self, key):
        """
        key is an int, the key of a node in the tree
        returns the key value of right child of that node
        or None if node has no right child
        """
        assert key in self.keys

        i = self.keys.index(key)
        i_right = self.rchilds[i]

        if i_right == -1:
            return None
        else:
            return self.keys[i_right]

    def get_parent(self, key):
        """
        key is an int, the key of a node in the tree
        returns the key value of its parent, or None
        if it's the root
        """
        assert key in self.keys

        ichild = self.keys.index(key)

        if ichild in self.lchilds:
            iparent = self.lchilds.index(ichild)
        elif ichild in self.rchilds:
            iparent = self.rchilds.index(ichild)
        else:
            iparent = None   #only root has no parent

        if iparent is not None:
            return self.keys[iparent]
        else:
            return None


    def in_order(self, k = None):
        """
        does an in-order traversal of this tree, starting from the node with key value k
        """

        ## first recursive call, start from root
        if k == None:
            k = self.get_root()

 
        ## see if k has a left child
        kleft = self.get_lchild(k)
        if kleft is not None:
            self.in_order(kleft)    ## RECURSIVE call on LEFT subtree of k

        print(k)   ## Print k's own value

        ## see if k has right child
        kright = self.get_rchild(k)  ## RECURSIVE call or RIGHT subtree of k
        if kright is not None:
            self.in_order(kright)



def test():
    keys = [4, 2, 5, 1, 3]
    lchilds = [1, 3, -1, -1, -1]
    rchilds = [2, 4, -1, -1, -1]
    tr = Tree(keys, lchilds, rchilds)
    print(tr)
    return tr


def main():
    """
    the first line contains the number of vertices n
    the vertices are numbered with i=0 to i=n-1, where 0 is root

    the next n lines contain the info about the vertices i=0, 1, .. n-1 in order.
    Each line contains three integers, keyi, lefti, righti
      ie the key of the ith vertex and the index of its left and right child (-1 if no child)

    """
    n = int(input())
    key = []
    lchild = []
    rchild = []

    for i in range(n):
        [k, l, r] = [int(s) for s in input().split()] 
        key.append(k)
        lchild.append(l)
        rchild.append(r)

    print("keys:", key)
    print("lchilds", lchild)
    print("rchilds", rchild)

    tr = Tree(key, lchild, rchild)
    print(tr)



