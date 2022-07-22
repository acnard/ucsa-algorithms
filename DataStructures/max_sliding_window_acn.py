# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:57:44 2022

@author: Anna
"""
import bisect

class SlidingQueue(object):
    def __init__(self, items):
        """ 
        items is a list of ints, the initial contents of the queue
        """
        
        self.m = len(items)
        self.queue = items[:]+[None]  # m items plus one head-tail spacer
        
        self.head = 0
        self.tail = self.m
        
        self.sorteditems = sorted(items)  #initial items sorted ascending
        
    def __str__(self):
        s = "queue: "
        s += str(self.queue)
       
        s = s+ "\nsorteditems:" + str(self.sorteditems)
        
        return s

    def max(self):
        """
        returns the maximum value in the queue
        
        """
        return self.sorteditems[-1]
        
    def slide(self, num):
        """
        slides the queue forward by dropping the head item
        and appending the int num to the back of the queue
        """
        # get current head item and remove it from sorted items
        val = self.queue[self.head]
        pos = bisect.bisect_left(self.sorteditems, val)  
        del self.sorteditems[pos]
        
        # on queue, drop the head item by advancing the pointer
        if self.head == self.m:   # the list has m items + 1 spacer, so when
            self.head = 0         # 0based index=m you're pointing to the 
        else:                     # last [-1] location in the list
            self.head+=1
        
        # on queue, write the new num in the current tail position
        self.queue[self.tail]=num
        
        # and increment the tail pointer
        if self.tail == self.m:
            self.tail = 0
        else:
            self.tail+=1
        self.queue[self.tail] = None  #just for clarity mark spacer location
        
        # insert the new num into the sorted items
        bisect.insort(self.sorteditems, num)
        
        
        
        

def sliding_window(nums, m):
    """
    nums is a list of ints
    n is an int, the number of ints in the list nums
    m is an int <= n, size of the sliding window
    
    generates all the sliding windows with m items
    """
    #print("nums:", nums)    
    
    n = len(nums)
    assert m<= n
    
    ## initialize window with first m items
    window = SlidingQueue(nums[:m])
    print(window.max(), end=" ")
    
    for i in range(n-m):
        window.slide(nums[i+m])

        print(window.max(), end=" ")
        
    



def main():
    """
    The first line contains an integer 𝑛, 
    the second line contains 𝑛 integers 𝑎1, . . . , 𝑎𝑛 separated
    by spaces, the third line contains an integer 𝑚
    """
    n = int( input( )) # not used

    nums = [int(s) for s in input().split() ]
    #print(nums)
    
    m = int( input() )
    
    sliding_window(nums, m)
    
    


if __name__ == "__main__":
    #pass
    main()