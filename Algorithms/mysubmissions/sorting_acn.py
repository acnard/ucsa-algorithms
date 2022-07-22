# Uses python3

import random

    
    
def quicksort3(seq):
    """
    seq is a list or tuple of integers
    returns a copy of the list, sorted in ascending order
    3-way partition variant
    """
    # base case: if 0 or 1 elements, is already sorted
    if len(seq) <= 1:
        return seq[:]
    
    ## two or more elements: split seq
    pivot = random.choice(seq)  #pick pivot 

    #seq.remove(pivot)  #don't remove from list, it'll go in the equals array
    low = []  #items < pivot
    high = []  # items > pivot
    equal = [] # items == pivot
    
    for num in seq:
        if num<pivot:
            low.append(num)
        elif num>pivot:
            high.append(num)
        else:
            equal.append(num)
    # print("\npartitioning", seq)
    # print("pivot is", pivot, "low=", low, "high=", high, "equal=", equal)
    
    ## recursive calls: sort each half
    low = quicksort3(low)
    high = quicksort3(high)
    
    result = low + equal + high
   # print("result is", result)
    return result


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
        
    ## for autograder
    lenseq = input()
    sequence = input()
    
    sequence = list(map(int, sequence.split() ))
    print( quicksort3(sequence) )
