#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:19:10 2020

@author: zobaed
"""

lis=[1,1,1,1,1,1,1,0,0,0]
high_rel=0
for i in range (len(lis)):
    
    if (lis[i] == 1):
        high_rel+=1/(i+1)
    
    if (lis[i] == 2):
        high_rel+=1/(2*(i+1))
    
    if (lis[i] == 3):
        high_rel+=0
        

tsap=high_rel/10

print (tsap)
    
    
        
        