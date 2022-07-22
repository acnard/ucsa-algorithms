import random

def majority(seq):
    """
    seq is a list of nonegative integers
    if seq contains an element that appears 
    strictly more than 𝑛/2 times, return that element, or None otherwise.
 
    """
    #print("\nexamining seq: ", seq)
    
    counts = {}

        
    for num in seq:
        if num not in counts:
            counts[num] = 0
        counts[num]+=1
        
    #print(counts)
    
    for c in counts:
        if (counts[c] > len(seq)//2):
           # print("majority element is", c)
            return 1
    #print("no majority element found")
    return 0

    



def test(n):
    """ n is an integer, generates list of n 
        random integers between 0 and MAX, 
      """
    # generate a list of n random nonegative integers

    MAX = 3
    seq = list( [random.randint(0, MAX) for i in range(n)]  )

    print("sequence is ", seq)

    if majority_builtin(seq)  != majority(seq) :
        print("majority gave different result")
    
    



def majority_builtin(seq):
    """
    seq is a list of nonnegative integers
    using builtin functions, return 1 if seq contains an element that appears 
    strictly more than 𝑛/2 times, and 0 otherwise.
    """
    for num in seq:
        if seq.count(num) > len(seq)//2:
            print("majority element is", num)
            return 1
    print("no majority element found")
    return 0
        
        


if __name__ == '__main__':

    # for humans
   # length = input("enter sequence length: ")
   # sequence = input("enter sequence: ")

    # for autograder
    lenseq = input()
    sequence = input()


    # don't discard the first element any more
    sequence = list(map(int, sequence.split() ))

    print(majority(sequence))



