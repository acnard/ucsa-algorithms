# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:43:40 2022

@author: Anna


Input Format. Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
marks and brackets from the set []{}().
Constraints. The length of 𝑆 is at least 1 and at most 105
.
Output Format. If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
brackets, output the 1-based index of the first unmatched opening bracket.
"""

def checkbrackets(s):
    """
    s is a string, in which we want to check that brackets are closed
    correctly
    """
    
    matches = {']':'[', ')':'(', '}':'{'
             }
    
    openers = []
    
    for i in range(len(s)):
        ch = s[i]
        ## opener : just append
        if ch in "[{(":
            openers.append( ( ch, i ) )
        ## closer: must match last opener
        elif ch in "]})":     
            if len(openers)==0 or matches[ch]!=openers.pop()[0] : 
                #print("unmatched closer", ch)
                return i+1       #one-based index of first unmatched closing bracket
            
            ## nb if there was a match you will have already removed
            ## the corresponding opener in the pop() of the no match test

    ## every closer found a match, now openers list should be empty
    if len(openers) > 0:
        #print("residual openers", openers)
        return openers[0][1]+1 #one-based index of first unmatched opening bracket          
            
    return("Success")            
    
    
def main():
    text = input()
    print( checkbrackets(text) )
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
    