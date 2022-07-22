# Uses python3
import sys


def givechange(money, coins, memo={}):
    """ money is an int, the amount of money we want to make up
        coins is a list of ints, the deonominations available, in descending order
        assume it always includes 1, eg coins=[25, 10, 5, 1]
        
        memo is a dict mapping money amounts --> to a list numcoins
        that stores the optimal way to make up that amount with the
        specified coins, eg if 
                coins = [15, 10, 5, 1]
                memo[50] = [3, 0, 1, 0]
        
                coins = [10, 20, 1]
                memo[6] = [0, 0, 6]
        
        if money not already present in memo, updates memo with the optimal 
        numcoins list and
        returns the number of coins required to make up the money amount

    """ 
    #base case? making zero money requires zero coins
    if money <= 0:
        return [0 for coin in coins]
    
    #check memo
    if money in memo:
        return memo[money]   # return numcoins list already stored for this amount

    #print("try to make amount", money)
    # use one of each coin plus optimal way to make up remaining amount
    # and see which single coin gives best result
    singlecoin_d = {}  # 
    
    for c in coins:
        singlecoin_mask = [1 if coin==c else 0 for coin in coins]
        if c> money:    # cannot use one of this this coin
            continue
        elif c==money:  # one of this coin makes money amount exactly
                        # memoize and quit because this is already optimal
            memo[money] = singlecoin_mask
            return singlecoin_mask
        else:
            diff = money-c  #remaining amount after using 1 of coin c
            numcoins_diff = givechange(diff, coins, memo) #RECURSIVE CAL
            singlecoin_d[c] = [ a+b for a,b in zip(singlecoin_mask, numcoins_diff) ]
        
    # see which single coin did best 

    sortedcoins = sorted(singlecoin_d, key=lambda x:sum(singlecoin_d[x]) )
    # print("singlecoin_dict=", singlecoin_d)
    # print("sortedcoins results=", sortedcoins)
    
    # memoize the best one
    memo[money] = singlecoin_d[sortedcoins[0]]                
    #print("memo is now", memo) 
    return memo[money]       
        

    
    
def get_change(amount, verbose=False):
    #denominations = (20, 8, 1)
    denominations = (1, 3, 4)
    if verbose: print("coin denominations:", denominations)

    result = givechange(amount, denominations)

    if verbose: 
        print("amounts required are", result )
        print("number of coins=", sum(result) )
    return sum(result)



if __name__ == '__main__':
    m = int( input() )
    print(get_change(m))
