# python3
#import sys
"""   Distance between the cities is 𝑑 miles, 
      Car can travel at most 𝑚 miles on full tank
      Gas stations at distances stop1, stop2, . . . ,stop𝑛 along the way
      
      Output the minimum number of refills needed. 
      Assume that the car starts with a full tank. 
      If it is not possible to reach the destination, output −1
"""

def compute_min_refills(distance, tank, stops):

    # write your code here
    return -1

def min_refills(positions, D, refills=None):
    """"
    positions is a list of ints where 
            positions[0] is the start
            positions[-1] is the destination
            and the intervening items are the positions of filling stations along the way.
        (all positions are expressed relative to the start position, and provided in order)
    
    D is the distance that can be covered with a single refill.
   
    refills stores the positions where refills were done, this list object is 
    passed to iterative calls which append their refill stops to it, so at the
    end it contains all the refill stops, and len(refill) is the minimum number
    of refills required 
            
    """
    start = positions[0]
    destination = positions[-1]
    
    # top level call, create new empty list
    if refills == None:
        refills = []
        #print the conditions of top-level call
        # print("positions=", positions)
        # print(" start at {} and reach {} with max step {}".format(start, destination, D) )
    
       
    ## find furthest stop you can reach
    reached = start
    for pos in positions[1:]:
        if pos-start <= D:
            reached = pos
        else:
            break
        
    # two base cases and one recursive call
    if reached == destination:
        # print( "reached {} with {} refills at {}\n".format(reached, len(refills), refills ) )
        return len(refills)

    elif reached == start:     
        # print("impossible, stuck at {} after refills at {}\n".format(start, refills) )
        return -1

    else:
        i = positions.index(reached)        #reached an intermediate position, make that the new start
        remaining_positions = positions[i:] 
        refills.append(reached)             # append it to refills list
        return( min_refills(remaining_positions, D, refills) )  #RECURSIVE CALL
        

if __name__ == '__main__':
    #d, m, _, *stops = map(int, input().split())
    #print(compute_min_refills(d, m, stops))

    d = int(input())   #distance between start and end cities
    m = int(input())   #miles car can cover on full tank
    _ = int(input())   # number of stops (we don't use this input)
    stops = list( map(int, input().split()) )  #intervening refill stops

    
    # add start and endpoints to stop list
    stops.insert(0, 0)
    stops.append(d)
    
   # print("stops list with endpoints", stops)
   
    print( min_refills(stops, m) )
        
    
    
