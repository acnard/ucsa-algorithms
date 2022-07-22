# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:17:15 2022

@author: Anna
"""

class Buffer(object):
    def __init__(self, size):
        """
        size is an int, the number of packets that the buffer can hold
        
        """
        self.size = size  # number of packets the buffer can store
        
        self.packets = [None]*(size+1)  # list of packets awaiting processing
                                        # for each packet we just store an int, 
                                        # its finish time, in a circular list

        # for a circular queue we have to leave one empty slot between 
        # the head and the tail, hence allocate size+1
        self.head = 0
        self.tail = 0
        
    def is_empty(self):
        """
        returns True if queue is empty (head pointer = tail pointer)
        """
        if self.head == self.tail:
            return True
        else:
            return False
        
    def is_full(self):
        """ returns True if the queue is full 
        (tail pointer at empty spacer between it and head pointer)
        """
        
        if (self.tail - self.head == self.size) or (self.head - self.tail == 1):
            return True
        else:
            return False
        
    def inc_tail(self):
        """
        increment the tail pointer, taking into account the buffer size
        you would do this after appending an item to the end of the queue
        """
        assert self.size >= 1   # buffer must hold at least one packet
                                # note that the list is always size+1 items
                                # to allow for the spacer
                                
        assert not self.is_full()  #check that didn't try to increment tail
                                   #when queue already full. ie tail pointer
                                   # should not already be at spacer
        
        
                    
        if self.tail == self.size: # the list has size+1 items, so when
            self.tail = 0          # 0based index=size you're pointing to the 
        else:                      # last item in the list
            self.tail+=1
            
            
    def inc_head(self):
        """
        increment the head pointer, taking into account the buffer size
        you would do this to pop an item from the head of the queue
        """
        assert self.size >= 1   # buffer must hold at least one packet
                                # note that the list is always size+1 items
                                # to allow for the spacer
                                
        assert not self.is_empty() #check that didn't try to increment head
                                   #when queue empty as that would let the
                                   # head overtake the tail
        
        
                    
        if self.head == self.size: # the list has size+1 items, so when
            self.head = 0          # 0based index=size you're pointing to the 
        else:                      # last item in the list
            self.head+=1
                                              
                                  
    def show_queue(self):
        
        print("raw packets list:", self.packets)
        
        print("head pos = ", self.head)
        print("tail pos = ", self.tail)
        
        print("head <------------< tail")
        if(self.tail >= self.head):
            print( self.packets[self.head:self.tail])
            
        else:
            print( self.packets[self.head:] + self.packets[:self.tail] )
        
        
    def enqeue_packet(self, arrivaltime, processingtime):
        """
        arrivaltime and processing time are ints, respectively when the 
        packet was received and how long it will take to process it
        """

        # starting from head of queue, dump any packets whose finish 
        # time <= the new packet's arrival time. To dump a packet you just
        # increment the head pointer
        while not self.is_empty() and self.packets[self.head] <= arrivaltime:
            self.inc_head()

        # if at this point the buffer is still full we can't add the packet                   
        if self.is_full():
            return -1         #packet dropped
        

        # Otherwise figure out when you will start to process this packet
        if self.is_empty():
            start_time = arrivaltime
        else:
            start_time = self.packets[self.tail - 1]  # previous packet finish time
            
            
        # And in the buffer append the new packet's finish time    
        self.packets[self.tail] = start_time + processingtime
        self.inc_tail()
        
        return start_time  # return when you start processing the packet
        
        
        
                
def test(n):
    print("test set, create a buffer of size", n)
           
    bf = Buffer(8)
        
        



def main():
    """
    The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming
    network packets. Each of the next 𝑛 lines contains two numbers. 𝑖-th line contains the time of arrival
    𝐴𝑖 and the processing time 𝑃𝑖 (both in milliseconds) of the 𝑖-th packet. It is guaranteed that the
    sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in
    milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).
    """
    firstline = input()
    firstline = firstline.split()
    
    buffersize = int(firstline[0])
    numpackets = int(firstline[1])
    
   # print("number of packets:", numpackets)
    
    bf = Buffer(buffersize)
   
    for i in range(numpackets):
        packet = input()  # string "Ai Pi"
        packet = packet.split()  # list ["Ai", "Pi"]
        
        arrivaltime = int(packet[0])
        processingtime = int(packet[1])    
        
        print( bf.enqeue_packet(arrivaltime, processingtime) )
              



if __name__ == "__main__":
    #pass
    main()