# python3
"""
Substring Equality
In this problem, you will use hashing to design an algorithm that is able to preprocess a given string 𝑠
to answer any query of the form “are these two substrings of 𝑠 equal?” efficiently. This, in turn, is a basic
building block in many string processing algorithms.

Input Format. The first line contains a string 𝑠 consisting of small Latin letters. The second line contains
the number of queries 𝑞. Each of the next 𝑞 lines specifies a query by three integers 𝑎, 𝑏, and 𝑙.

a and b are the 0-based start positions of the two substrings, l is the length

Longest Common Substring


"""

from random import randint

### values used for substring equality
### prob of collision prop to 1/prime, and x must be int between
### 1 and prime-1
PRIME1 = (10**9) + 7
PRIME2 = (10**9) + 9
X =randint(1, 10**9) 




def polyhash(s, x=263, prime=PRIME1):
    # The ord() function returns an integer c, representing the Unicode character.
    # Polynomial funciton is,
    #   SUM (from i=0 to last index in string) of (ith char)*x^i  modP
    # eg for a four-character string:
    #    c0x^0 + c1x^1 + c2x^2 +c3x^3
    #
    # if you start from i=0 but work backwards through the string,
    # hash0 = c3x^0 = c3
    # hash1 = c3*x +c2
    # hash2 = c3*x^2 +c2*x +c1
    # hash3 = c3*x^3 + c2*x^2 + c1*x + c0
    #
    # and more generally you can iteratively do :
    #   hash(next) = hash(previous)*x + c(next)
    #
    # all mod prime
    #
    # x and prime are global constants defined above

    tot = 0
    for c in reversed(s):
        tot = (tot*x + ord(c)) % prime

    return tot

class HashString(object):
    def __init__(self, s, prime=PRIME1, x=X):
        """
        s is the string
        prime and x are ints, the parameters to use for the 
        polyhash function
        """
        self.s = s
        self.prime = prime
        self.x = x 

        self.prefixes = self.get_prefixes()

        self.yvals = [1]  # to memoize y = x^n mod prime, first entry (for n=0) is 1


    def forward_polyhash(self, s):
        """
        utility function, for testing
        s is the string you want to hash, using parameters self.x and self.prime

        uses a polyhash that moves forward through the string like so:

        #eg for a four-character string:
        #   c0x^3 + c1x^2 + c2x + c3
        # 
        # hash0 = c0  = 0 + c0
        # hash1 = c0*x + c1  = hash0*x + c1
        # hash2 = c0*x^2 + c1*x + c2  = hash1*x + c2
        # hash3 = c0*x^3 + c1*x^2 + c2*x + c3  = hash2*x + c3
        # 
        # and more generally, hash[i] = hash[i-1]*x + ci


        """
        tot = 0
        for c in s:
            tot = (tot*self.x + ord(c)) % self.prime

        return tot


    def get_prefixes(self):
        """
        computes hash values of all possible substrings of self.s with 
        start position 0. Uses a FORWARD polyhash function, see below, 
        with parameters self.x and self.prime (both integers).

        eg if s = s0,s1,s2,s3,s4 
        the substrings are s0, s0s1, s0s1s2, s0s1s2s3, s0s1s2s3s4

        returns an array h containing the resulting prefix hashes
        (in the hash array, the value stored in pos j is the hash of the 
        substring starting at pos 0 and ending at pos j, inclusive)

        """
        # This is like polyhash, except we work forwards 
        # rather than backwards through the string
        # as a result, the hash function becomes, eg for a four-character string:
        #   c0x^3 + c1x^2 + c2x + c3
        # 
        # hash0 = c0  = 0 + c0
        # hash1 = c0*x + c1  = hash0*x + c1
        # hash2 = c0*x^2 + c1*x + c2  = hash1*x + c2
        # hash3 = c0*x^3 + c1*x^2 + c2*x + c3  = hash2*x + c3
        # 
        # and more generally, hash[i] = hash[i-1]*x + ci
    
        h = []

        tot = 0
        for c in self.s:
            tot = (tot*self.x + ord(c)) % self.prime
            h.append(tot)

        return h

    def get_yval (self, n):
        """
        n is an int, for which we want to compute y = (self.x^n) mod self.prime
        (ie multiply x by itself n times)
        uses memoization in self.yvals, where:
        yvals[n] contains the corresponding result
        """
        last_n = len(self.yvals)-1  #max value of n for which we have already memoized

        if n <= last_n:             
            return self.yvals[n]    # value is already memoized
        else: 
            m = n - last_n   #need to do m more multiplications
            y = self.yvals[-1] #get the last y value
            for _ in range(m):
                y = (y*self.x) % self.prime
                self.yvals.append(y)
            return y


    def hash_substring(self, i, n):
        """
        computes the hash of the substring of self.s having
        start position i and length n, using the precomputed
        prefixes stored in self.prefixes
        """
        assert i>=0 and i <len(self.s)
        assert n>0 and i+n <= len(self.s)

        ## compute y = (x^n) mod prime 
        ## multiply x by itself n times
        # y=1
        # for _ in range(n):
        #     y = (y*self.x) % self.prime

        y= self.get_yval(n)      

        ## hash of substring starting at i of length n is equal to
        ##    H(0-->end) - x^n * H(0-->start)
        ## where
        ##    H(0-->end)   = hash of substring pos(0)-->pos(i+n-1) inclusive
        ##    H(0-->start) = hash of substring pos(0)-->pos(i-1) inclusive
        ##  
        h = self.prefixes

        h_start = 0 if i==0 else h[i-1]
        h_end = h[i+n-1]

        # print("hstart = ", h_start)
        # print("hend = ", h_end)
    
        hash_ss = h_end - (y * h_start)%self.prime

        if hash_ss < 0:                     #manage negative values
            hash_ss = (hash_ss+self.prime) % self.prime

       # print("substring hash is", hash_ss)
        return hash_ss



    def check_equality(self, a=0, b=0, l=1):
        """
        a and b are the start indices of two length-l substrings of self.s
        checks if the substrings a and b are e,qual
        returns True if they are
        False otherwise

        """
        ## if start indices are the same, then substrings are the same
        if a==b:
            return True

        hash_a = self.hash_substring(a, l)
        hash_b = self.hash_substring(b, l)

        if hash_a == hash_b: 
        # print("hashes match")
            return True
        else:
            #print("hashes are different")
            return False

    def get_khashes(self, k):
        """
        k is an int between 1 and len(self.s) inclusive
        computes hashes of all possible length-k substrings of self.s and returns them
        in a list of ints, khashes[]
        where khashes[j] = hash of the k-length substring starting at position j of self.s
        """ 
        assert k>0 and k<=len(self.s)
        khashes = []

        ## first start index of substring is 0
        ## last start index of subsstring is len(s) - k
        for i in range(len(self.s)-k +1):
            khashes.append(self.hash_substring(i, k))

        return khashes

def get_common_elements(l1,l2):
    """
    l1 and l2 are lists
    checks if they contain any common elements and returns (i1, i2)
    where i1, 12 are the indices of the first common element found in each list
    returns (None, None) if no common elements found
    """
    common_elements = list(set(l1) & set(l2))

    if len(common_elements)== 0:
        return (None, None)

    i1 = l1.index(common_elements[0])
    i2 = l2.index(common_elements[0])

    return (i1, i2)

def find_common_substring(s1, s2):
    """
    s1 and s2 are nonempty strings, for which we want to find the longest common substring
    returns (i1, i2, l) the indices of the longest common substring found and its 
    in case of no substring found returns indices 0 and l=0.
    """
    if len(s1) == 0 or len(s2) == 0:
        return (0,0,0)

    ## hashstring objects for both strings
    hs1 = HashString(s1)
    hs2 = HashString(s2)

    ## initial return values
    (i1, i2, l) = (0, 0, 0)

    lmin = 0                        ## shortest possible length for common substring
    lmax = min(len(s1), len(s2))    ## max possible length for a common substring

    lmid = (lmax + lmin)//2     ## find first midpoint

    while lmid >= lmin and lmid>0:
        print(lmin,"-->", lmax, "lmid=", lmid)

        ## see if there is a common substring of length lmid
        khashes1 = hs1.get_khashes(lmid)
        khashes2 = hs2.get_khashes(lmid)

        ## returns indices of commmon elements, or (None, None) if not found
        (j1, j2) = get_common_elements(khashes1, khashes2)

        if j1==None or j2==None:  ## no length lmid common substring
            print("no length", lmid, "common substring")
            lmax = lmid-1         ## next try between lmin->lmid-1


        else:                     #found length lmid common substring
            print("found length", lmid, "common substring")
            (i1, i2, l) = (j1, j2, lmid)   ## update return values
            lmin = lmid+1                  ##  next try between lmid+1-->lmax 

        # calculate new midpoint for both cases
        lmid = (lmin + lmax)//2
            
    print("found longest comon substring of length", l)
    print("at indices", i1, i2)

    return (i1, i2, l)






def test(s):
    """
    test function for HashString class
    s is a string
    """
    hs = HashString(s)

    n = len(s)


    ## get a random start and end position in this string
    istart = randint(0, n-1)
    iend = randint(istart, n-1)

    substring = s[istart:iend+1]
    print("start pos is", istart, "and end pos is", iend)
    print("the substring is", substring)

    ## compute substring hash using the precomputed prefixes:
    hash1 = hs.hash_substring(istart, iend-istart+1) 

    ## compute substring hash directly
    hash2 = hs.forward_polyhash(substring)

    print("hash using prefixes =", hash1)
    print("direct hash = ", hash2)

def test2(s):
    """
    test function for HashString class
    s is a string
    """
    hs = HashString(s)
    n = len(s)

    ## get two random start positions in this string
    a = randint(0, n-1)
    b = randint(0, n-1)

    ## figure out max substring length for these two start indices
    l_max = n - max(a, b)

    ## get a random substring length
    l = randint(1, l_max)

    print("checking equality for a=", a, ", b=",b, ", length=",l)

    if hs.check_equality(a, b, l):
        print("yes")
    else:
        print("no")



if __name__ == '__main__':
    pass
    # s = input()
    # n = int(input())   #number of queries

    # hs = HashString(s)

    # for _ in range(n):
    #     qs = input().split()
    #     (a, b, l) = [int(element) for element in qs]
    #     if hs.check_equality(a, b, l):
    #         print("Yes")
    #     else:
    #         print("No")



