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
        self.coeffs = tuple(coeffs)  #store coeffs as a tuple
        
    def __str__(self):
        """
        returns a string representation of the polynomial, eg
        eg coeffs = [3 1 8]
        output = "3x**2 + x + 8"
        
        coeffs = [3, 0, 1]
        output = "3x**2 +1"
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
                term = term+"**"+str(degree) 
               
            # append the completed term to the polynomial with trailing plus
            poly_s = poly_s + term + " + "
            
        # eliminate trailing plus from last term
        if poly_s[-3:] == " + ":
            poly_s = poly_s[:-3]
            
        return poly_s
        
        
        
        

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

    MAX = 55
    coeffs = list( [random.randint(0, MAX) for i in range(n)]  )
    
    return coeffs

def test(n):
    coeffs = gen_coefficients(n)
    print("random coefficients are ", coeffs)
    
    show_polynomial(coeffs)
    
    ## test class
    print("\nnow test polynomial object")
    
    p = Polynomial(coeffs)
    print(p)
    
def show_polynomial(coeffs):
    """ coeffs is a list of ints which are the coefficients of 
        the polynomial, from highest term to zero degree term, prints
        a string of the corresponding polynomial
        eg coeffs = [3 1 8]
        output = "3x**2 + x + 8"
        
        coeffs = [3, 0, 1]
        output = "3x**2 +1"
        
    """
    assert len(coeffs) > 0   # there must be at least one coefficient

    degree = len(coeffs)    #highest degree +1
    poly_s = ""    # string representation of the polynomial
    
    for coeff in coeffs:
        degree -=1
        if coeff == 0:
            continue       #skip any term with zero coefficient
            
        term = "" #start compiling term for current coefficient

        if degree == 0 or coeff!=1:  #for zero degree term always show coeff
            term = str(coeff)        #for higher degree terms show it if it's not 1
            
        if degree > 0:
            term = term + "x"    #put in the x
        if degree > 1:
            term = term+"**"+str(degree) 
        poly_s = poly_s + term + " + "
        
    poly_s = poly_s[:-3]
        
    print(poly_s)
    