# python3
"""
In this problem, you will use hashing to design an algorithm that is able to preprocess a given string 𝑠
to answer any query of the form “are these two substrings of 𝑠 equal?” efficiently. This, in turn, is a basic
building block in many string processing algorithms.

Input Format. The first line contains a string 𝑠 consisting of small Latin letters. The second line contains
the number of queries 𝑞. Each of the next 𝑞 lines specifies a query by three integers 𝑎, 𝑏, and 𝑙.

a and b are the 0-based start positions of the two substrings, l is the length

"""

from random import randint

### values used for substring equality
### prob of collision prop to 1/prime, and x must be int between
### 1 and prime-1
PRIME1 = (10**9) + 7
PRIME2 = (10**9) + 9
X =randint(1, 10**9) 



def print_occurrences(output):
    print(' '.join(map(str, output)))




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

        self.hashes = self.polyhashes()

    def polyhashes(self):
        """
        computes hash values of all possible substrings of self.s with 
        start position 0. Uses a FORWARD polyhash function, see below, with parameters self.x and self.prime (both integers).

        eg if s = s0,s1,s2,s3,s4 
        the substrings are s0, s0s1, s0s1s2, s0s1s2s3, s0s1s2s3s4

        returns an array h containing the resulting hashes
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

    def hash_substring(self, i, n):
        """
        computes the hash of the substring of self.s having
        start position i and length n
        """

        ## compute y = (x^n) mod prime 
        ## multiply x by itself n times
        y=1
        for _ in range(n):
            y = (y*self.x) % self.prime

        ## hash of substring starting at i of length n is equal to
        ##    H(0-->end) - x^n * H(0-->start)
        ## where
        ##    H(0-->end)   = hash of substring pos(0)-->pos(i+n-1) inclusive
        ##    H(0-->start) = hash of substring pos(0)-->pos(i-1) inclusive
        ##  
        h = self.hashes
        hash_ss = h[i+n-1] - (y * h[i-1])%self.prime

        if hash_ss < 0:                     #manage negative values
            hash_ss = (hash_ss+self.prime) % self.prime

        print("substring hash is", hash_ss)
        return hash_ss



def check_equality(s, a=0, b=0, l=1, prime=PRIME1, x=X):
    """
    s is a string, a and b are the start indices of two substrings of length l
    prime and x are the parameters to use for polyhashing
    checks if the substrings a and b are equal
    """

    ## precompute all hash prefixes for the string s
    h = polyhashes(s, prime, x)

    print("h=", h)

    ## compute y = (X^l) mod prime 
    ## multiply X by itself l times
    y=1
    for _ in range(l):
        y = (y*x) % prime

    ## compute the hash of each substring
    ## hash of substring starting at a of length l is equal to
    ##    H(0-->end) - x^l * H(0-->start)
    ## where
    ##    H(0-->end)   = hash of substring pos(0)-->pos(a+l-1) inclusive
    ##    H(0-->start) = hash of substring pos(0)-->pos(a-1) inclusive
    ##
    ##  
    hash_a = h[a+l-1] - (y * h[a-1])%prime

    print("hash a, hash b =", Hash_a, Hash_b)


if __name__ == '__main__':
    pass
   # print_occurrences(get_occurrences(*read_input()))

   # (pattern, text) = (input().rstrip(), input().rstrip())

    #test(pattern, text)
    #print_occurrences(get_occurrences_opt(pattern,text))
