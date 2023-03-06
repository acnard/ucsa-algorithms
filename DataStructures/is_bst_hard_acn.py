"""
based on tree_orders() structure, now
have to test whether the provided tree is a binary search tree
"""
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
        self.minmax = [None]*len(self.keys)

    def __str__(self):
        s = "Tree: \n"
        s = s + "keys: " + str(self.keys) +"\n"
        s = s + "lchilds: " + str(self.lchilds) + "\n"
        s = s + "rchilds: " + str(self.rchilds) + "\n"
        s = s + "minmax: " + str(self.minmax) + "\n"
        return s


    def get_root(self):
        return self.keys[0]


    def get_minmax(self, i=0):
        """
        VERSION MODIFIED TO ALLOW DUPLICATE KEYS, BUT MUST ALWAYS BE IN THE RIGHT SUBTREE

        if the subtree at i meets the bst property, returns a tuple (min, max) of the
        biggest and smallest values in that subtree, otherwise returs False

        use the following memoization:
        - if the subtree rooted at i meets the bst property, in the list self.minmax[i] 
        we store a tuple (min,max) of the biggest and smallest key values to be found in the 
        subtree rooted at node i, inclusive of node i itself
        - if the subtree rooted at i does NOT meet bst property, we memoize False

        NB for bst property we want:
              min <= k and max >= k 
        (we include equals because the min or max could be the value of k itself)


        """
        k = self.keys[i]        # the key value k of node i
       # print("call minmax on node", k)

        ileft = self.lchilds[i]
        iright = self.rchilds[i]

        ## CHECK MEMOIZATION
        if self.minmax[i] is not None:
         #   print("using memoized value")
            return self.minmax[i]


        ## BASE CASE, i is a leaf, so its key k is only value in the subtree rooted at i
        if ileft == -1 and iright == -1:
            self.minmax[i] = (k,k)
         #   print("node", k, "is a leaf")
            return self.minmax[i]            # memoize the value and return

        ## BASE CASE, i's immediate left or right child is too big/small
        # modified to not allow duplicate keys in left subtree
        if (ileft !=-1 and self.keys[ileft] >= k) or (iright!=-1 and self.keys[iright] < k):
                self.minmax[i]= False
                return False            

        ## RECURSIVE CALLS
        lmin, lmax, rmin, rmax = k, k, k, k

        if ileft != -1:                       #left child exists
            left = self.get_minmax(ileft)
            if left is False:                 #left subtree is invalid
                self.minmax[i]= False
                return False
            else:                             
                lmin, lmax = left             #left subtree valid 
                if lmax >= k:                  # but contains items bigger than (OR EQUAL TO) k
                    self.minmax[i]= False
                    return False                    


        if iright != -1:                        #right child exists
            right = self.get_minmax(iright)
            if right is False:                 #right subtree is invalid
                self.minmax[i]= False
                return False
            else:                             
                rmin, rmax = right             #right subtree valid 
                if rmin < k:                  # but contains items smaller than k
                    self.minmax[i]= False
                    return False                    


        smallest = min(k, lmin, rmin)
        biggest = max(k, lmax, rmax)

        self.minmax[i] = (smallest, biggest)  #memoize and return
      #  print("memoizing", self.minmax[i], "for node", k)
        return self.minmax[i]




    def is_binary_search_tree(self, i=0):
        """
        for naive version: starting from the node with index i, checks if 
        it satisfies the binary search tree property with recursion 

        returns True if bst, otherwise False

        NB. THIS VERSION WILL NOT WORK if the node violating the binary property
        is further down in the tree (ie not an immediate child)
        """

        k = self.keys[i] # the key value k of node i

        ## check left side
        ileft = self.lchilds[i]
        if ileft != -1:
            if self.keys[ileft] >= k or not self.is_binary_search_tree(ileft):  #RECURSIVE CALL
                return False   # left subtree is not bst
        ## now check right side
        iright = self.rchilds[i]
        if iright !=-1:
            if self.keys[iright] <=k or not self.is_binary_search_tree(iright): #RECURSIVE CALL
                return False     # right subtree is not bst

        ## if right/left subtrees exist, they are bst
        return True
                


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

def test_bst():
    # SAMPLE1
    # keys = [2, 1, 3]
    # lchilds = [1, -1, -1]
    # rchilds = [2, -1, -1] 

    # SAMPLE2
    # keys = [1, 2, 3]
    # lchilds = [1, -1, -1]
    # rchilds = [2, -1, -1]

    # SAMPLE4
    # keys = [1, 2, 3, 4, 5]
    # lchilds = [-1,-1,-1,-1,-1]
    # rchilds = [1,2,3,4,-1]

    #SAMPLE5
    # keys = [4, 2, 6, 1, 3, 5, 7]
    # lchilds = [1, 3, 5, -1, -1, -1, -1]
    # rchilds = [2, 4, 6, -1, -1, -1, -1]

    # SAMPLE 6
    keys = [4, 2, 1, 5]
    lchilds = [1, 2, -1, -1]
    rchilds = [-1, 3, -1, -1]


    tr = Tree(keys, lchilds, rchilds)
    print(tr)

    if tr.get_minmax(0) is False:
        print("INCORRECT")
    else:
        print("CORRECT")

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

    ## EMPTY TREE OR TREE WITH ONLY A ROOT ALWAYS CORRECT
    if n<=1:
        print("CORRECT")
        return

    ## AT LEAST TWO NODES, CHECK BINARY PROPERTY
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
    
    if tr.get_minmax(0) is False:
        print("INCORRECT")
    else:
        print("CORRECT")


    # tr.order("in")
    # print()
    # tr.order("pre")
    # print()
    # tr.order("post")

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
