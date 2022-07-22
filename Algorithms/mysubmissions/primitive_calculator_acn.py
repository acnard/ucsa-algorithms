# Uses python3


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def make_num(n, memo = {}):   
    """
    You are given a primitive calculator that can perform the following three operations with
    the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a
    positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛
    starting from the number 1. 
    
    memo is a dict mapping int numbers -> [seq to make that number]
    
    returns seq, a list of the intermediate numbers to get from 1 to n 
    (inclusive of endpoints)
    
    """
    
    ## base cases
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
       return [1,3]
    
    ## check memo 
    if n in memo:
        return memo[n]
    
    ## try to go from 1 to n starting with each operation in turn 
    ## and see which one does best
    assert n >= 4
    #print("trying to make", n)
    results = []
    if n%3 == 0:
        results.append( make_num(n//3, memo) + [n] ) # mult3
    if n%2 == 0:
        results.append( make_num(n//2, memo) + [n] ) # mult2
    if (n%2 == 1 or n%3 == 1):
        results.append( make_num(n-1, memo) + [n] )  # add 1 (put in if to avoid recursion error)


        

    ## sort the results from best (shortest sequence) to worst (longest)
    results.sort( key=lambda x:len(x) ) 
    #print("results for", n, "are", results)
    
    # memoize and return the best one
    memo[n] = results[0]
    
   # print("memo is now", memo)
    return memo[n]

    


if __name__ == '__main__':
    n = int( input() )
    best_seq = make_num(n)

    print(len(best_seq) - 1)    
    for num in best_seq:
        print(num, end=" ")
    

