#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:50:55 2020

@author: zobaed
"""


import sys
import os
import numpy as np
dir="/home/zobaed/Downloads/All_bbc_together/"

allfiles = os.listdir( dir )


dic={}
wordlist= ['animal welfare', 'animal bill', 'animal act', 'animal welfare act', 'animal']

wordlist= ['windows', 'windows pc', 'operating system', 'computer', 'microsoft'] 

wordlist=['camera', 'camera phone', 'phone', 'videocamera', 'video', 'smartphone', 'television', 'image']

direct="/home/zobaed/Desktop/new_research/weighted query BBC/weighted_query_animal welfare bill.txt"
'''
wscore={}
with open(direct, 'r') as f:
    lines=f.readlines()
    for line in lines:
        l1=line[:line.index(':')]
        l2=line[line.index(':')+1:-1]
        l2=float(l2 )
        wscore[l1]=l2
        wordlist.append(l1)

'''

for i in allfiles:
    with open(dir+i, 'r', encoding="ISO-8859-1") as f:
        reader=f.readlines()
        lineholder=""
        for line in reader:
            lineholder+= " " +line
        lineholder=lineholder.lower()
        
      
        cnt=0
        for j in wordlist:
            if j in lineholder:
                cnt+=lineholder.count(j) #*wscore[j]

        
        if cnt>0:
            dic[i]=cnt
        
            

import operator

sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
        
        
sorted_dic.reverse()
all_val=[]
for key, val in sorted_dic:
    all_val.append(val)



mDict=sorted_dic[:40]
for i in mDict:
    # print(i)
    continue

with open('/home/zobaed/Desktop/new_research/weighted query BBC/kendra/res_Kendra-extended_encry_'+wordlist[1]+'.csv', 'w') as f:
    for i,k in mDict:
        i=i[:i.index('.')]
        f.write(i)
        f.write(', ')