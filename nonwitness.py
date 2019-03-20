# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:47:31 2019

@class: ECE 3790
@prof: Bob McLeod

@author: Eric Kapilik [7807969] & Ryan Shaski [0000000]

@history:
    2019-03-20:
        wrote non_witness_test function
        added simple tests
"""
import sys, random as rand

###############################################################################
"""
Description
Test if x is prime s times.
-- Miller-Rabin algorithm

PARAMETERS
    x: the number to test
    s: certainty 

RETURNS:
    True if x has non-witness, false otherwise.
"""
def non_witness_test(x, s):
    nw = -1
    w = -1
    tested = []
    
    if(s > x-2):
        print("ERROR: Certainty is greater than x-2")
        return False
    
    for test in range(s): #run test s times
        a = rand.randint(2, x-2) # select from Z+*
        while(tested.count(a) != 0): #get unique a
            a = rand.randint(2, x-2) # select from Z+*
        tested.append(a)
        
        if( pow(a, x-1, x) == 1): #non-witness to compositeness
            nw = a
        else: #witness to compositeness
            w = a
            
        if(w != -1 and nw != -1):
            break
    
    if(nw != -1 and w == -1):
        print("%d is probabilistically prime (certainty: %d)" % (x,s))
        return False
    else: #only considered non-witness if there are also witnesses...
        print("%d is composite" % x)
        print("\tWitnesses: %d" % w)
        print("\tNon-witnesses: %d" % nw)
        return True
        
###############################################################################
#########################      Tests       ####################################
###############################################################################    
non_witness_test(5, 8) #should through error.. 
non_witness_test(17, 5) #should be prime
non_witness_test(15, 5) #should have non-witness