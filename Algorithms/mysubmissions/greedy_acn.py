# Uses python3
#import sys

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
        print("positions=", positions)
        print(" start at {} and reach {} with max step {}".format(start, destination, D) )
    
       
    ## find furthest stop you can reach
    reached = start
    for pos in positions[1:]:
        if pos-start <= D:
            reached = pos
        else:
            break
        
    # two base cases and one recursive call
    if reached == destination:
        print( "reached {} with {} refills at {}\n".format(reached, len(refills), refills ) )

    elif reached == start:     
        print("impossible, stuck at {} after refills at {}\n".format(start, refills) )

    else:
        i = positions.index(reached)        #reached an intermediate position, make that the new start
        remaining_positions = positions[i:] 
        refills.append(reached)             # append it to refills list
        min_refills(remaining_positions, D, refills)   #RECURSIVE CALL
        
    
        
    

            
def test():
    route = [0, 5, 7, 9, 12, 16]
    
    for D in range(3,18):
        min_refills(route, D)

if __name__ == "__main__":
#    input = sys.stdin.read()
    # a, b = map(int, input().split())
    # print(gcd(a, b))
    pass
