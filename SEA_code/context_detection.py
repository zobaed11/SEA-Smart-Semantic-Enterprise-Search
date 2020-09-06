#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:53:55 2020

@author: zobaed
"""

import nltk
from pywsd.lesk import simple_lesk
import yake
import numpy as np
import os
import sys
import enchant
engcheker=enchant.Dict("en_US")
sent = 'I water the plants'

kw_extractor = yake.KeywordExtractor(lan="en", n=2, windowsSize=2, top=3)
keywords = kw_extractor.extract_keywords(sent)
imp_key=[]
for i in enumerate(keywords):
    imp_key.append(i[1][1])

raw_tokens=nltk.word_tokenize(sent)


pos2=nltk.pos_tag(raw_tokens)

pa=["JJ", "JJR", "JJS"]
pn=["NNS", "NNP", "NNPS", "NN", "FW"]
pv=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
pav=["RB", "RBR", "RBS"]
imp_pos=[]
for i in enumerate(pos2):
    if (i[1][0] in imp_key):
        if (i[1][1] in pn):
            imp_pos.append("n")    
        elif (i[1][1] in pa):
            imp_pos.append("a")
        elif (i[1][1] in pv):
            imp_pos.append("v")        
        elif (i[1][1] in pav):
            imp_pos.append("r")
        else:
            imp_pos="none"
            

imp_synset_definition=[]
for i in range(len(imp_key)):
    imp_synset_definition.append(simple_lesk(sent, imp_key[i],pos=imp_pos[i]).definition())

kw_extractor = yake.KeywordExtractor(lan="en", n=2, windowsSize=2, top=3)    
imp_key_from_definition=[]
for i in range(len(imp_key)):
    a=kw_extractor.extract_keywords(imp_synset_definition[i])
    for j in range(len (a)):
        imp_key_from_definition.append(a[j][1])



'''
Weight Distribution 
'''

all_expanded=[]
weighted_keywords={}

all_expanded=imp_key+imp_key_from_definition



non_dict_words=[]
for k in all_expanded: 
    if engcheker.check(k)== False:
        
        weighted_keywords.update({k:1})
        non_dict_words.append(k)

dict_words=[]        
      
dict_words = list(set(all_expanded).difference(set(non_dict_words)))

'''
i have segregarted dict word and non dict word. I have waited non dict word as 1. I need to calculate weight for dict words..
Then the weighting part will be done.. Oh, I need to calculate weight based on user's next search. 

'''

weighted_dict={}

search_interest="technology"
import gensim 
model = gensim.models.KeyedVectors.load_word2vec_format('/home/zobaed/Downloads/GoogleNews-vectors-negative300.bin', binary=True)



