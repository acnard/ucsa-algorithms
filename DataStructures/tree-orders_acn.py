# python3
import sys
import threading


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


    def order(self, type="in", i=0):
        """
        does an order traversal of this tree, starting from the node 
        with index i in keys[] (will start from root if not specified)

        type is a string, specifies whether the traversal is 
        "in", "pre" or "post" order
        """
        assert type=="in" or type=="pre" or type=="post"

        k = self.keys[i]  # key value k of node i

        if type == "pre":
            print(k, end=" ")  # print k's own value here for PRE-ORDER

        ## see if node i has a left child
        ileft = self.lchilds[i]
        if ileft != -1:
            self.order(type, ileft)    ## RECURSIVE call on LEFT subtree of k

        if type == "in":
            print(k, end=" ")  # print k's own value her for IN-ORDER

        ## see if node i has right child
        iright = self.rchilds[i]  ## RECURSIVE call or RIGHT subtree of k
        if iright != -1:
            self.order(type, iright)

        if type == "post":
            print(k, end=" ")  # print k's own value her for POST-ORDER


def test():
    # keys = [4, 2, 5, 1, 3]
    # lchilds = [1, 3, -1, -1, -1]
    # rchilds = [2, 4, -1, -1, -1]

    keys = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    lchilds = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
    rchilds = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]

    tr = Tree(keys, lchilds, rchilds)
    print(tr)

    tr.order("in")
    print()
    tr.order("pre")
    print()
    tr.order("post")
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

    # print("keys:", key)
    # print("lchilds", lchild)
    # print("rchilds", rchild)

    tr = Tree(key, lchild, rchild)
    # print(tr)

    tr.order("in")
    print()
    tr.order("pre")
    print()
    tr.order("post")

# if __name__ == '__main__':

#     main()

## recursion limit in python is 1000 so we must increase it
sys.setrecursionlimit(10**6) # max depth of recursion

## we also change the stack size
threading.stack_size(2**27)  # new thread will get stack of such size

## create a new thread for main()
mythread = threading.Thread(target=main)
mythread.start()
mythread.join()     #wait for it to finish   
