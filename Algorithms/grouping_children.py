# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:38:59 2021

@author: Anna

organize children into the minimum number of groups such that 
the age of any two children in the same group differ by at most one year
"""
from random import randint 
     

class Age(object):
    def __init__(self, years, months):
        """
        years is an int between 0 and 
        """
        self.years = years
        self.months = months
        
        
    def __str__(self):
        return "{} years, {} months".format(self.years, self.months) 
    
    def get_months(self):
        """
        returns the years+months value converted all to months
        """
        return 12*self.years + self.months
    
    def get_diff(self, other):
         """
         returns difference (in months) between self and other age
         
         """
         gap = abs( self.get_months() - other.get_months() )
         
         return gap

        
        
class Party(object):
    def __init__(self, n):
        """
        n is a positive int, the number of children at the party
        """
        self.ages = self.rand_ages(n)
        self.months = [age.get_months() for age in self.ages]
        
    def __str__(self):
        s = "\n"
        for age in self.ages:
            s = s + str(age) +"\n"
            
        s += "\nin months:\n" + str(self.months)
        return s
        

    def rand_ages(self, n):
        """
        genereates n random ages between 
        0yrs 0 months and 17yrs 11 months
        returns a tuple of the age objects
        """
        ages = []
        for _ in range(n):
            yrs = randint(0,13)  #int returned is inclusive of endpoints
            mths = randint(0,11)
            ages.append( Age(yrs, mths) )
        
        return tuple(ages)
    
    def group_children(self):
        print( "\nchildren's ages are:", str(self) )
        
        sorted_ages = sorted(self.months)
        
        print( "\nsorted ages:", sorted_ages )

        groups = []
        current_group = []
        for age in sorted_ages:
            if len(current_group) > 0 and (age - current_group[0]) > 12:  #start new group
                print("completed group:", current_group, ".. max age diff=", current_group[-1]-current_group[0])
                groups.append(current_group[:])  # append a COPY of completed group   
                current_group = []
            current_group.append(age)
        print("last group:", current_group)
        groups.append(current_group)   
            
            
            
    
        