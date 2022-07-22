import random

def binary_search(seq, query):
    # searches the ascending sequence 'seq' for  the element 'query' and 
    # returns its index if found, otherwise -1
    # this version does not use built-in functions

    istart = 0
    iend = len(seq)-1

    while istart <= iend:

        #if there is only one item imid will point to that iem
        imid = istart + (iend-istart+1)//2   #midpoint

        if seq[imid] == query:
            return imid
        elif seq[imid] > query:
            iend = imid-1  # if iend becomes < istart, at next iteration will exit loop
        else:               
            istart = imid+1 # if istart becomes > iend, at next iteration will exit loop

    return -1   # exited loop without finding query in the sequence


def test(n):
    """ n is an integer, generates an ascending sequence of n 
        random integers between 0 and MAX, then generates a second list of 
        n random query numbers also between 0 and MAX
        calls both binary_search and binary_search_builtin and compares the results
    """
    # generate a list of n random ascending integers and of n random queries
    MAX = 35
 
    seq = list( [random.randint(0, MAX) for i in range(n)]  )
    seq.sort()
    queries = [random.randint(0, MAX) for i in range(n)]

    print("sequence is ", seq)
    print("queries are ", queries)

    indexes = []

    for q in queries:
        i1 = binary_search_builtin(seq, q)
        i2 = binary_search(seq, q)

        if i1==i2:  #both gave same result
            indexes.append(i1)
        else:
            indexes.append( (i1, i2) )  #append tuple if not matching

    print("indexes found are: ", indexes)



def binary_search_builtin(keys, query):
    # searches the sequence 'keys' for  the element 'query' and 
    # returns its index if found, otherwise -1
    # this version uses the python built-in functions (presumably fast)
    if query in keys:
        return keys.index(query)
    else:
        return -1

if __name__ == '__main__':

    # for humans
    # sequence = input("enter sequence: ")
    # tofind = input("enter values to search for: ")

    # for autograder
    lenseq = input()
    sequence = input()
    lentofind = input()
    tofind = input()

    # discard the first element which is just the list length
    # sequence = list(map(int, sequence.split() ))[1:]
    # tofind = list( map( int, tofind.split() ))[1:]

    # don't discard the first element any more
    sequence = list(map(int, sequence.split() ))
    tofind = list( map( int, tofind.split() ))    

    for q in tofind:
        print( binary_search(sequence, q), end=' ' )


