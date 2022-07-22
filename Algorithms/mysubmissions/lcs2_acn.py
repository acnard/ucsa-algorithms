#Uses python3

import random

def lcs2(a, b, memo = {}):
    """
    a and b are tuples of integers, returns a tuple, the largest common subsequence (lcs)
    found between a and b.
    
    memo maps a tuple of two tuples of ints (a, b) --> a tuple, their lcs
    
    (nb could actually just memoize the length of their lcs)
    """
    # base case the two sequences are the same
    if a == b:
        return a
    
    # base case, one of the two sequences is empty
    if len(a)==0 or len(b)==0:
        return ()

    #check if answer in memo  (check both orders because symmetrical)  
    if (a, b) in memo:
        return memo[ (a, b) ]
    if (b, a) in memo:
        return memo[ (b, a) ]
    
    # RECURSIVE, compare shifting either a or b to the left
    results = []

    results.append( lcs2(a[1:], b, memo) )    
    results.append( lcs2(a, b[1:], memo) )       
    
    # if current leading numbers match shift both a and b to the left
    if a[0]==b[0]:
        results.append( (a[0],) + lcs2(a[1:], b[1:], memo) )           
    
    
    ## sort the results from best (longest sequence) to worst (shortest)
    results.sort( key=lambda x:len(x), reverse=True ) 
    

    # memoize and return the best one
    memo[(a,b)] = results[0]
#    print("added memo entry", (a,b), ":", results[0] )
    return results[0]   






def test(n, m):
    """ n and m are integers, generates two list of n and m
        random integers between MIN and MAX, 
      """

    MIN = -10
    MAX = 10
    seq1 = tuple( [random.randint(MIN, MAX) for i in range(n)]  )
    seq2 = tuple( [random.randint(MIN, MAX) for i in range(m)]  )

    print("sequences are:")
    print(seq1)
    print(seq2)
    
    print("longest common subsequence is")
    print(lcs2(seq1, seq2) )
    
def test2():
    a = (2, 7, 5)
    b = (2, 5)
    print("sequences are:")
    print(a)
    print(b)
    
    print("longest common subsequence is")
    print(lcs2(a, b) )    
    

if __name__ == '__main__':
    pass
    # for autograder
    n = input()  #not used
    seq1 = input()
    seq1 = tuple( map(int, seq1.split()) )
    
    m = input() #not used
    seq2 = input()
    seq2 = tuple( map(int, seq2.split()) )
    

    print( len(lcs2(seq1, seq2)) )
