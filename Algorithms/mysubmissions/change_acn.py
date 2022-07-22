# Uses python3
#import sys

def get_change(m):
    """
    find the minimum number of coins needed to change the input value
    (an integer) into coins with denominations 1, 5, and 10
    outputs the minimum number of coins
    """

    tens, remainder = m//10, m%10
    
 #O   print("tens: {}, remainder: {}".format(tens, remainder) )
    
    fives, remainder = remainder//5, remainder%5
    
 #   print("fives: {}, new remainder: {}".format(fives, remainder) )

    n_coins = tens + fives + remainder
 #   print("n coins=", n_coins)
    
    return n_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
