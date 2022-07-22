# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:14:17 2021

@author: Anna
"""
import random

class Polynomial(object):
    def __init__(self, coeffs):
        """
        coeffs is a sequence (list or tuple) of ints which are the coefficients of 
        the polynomial, from highest term to zero degree term,
        any missing terms must have 0 coefficient
        """
        
        ## helper function to strip leading zeros from 
        ## the passed coefficients before storing
        def stripzeros(seq):
            """
            coeffs is a sequence of integer coefficients (list or tuple)
            returns the list of coefficient minus any leading zeros
            """
            coefficients = list(seq)
            
            #nb do not iterate over list from which we are removing zeros
            for c in seq:
                if c!=0:
                    break #stop as soon as leftmost nonzero coefficient found
                else:
                    coefficients.remove(c)
                    
            return coefficients
        
        self.coeffs = tuple(stripzeros(coeffs))  #store coeffs as a tuple
        

        
    def __str__(self):
        """
        returns a string representation of the polynomial,followed by 
        its list of coefficients on the next line, eg
        "3x**2 + x + 8
          (3, 1, 8)"
        
        "3x**2 +1
          (3, 0, 1) "
        """

        poly_s = ""    # string representation of the polynomial
        
        degree = len(self.coeffs)    #highest degree +1
        for coeff in self.coeffs:
            degree -=1
            if coeff == 0:
                continue       #skip any term with zero coefficient
                
            term = "" #start compiling term for current coefficient

            if degree == 0 or coeff!=1:  #for zero degree term always show coeff
                term = str(coeff)        #for higher degree terms show it if it's not 1
                
            if degree > 0:
                term = term + "x"    #put in the x
            if degree > 1:
                term = term+"^"+str(degree) 
               
            # append the completed term to the polynomial with trailing plus
            poly_s = poly_s + term + " + "
            
        # eliminate trailing plus from last term
        if poly_s[-3:] == " + ":
            poly_s = poly_s[:-3]
            
        # now append the list of coefficients on a new line
        poly_s = poly_s + "\n   " + str(self.coeffs)
        
        return poly_s
        

        
    def getdegree(self):
        """
        returns the degree of the polynomial self, taking into account that
        there may be some leading zero coefficients, so the degree of the 
        polynomial is not necessarily len(coeffs)-1
        """
        return len(self.coeffs) - 1
    
        
    def split(self):
        """
        splits the polynomial self P into two halves (P1, P2) such that
        P = P1 + P2 
        
        if P cannot be evenly split, P2 (the lower degree part) gets
        the one extra term
        
        eg x**2 + 3x + 5 = (x**2)  + (3x + 5)
           x**3 + 5x**2 + x + 7 = (x**3 + 5x**2)  + (x + 7)
        """
        assert self.getdegree() >= 2   #polynomial at least degree 2 to split
        
        ## we want to split the coefficients up at [:midpoint] and [midpoint:]
        ## and pad the higher degree (left) half appropriately
        ## eg if length is 4 midpoint is 2 and array is split [a,b,-,-] and [c,d]
        ## if length is 5 midpoint is 2 and array is split [a,b,-,-,- ] and [c,d,e]
       
        midpoint = len(self.coeffs) // 2
        coefficients = list(self.coeffs)
        
        right_coeffs = coefficients[midpoint:] 
        left_coeffs = coefficients[:midpoint] + [0]*(len(right_coeffs)) 
        
        pleft = Polynomial(left_coeffs)
        pright = Polynomial(right_coeffs)
        
        print("\n ** test splitting ** \n")
        print( "the polynomial\n {} \n was split into:\n".format(self))
        print(" pleft = {} \n and \n pright = {}\n".format(pleft, pright) )
        print("the lowest power of pleft is", pleft.get_lowest_power())
        print("the lowest power of pright is", pright.get_lowest_power())
        
        print("\n ** test factoring of pleft\n" )
        pleft.factor_out_x()
        
        
    def get_lowest_power(self):
        """
        returns the lowest power of x in the polynomial self, eg
        3x^2 + 3x  returns 1 (x to the 1st is lowest power)
         3x^2 +3x +4 returns 0
         3x^9 + 3x^3 returns 3, etc.
        """
        assert len(self.coeffs) > 0
        
        coefficients = self.coeffs
        #scan coefficients from right to left to find first nonzero one
        
        for i in range( len(coefficients)-1, -1, -1 ):
            if coefficients[i] != 0:
                return self.getdegree() - i
            
        #will get here only if the coefficient list is empty
        # (this can happen on creating a polynomial with all coefficients zero)
        print ("could not find lowest power of x")
        
    def factor_out_x(self):
        """
        factors out x from the polynomial self, eg
        3x^2 + 3x  factors out x to get (x) * (3x +3)
         3x^2 +3x +4 doesn't factor out anything
         3x^9 + 3x^3 factors out x^3 to get (x^3) * (3x^6 + 3)
         
        this corresonds to just removing all the trailing (rightmost) zero
        coefficients to reduce the degree of the polynomial
        """
        assert len(self.coeffs) > 0
        
        print("am factoring", self)
        
        coefficients = self.coeffs
        #scan coefficients from right to left to find first nonzero one
        
        for i in range( len(coefficients)-1, -1, -1 ):
            if coefficients[i] != 0:
                break
            
        pow_x = self.getdegree() - i  # the power of x that can be factored out
        print("can factor out x^{}".format(pow_x) )
        
        factored_coeffs = coefficients[:i+1] #slice to exclude trailing zeros
        f_poly = Polynomial(factored_coeffs)
        print("the factored polynomial is", f_poly)       

        

        

def get_polynomials():
    poly1 = input("enter first polynomial coefficients: ")
    poly2 = input ("enter second polynomial coefficients: ")
    
    poly1 = list( map( int, poly1.split() ) )
    poly2 = list( map( int, poly2.split() ) )
    
    print(poly1)
    print(poly2)
    
def gen_coefficients(n):
    """
    generates a list of n random coefficients for a polynomial
    """
    # generate a list of n random nonegative integers

    MAX = 4
    coeffs = list( [random.randint(0, MAX) for i in range(n)]  )
    
    return coeffs

def test(n):
    coeffs = gen_coefficients(n)
    print("random coefficients are ", coeffs)
    
    
    ## test class
    print("\nnow test polynomial object")
    
    p = Polynomial(coeffs)
    print(p)
    
    # test stripping & getdegree
    print("\n polynomial degree =", p.getdegree())
    
    # test splitting
    p.split()
    
    
    
