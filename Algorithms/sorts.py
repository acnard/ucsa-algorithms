
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

def quicksort(seq):
    """
    seq is a list or tuple of integers
    returns a copy of the list, sorted in ascending order
    """
    
    seq = list(seq)  #don't mutate the passed list
    
    # base case: if 0 or 1 elements, is already sorted
    if len(seq) <= 1:
        return seq
    
    ## two or more elements: split seq
    #pivot = seq[-1]            ## pick pivot as last element
   
    pivot = random.choice(seq)  #pick pivot and remove from list
    seq.remove(pivot)
    low = []  #items <= pivot
    high = []  # items > pivot
    
    for num in seq:
        if num<=pivot:
            low.append(num)
        else:
            high.append(num)

    #print("pivot is", pivot, "low=", low, "high=", high)
    
    ## recursive calls: sort each half
    low = quicksort(low)
    high = quicksort(high)
    
    result = low + [pivot] + high
    return result
    

def mergesort(seq):
    """
    seq is a list or tuple of integers
    returns a copy of seq, sorted in ascending order
    """
    
    # base case: if 0 or 1 elements, is already sorted
    if len(seq) <= 1:
        return seq[:]
 

    # two or more elements: split seq in half
    mid = len(seq)//2
    leftseq = seq[:mid]
    rightseq = seq[mid:]
    
    # sort each half - recursive call
    leftseq = mergesort(leftseq)
    rightseq = mergesort(rightseq)    
    
    # merge the results
 #   print("\n** merging", leftseq, "and", rightseq)

    
    mergedseq = []
    totelements = len(leftseq) + len(rightseq) 
    for i in range(totelements):
        if len(leftseq) == 0:
            mergedseq.append(rightseq.pop(0))
        elif len(rightseq) == 0:
            mergedseq.append(leftseq.pop(0))
        else:
            if leftseq[0] <= rightseq[0]:
                mergedseq.append(leftseq.pop(0))
            else:
                mergedseq.append(rightseq.pop(0))
                
        
       # print("mergedseq so far=", mergedseq)

    # return the merged sequence
    return mergedseq
  
    
     

def test(n):
    """ n is an integer, generates list of n 
        random integers between 0 and MAX, 
      """
    # generate a list of n random nonegative integers

    MAX = 3
    seq = list( [random.randint(0, MAX) for i in range(n)]  )

    print("sequence is ", seq)

    print("mergesort seq=" , mergesort(seq) )  
    print("quicksort seq=", quicksort(seq) )
    print("quicksrt3 seq=", quicksort3(seq) )    
   
    

if __name__ == '__main__':

    
    ## for autograder
    lenseq = input()
    sequence = input()
    
    # sequence = list(map(int, sequence.split() ))
