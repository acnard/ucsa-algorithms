# python3
"""
In this problem, your goal is to implement the Rabin–Karp’s algorithm.
for searching the given pattern in the given text.
Input Format. There are two strings in the input: the pattern 𝑃 and the text 𝑇.

Output Format. Print all the positions of the occurrences of 𝑃 in 𝑇 in ascending order. 
Use 0-based indexing of positions in the the text 𝑇.

"""
from random import randint


## parameters for polyhash function 
PRIME1 = (10**9)+7
PRIME2 = (10**9)+9
X = randint(1, 10**9)


def print_occurrences(output):
    print(' '.join(map(str, output)))


def compare_strings(s1, s2):
    """
    s1 and s2 are the two strings we want to compare (find longest common substring)
    """
    ## longest possible length of common substring is length of shortest of the two
    ## shortest possible common substring is a single character
    k_max = min(len(s1), len(s2))
    k_min = 1

    hs1 = HashString(s1)
    hs2 = HashString(s2)

    print("s1:\n", hs1.k_hashes)
    print("s2:\n", hs2.k_hashes)

    print("kmax", k_max)


    ## bisection search - start from a middle value k_mid
    ## if there is a common substring of length k_mid, then we go 
    ## on to search for any longer ones (the short ones for sure exist), 
    ## between k_mid+1 and k_max
    ## if there is no common substring of length k_mid, we must search
    ## between k_min and k_mid-1
    while(k_max > k_min):
        k_mid = (k_max+k_min)//2     
        if hs1.k_hashes[k_mid]







class HashString(object):
    def __init__(self, s, x=X, prime=PRIME1):
        """
        s is a string, that we want to work with through hashing
        x and prime are ints, the parameters to use for polyhash, etc.
        """
        self.s = s
        self.x = x
        self.prime = prime
        self.k_hashes = self.all_k_hashes()


    def polyhash(self, text):
        """
        text is a string, returns the polyhash of it, using the 
        values self.x and self.prime
        """
        # The ord() function returns an integer c, representing the Unicode character.
        # Polynomial function is,
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

        tot = 0
        for c in reversed(text):
            tot = (tot*self.x + ord(c)) % self.prime

        return tot

    def precompute_hashes(self, k):
        """
        k is an int, the length of the substring
        precomputes the hashes for all k-length substrings of self.s, 
        and returns them as an array of ints
        """
        
        num_substrings = len(self.s) - k + 1
        hashes = [None]*(num_substrings)

        lastpos = len(self.s) - k  # last index pos where a substring can start

        ## compute polyhash of last substring in text
        hashes[-1] = self.polyhash( self.s[lastpos:])
        
        ## compute y = (x**k) mod prime
        ## multiply x by itself k times
        y = 1
        for _ in range(k):
            y = (y*self.x) % self.prime
        

        ## work backwards from penultimate substring position to zero
        for i in range(lastpos-1, -1, -1):
            
            ## we have to take val mod prime but val may be negative
            ## compute the next hash value, working backwards
            ## take mod prime at each stage of the calcuation
            val = (self.x * hashes[i+1]) % self.prime 
            val = ( val + ord(self.s[i]) )%self.prime   
            val = val - ( y*ord(self.s[i+k]) )%self.prime
            
            if val < 0:
                val = (val+self.prime) 
            hashes[i] = (val) % self.prime 
        
        return hashes

    def all_k_hashes(self):
        """
        returns a list of lists, containing the hashes of all k-length 
        substrings of self.s, for all possible values of k 

        """

        ## zeroth element of k_hashes is [None] so that
        ## in general k_hashes[j] = list of all j-length substrings of self.s
        k_hashes = [[None]] 

        for k in range(1, len(self.s)+1):  # longest substring is len(self.s)   
            k_hashes.append(self.precompute_hashes(k))

        return k_hashes


    def test_precompute(self, k):
        """
        compares the precomputed hashes for length-k substrings 
        with the manually generated ones
        """

        precomputed = self.precompute_hashes(k)

        manual = []
        for i in range( len(self.s) - k + 1):
            substring = self.s[i:i+k]  # slice the substring
            manual.append( self.polyhash(substring) ) 

        print("manual hashes:", manual)
        print("prcomputed hashes", precomputed)

        if manual == precomputed:
            print("same results")
        else:
            print("discrepancy")



def test(pattern, text):
    result = get_occurrences(pattern, text)
    result_naive = get_occurrences_naive(pattern, text)
    result_optimized = get_occurrences_opt(pattern, text)

    print("result:", result)
    print("result naive:", result_naive)
    print("result optimized:", result_optimized)

if __name__ == '__main__':
   # print_occurrences(get_occurrences(*read_input()))

  #  (pattern, text) = (input().rstrip(), input().rstrip())
    pass
    #test(pattern, text)
  #  print_occurrences(get_occurrences_opt(pattern,text))
