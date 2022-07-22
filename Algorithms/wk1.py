# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:29:01 2021

@author: Anna
"""
from random import randint
import random

## solution using python built-in max function
## to find biggest and second biggest numbers in list
def max_pairwise_product(numbers):

    #find biggest number    
    biggest = max(numbers)
    numbers.remove(biggest)
    
    #find second biggest
    secondbiggest = max(numbers)

    print( "{}*{}={}".format(biggest, secondbiggest, biggest*secondbiggest) )
    return biggest*secondbiggest

## manual optimized solution
## find biggest and second biggest number
## then multiply them together
def max_pairwise_product_manual(numbers):

    print(numbers)

    #find biggest number    
    biggest = 0
    for num in numbers:
        if num>biggest:
            biggest = num
            
    #remove it from the list
    numbers.remove(biggest)
    print(numbers)
    
    #find second biggest
    secondbiggest = 0
    for num in numbers:
        if num>secondbiggest:
            secondbiggest = num   

    print("biggest, secondbiggest", biggest, secondbiggest)
    return biggest*secondbiggest

## solution using python built-in sorting
## but this is wasteful because we only need to find the two biggest numbers
## and the rest of the list can be left out of order
def max_pairwise_product_builtinsort(numbers):
    numbers.sort(reverse=True) #sort in place
    print(numbers)
    return numbers[0]*numbers[1]


## naive solution, multiplies together all possible combinations of 
## pairs of digits, runs in n**2 time
def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product




## Test functions
def stresstest():
    
    ## test a long list of numbers
    # biglist = [n for n in range(1,(2*10**5)+1)]
    # assert max_pairwise_product(biglist) == 39999800000
    
    ## generate list of random integers
    ## randint(a,b) generates random int in range [a,b], both endpoints included
    
    random.seed(1)  # specify seed to ensure same pseudorandom sequence each time
                    # this will let you go back and repeat the same case if it fails

    list_length = 10   # how many integers in the list
    max_val = 10**5    # how big the integers can be (inclusive)
    
    randints = [randint(0,max_val) for i in range(list_length)]    
    print(randints)
    
    result1 = max_pairwise_product_naive(randints)
    result2 = max_pairwise_product(randints)
    
    if result1==result2:
        print("ok")
    else:
        print("wrong answer", result1, result2)


## nb main asks us to first input the list length n and then 
## the list itself, however in python we don't need the n
# if __name__ == '__main__':
#     input_n = int(input())
#     input_numbers = [int(x) for x in input().split()]
#     print(max_pairwise_product(input_numbers))