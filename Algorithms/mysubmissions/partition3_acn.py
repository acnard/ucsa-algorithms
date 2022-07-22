# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:28:04 2022

@author: Anna

You and two of your friends have just returned back home after visiting various countries. 
Now you would like to evenly split all the souvenirs that all three of you bought.


Input Format.   The first line contains an integer 𝑛. 
                The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated by spaces.

Output Format. 
Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and
0 otherwise.
"""
import random

#######################################
#### UNUSED (BUT TESTED) FUNCTIONS ####
#######################################    

def getsums(items, memo = {}):
    """
    items is a tuple of ints sorted *ascending*
    memo is a dict mapping a tuple(items) --> list of all possible sums
                                         that can be made from it
                                         (deduplicated)
                                         
    returns the list of all possible sums that can be made using elements 
    from items. The results list does not contain duplicates
    """
    print("find sums of", items)
    
    ## base cases, items
    if len(items) == 0:
        return []           #empty list, no sums
    
    if len(items) == 1:
        return [items[0]]       # only one item
    
    
    ## check memo : if found just return stored result
    if items in memo:
        return memo[items]   
    
    ## otherwise create new memo entry for this items list
    memo[items] = []
    
    ## recursive call: remove first item & get sums without it
    sub_sums = getsums(items[1:], memo)  #RECURSIVE
    
    # adding item back we can make all the same sub_sums as before, 
    # and additionally each sub_sum+item, and item itself. Memoize this. 
    all_sums = [ items[0] ] + sub_sums  + [x+items[0] for x in sub_sums] 
    
    all_sums = list(set (all_sums) ) #remove duplicates
    memo[items] = all_sums
    
    print("returning memo entry", items, "-->", memo[items])    
    return sorted(memo[items])
    



################################
#### USED FUNCTIONS ############
################################
    
def powerset(items):
    """ 
    items is a tuple of ints sorted *ascending*
    
    returns a list of tuples, all possible subsets of items
    (excluding empty set)       
                
    """
    #print("find powerset of", items)  
    ## base cases
    if len(items) == 0:  # no items return empty list
        return []
    
    if len(items) == 1:   #one item is its own subset
        return [items]
        
    ## recursive call: remove first item & get subsets without it
    sub_results = powerset(items[1:])  #RECURSIVE
    
    # adding item back we can make all the same sub_results as before, 
    # and additionally each sub_result+item, and item itself. Memoize this. 
    all_results = [ items[:1] ] + sub_results  + [items[:1]+x for x in sub_results] 
    
    #print("result is", all_results)
    return(all_results)
    
    
    

def makeval(target, items, memo={}):
    """
    target is an int, the value you want to reach
    items is a sequence of ints sorted *ascending*
    
    Returns a list of tuples: all the subsets of items that 
                              summed together make the target.
    If sum cannot be made returns empty list.
    

    """
    #print("try to make", target, "with", items)
    
    ## base cases
    if sum(items) < target:  #even all items is not enough 
        return []
    
    if sum(items) == target: #taking all of them is only solution
        return [items]
    
   
    ## create the power set of items (this is a list of tuples, 
    ## representing all possible subsets that can be made from items)

    subsets = powerset(items)
    # print("powerset of", items, "is")
    # for subset in subsets:
    #     print(subset)

    results = []        
    for subset in subsets:
        if sum(subset) == target:
            results.append(subset)
            
    return results        
            
 
def tuplediff(t1, t2):
    """
    t1 and t2 are tuples of ints
    
    if all the elements of t2 are present in t1 (also considering duplicates), 
    returns the tuple corresponding to t1 - t2.

    eg (4, 5, 5, 6) - (5, 6) = (4, 5)
    
    (1, 2, 3) - (1, 2, 3) 0 ()
    
    otherwise returns None
    """
    
    tuple1 = list(t1)
    
    for val in t2:
        if val in tuple1:
            tuple1.remove(val)
        else:
            return None
        
    return tuple(tuple1)
    
    

def partition(items, memo={}):
    """
    items is a list of integers (values of the souvenirs), sorted ascending
    
    number of items between 1 and 20 inclusive
    value of each item between 1 and 30 inclusive
    
    returns 1 if items can be partitioned into 3 subsets of equal value
    0 otherwise
    
    """
    
    totval = sum(items)
    # print("total value =", totval, end=" ")
    # print("one third of total = ", totval/3)

    ## base case: sum of items not divisible by 3 or there are less than 3 items    
    if totval%3 != 0 or len(items)<3:
        return []

    ## we want three subsets, each with value = one third of total
    one_third = totval//3
    
    ## base case, there is an item that exceeds one third of value
    for item in items:
        if item > one_third:
            return []            

 
    ## try to make subsets worth one third of total value
    partitions = makeval(one_third, items)
    # print("partitions found:", partitions)
    
    ## now try to find three non-overlapping partitions
    ## remember, partitions is a list of tuples
    if len(partitions) < 3:
        # print("less than 3 partitions found")
        return []
    
    #take each partition in turn
    remaining_partitions = partitions[:]

    for p1 in partitions:
        # remove p1 from the list of partitions and its items from the list of items
        remaining_partitions.remove(p1)
        remaining_items = tuplediff(items, p1)     

        # print("trying p1=", p1)
        #see if there is a second partition that you can still make
        # out of the remaining items. If so, by definition whatever unused
        # items are left must constitute the 3rd partition, since all subsets
        # add to one-third of the total value
        for p2 in remaining_partitions:
            remaining_items2 = tuplediff(remaining_items, p2)
            if remaining_items2 != None:
                return [p1, p2, remaining_items2]
    # print("partitions overlap")
    return []


    
        
    
def test(n=6):

    # generate a sequence of n items with value betw 1 and MAX inclusive
    # repeatedly until you get one whose sum is divisible by three
    MAX = 30  
    
    items = (1, 1) #dummy value to start
    
    while( sum(items) % 3 != 0 ):
        items = list( [random.randint(1, MAX) for i in range(n)]  )

    items.sort()
    items = tuple(items)
    
    print("items are", items)
    
    #print( getsums(items) )
    #print( powerset(items) )

    #set a target that is <= sum of the items
    # target = random.randint(1, sum(items))
    # print("ways to make", target, ":")
    # print( makeval(target, items) )
    
    print( partition(items) )    
    
    

        

if __name__ == '__main__':

   # for autograder
    n = input() 
    items = input()
    items = tuple( map(int, items.split()) )
    
   
    if len( partition(items) ) == 0 :
        print(0)
    else:
        print(1)

    
    

