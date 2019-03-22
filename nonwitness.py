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
    2019-03-22:
        generated primes
        ryan learnded github
        hello
"""
import sys, rsa, random as rand

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
    test = 1
    
    #if more tests than there are available numbers...
    if(s > x-2):
        s = x-3
        
    #Test 2 first because it's common
    if( pow(2, x-1, x) == 1): #non-witness to compositeness
        nw = 2
    else: #witness to compositeness
        w = 2
    
    for test in range(2, s + 2): #run test s times
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
        #print("%d is probabilistically prime (certainty: %d)" % (x,s))
        return False
    elif(nw == -1 and w != -1): #purely composite
       # print("%d is purely composite" % x)
       return False
    else: #only considered non-witness if there are also witnesses...
        print("Count %d" % test)
        print("%d is composite" % x)
        print("\tWitnesses: %d" % w)
        print("\tNon-witnesses: %d" % nw)
        return True

def driver(nbits = 38):
    done = False
    test = 1
    
    while(not done):
        prime = abs(rand.getrandbits(nbits))
        done = non_witness_test(prime, 5)
    
###############################################################################
#########################      Tests       ####################################
###############################################################################    
#non_witness_test(5, 8) #should through error.. 
#non_witness_test(17, 5) #should be prime
#non_witness_test(15, 5) #should have non-witness
#non_witness_test(27534692908801, 50)
#non_witness_test(339772479099301, 50)

driver()

