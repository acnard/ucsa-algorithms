
import random


def get_num_inversions_naive(seq):
    # for each number in turn, count how many to its right are smaller
    count=0
    for i in range( len(seq)-1 ):
        num = seq[i]
        
        for othernum in seq[i+1:]:
            if othernum < num:
                count+=1
    return count
       
def inversioncount(seq, count=0):
    """
    seq is a list or tuple of integers, count in an integer
    returns a tuple (seq,count): copy of seq, sorted in ascending order
    and a count of the inversions found in it
    """
    
    # base case: if 0 or 1 elements, is already sorted
    if len(seq) <= 1:
        return (seq[:], 0)
 

    # two or more elements: split seq in half
    mid = len(seq)//2
    leftseq = seq[:mid]
    rightseq = seq[mid:]
    
    # sort each half - recursive call
    leftseq, countleft = inversioncount(leftseq, count)
    rightseq, countright = inversioncount(rightseq, count)    
    
    count+= (countleft + countright)
    
    # merge the results
    # print("\n** merging", leftseq, "and", rightseq)
    # print("count before merge is", count)
    
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
                # inversion found: leftseq[0] > rightseq[0] 
                # but also all other elements of leftseq must be
                # greater than rightseq[0] (since leftseq is ascending)
                mergedseq.append(rightseq.pop(0))
                count+=len(leftseq)
                
        
    #     print("mergedseq so far=", mergedseq)
    # print("count after merge is", count)
    # return the merged sequence and the updated inversion count
    return mergedseq, count
    

    
     

def test(n):
    """ n is an integer, generates list of n 
        random integers between 0 and MAX, 
      """
    # generate a list of n random nonegative integers

    MAX = 8
    seq = list( [random.randint(0, MAX) for i in range(n)]  )

    print("sequence is ", seq)
    print("naive inversion count is", get_num_inversions_naive(seq) )
    
    print("recursive inversion count is", inversioncount(seq)[1] )

   
    

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    
    ## for autograder
    lenseq = input()
    sequence = input()
    
    sequence = list(map(int, sequence.split() ))
    print( inversioncount(sequence)[1] )
