# Uses python3


def transform(s1, s2, memo={}):
    """ 
    The edit distance between two strings is the minimum number of operations 
    (insertions, deletions, and substitutions of symbols) 
    to transform one string into another.
    
    s1 is the initial string and s2 is the final string 
    (assume both are only lowercase letters)
    returns the min number of operations to change s1 to s2
    
    memo maps tuples (s1,s2) --> int min number of transformations
    """
    # print("comparing strings:")
    # print(s1)
    # print(s2)
    
    # base case, strings are the same with zero transformations
    if s1 == s2:
        return 0

    # base case, one of the strings is exhausted    
    if s1=="" or s2=="":
        return len(s1+s2)
        
    #check if answer in memo  (check both orders because symmetrical)  
    if (s1, s2) in memo:
        return memo[ (s1, s2) ]
    if (s2, s1) in memo:
        return memo[ (s2, s1) ]
    
    # RECURSIVE compare insert, delete, substitute, do nothing
    results = []
    
    results.append(1 + transform(s1, s2[1:]) )  # delete leading char from s2 
    results.append(1 + transform(s1[1:], s2) )  # delete leading char from s1
    results.append(1 + transform(s1[1:], s2[1:]) )  # subst leading char of s1 to match s2     
                
     # if first chars match, do nothing: cost = cost of substituting - 1
    if s1[0] == s2[0]:
        results.append( results[-1]-1 )  

    #memoize and return the best result
    memo[(s1, s2)] = min(results)
    #print("added memo entry", (s1,s2), ":", min(results) )
    return min(results)

if __name__ == "__main__":

    ## for autograder
    string1 = input()
    string2 = input()
    
    print( transform(string1, string2) )
