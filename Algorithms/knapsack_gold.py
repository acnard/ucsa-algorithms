# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:46:12 2022

@author: Anna

You are given a set of bars of gold and your goal is to take as much gold as possible into
your bag. There is just one copy of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar)

Task. Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.

Input Format. The first line of the input contains the capacity 𝑊 of a knapsack 
and the number 𝑛 of bars of gold. 
The next line contains 𝑛 integers 𝑤0, 𝑤1, . . . , 𝑤𝑛−1 defining the weights of the bars of gold.
Constraints. 1 ≤ 𝑊 ≤ 104; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . , 𝑤𝑛−1 ≤ 105

Output Format. Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.
"""

import random

def max_weight(C, bars, memo={}):
    """
    C is an int, the bag capacity
    bars is a tuple of ints, the weights of the available gold bars, sorted in
    descending order    (you can only take one of each bar)
    
    memo is a dict mapping a tuple (sorted seq of bars) --> nested dict mapping 
                an int, capacity C--> int, max weight of gold that can fit in C.
    
    return the max weight of gold bars that can fit in the bag
    """
   # print("trying to make", C, "with bars", bars)
    
    ## base case: there are no bars, or bag capacity is zero
    if len(bars) == 0 or C==0:
    #    print("no bars, or capacity is zero")
        return 0
    
    # base case: if C can hold all the bars, take all of them
    #   that's the best you can do
    if C>= sum(bars):
        return sum(bars) 
    
    bars_that_fit = [bar for bar in bars if bar<=C]
    
    ## base case: all the bars are heavier than C
    if len(bars_that_fit) == 0:
        return 0
    
    ## base case: there is only one bar that fits
    if len(bars_that_fit) == 1:
        return bars_that_fit[0]
    
    ## base case: one of the bars weighs exactly same as C
    if C in bars_that_fit:
        return C
    
    ## check memo
    if bars in memo:
        if C in memo[bars]:
            #print("found in memo:", bars, "-->", C, ":", memo[bars][C])
            return memo[bars][C]
            
    
    ## try to take one of each bar that fits and see which gives the 
    ## best result (RECURSIVE CALL)
    results = []
    for bar in bars_that_fit:
       
        remaining_bars = bars_that_fit[:]       #make a copy of the list
        remaining_bars.remove(bar)              #remove the bar you are trying
        remaining_bars = tuple(remaining_bars)  #change to tuple
        
        remaining_C = C-bar
        results.append(bar + max_weight(remaining_C, remaining_bars, memo))
       
        if C in results:
            break        # quit loop if you've managed exactly C 
        
        
    ## memoize and return the best result
    if bars not in memo:
        memo[bars]= {}
    memo[bars][C] = max(results)
    #print("memoize", bars, "-->", C, ":", max(results))
    
    return max(results)                       
        
def test(n):
    
    # generate a sequence of n gold bars with weights betw 1 and MAX inclusive

    MAX = 1000  # actual max is 10^4, min is 1
    bars = list( [random.randint(1, MAX) for i in range(n)]  )

    bars.sort(reverse=True)
    bars = tuple(bars)
    
    # generate a random capacity
    
    C = random.randint(1, MAX*10)
    print("try to make", C, "with bars", bars)
    print( max_weight(C, bars) )
    
    
    
if __name__ == '__main__':

    
    # for autograder
    line1 = input()
    line1 = list( map(int, line1.split()) )
    
    C = line1[0]
    
    bars = input()
    bars = tuple( map(int, bars.split()) )
    

    print( max_weight(C, bars) )
        
    
    
    