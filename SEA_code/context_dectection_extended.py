#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:52:57 2020

@author: zobaed
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:53:55 2020

@author: zobaed
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
from pywsd.lesk import simple_lesk
from nltk.corpus import wordnet
import yake
import numpy as np
import os
import sys
import enchant
engcheker=enchant.Dict("en_US")
sent = "opera in vienna"
stop_words = set(stopwords.words('english')) 


def query_expansion(token_query):
    synonyms=[]
    for syn in wordnet.synsets(token_query): 
        for l in syn.lemmas():
            if l.name() not in synonyms:
                synonyms.append(l.name())
    # synonyms.append(len(synonyms))
    return synonyms
        
        


full_token_query=[]
for r in sent.lower().split(" "): 
    if not r in stop_words:
        full_token_query.append(r)
        
        
        
'''    Expansion         '''
synonyms_dict={}
for word in full_token_query:
    if engcheker.check(word) == True:
        synonyms=[]
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas():
                if l.name() not in synonyms:
                    synonyms.append(l.name())
        # synonyms.append(len(synonyms))
        synonyms_dict[word]=synonyms
       
    
    

kw_extractor = yake.KeywordExtractor(lan="en", n=1, windowsSize=2, top=5)



keywords = kw_extractor.extract_keywords(sent)
imp_key=[]
non_dict_words=[]
for i in enumerate(keywords):
    if engcheker.check(i[1][1]) ==True: 
        imp_key.append(i[1][1])
    else: 
       # s=i[1][1][0].upper()+ i[1][1][1:]  #european is false but European is True. 
       # if (engcheker.check(s) == True):
        #    imp_key.append(i[1][1])
        #else: 
        non_dict_words.append(i[1][1])
        
        "CHECK FROM NEXT..... "
        
'''       
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
            imp_pos.append("none")
            
'''
imp_synset_definition=[]
for i in range(len(imp_key)):
    # imp_synset_definition.append(simple_lesk(sent, imp_key[i],pos=imp_pos[i]).definition())
    imp_synset_definition.append(simple_lesk(sent, imp_key[i],pos= None).definition())
    



dic_for_context={}
kw_extractor = yake.KeywordExtractor(lan="en", n=1, windowsSize=2, top=10)    
imp_key_from_definition=[]
for i in range(len(imp_key)):
    temp=[]
    a=kw_extractor.extract_keywords(imp_synset_definition[i])
    for j in range(len (a)):
        imp_key_from_definition.append(a[j][1])
        temp.append(a[j][1])
    dic_for_context[imp_key[i]]=temp


'''
Weight Distribution 
'''




'''
ekhane shudhu query word thakbe.. bakira bad 
'''
context=[]
context=imp_key_from_definition

''' weight given to context by number of context, no of words in each context
'''

weight_context={}
no_of_context=len(imp_key)
for key, w in dic_for_context.items():
    for ww in w:
        if len(ww)==1 and engcheker.check(ww) == False:
            weight_context[ww]=1            
        else:
            # weight_context[ww]=(1/no_of_context)*(1/len(w))
            weight_context[ww]=(1/len(w))

    



weighted_keywords={}


for i in imp_key:
    weighted_keywords[i]=.0001

for i in non_dict_words:
    weighted_keywords[i]=1

weighted_keywords[sent]=1

'''
i have segregarted dict word and non dict word. I have weighted non dict word as 1. I need to calculate weight for dict words..
Then the weighting part will be done.. Oh, I need to calculate weight based on user's next search. 

'''

weighted_dict={}

search_interest="technology"
import gensim 
model = gensim.models.KeyedVectors.load_word2vec_format('/home/zobaed/Downloads/GoogleNews-vectors-negative300.bin', binary=True)




dict_score_context={}

avg_score_keeper=[]
for qw, eqw in synonyms_dict.items():
    sum_score_expanded_query_words=[]
    for eachword in eqw:
        l=0
        for conw in context:
            # print(eachword, conw)
            try:
                l+=model.similarity(eachword, conw)
                
            except:
                l+=0
        sum_score_expanded_query_words.append(l)
        
    avg_score_keeper.append(sum(sum_score_expanded_query_words)/len(sum_score_expanded_query_words)  )        
    dict_score_context[qw]=sum_score_expanded_query_words
    
purified_synonyms_dict={}    
i=-1    
for key, score in dict_score_context.items():
    i+=1 
    la=[]
    for s in score:
        if (s>=avg_score_keeper[i]):
             
            a=score.index(s)
            print(synonyms_dict[key][a])
            la.append(synonyms_dict[key][a])
    purified_synonyms_dict[key]=la 
    
total_extended_words_for_each_query_word=[]    
for key, li in purified_synonyms_dict.items():
    i=len(li)
    total_extended_words_for_each_query_word.append(i)
    
i=0

#####
'''
weight_expanded_query={}
for key,li in purified_synonyms_dict.items():
    temp=[]
    n=len(li)
    print (n)
    for w in li:
        sim_score=model.similarity(w,search_interest)    
        
        temp.append(sim_score*1/n)
        #temp.append(sim_score)
        
    weight_expanded_query[key]=temp
'''
'''CHECK this Portion'''
#####

new_weight_expanded_query={}
for key,li in purified_synonyms_dict.items():

    for w in li:
        sim_score=model.similarity(w,search_interest)    
        
        #temp.append(sim_score*1/n)
        new_weight_expanded_query[w]=sim_score  #without normalization       
#####


    
'''  

all_purified_together=[]
for key, ll in purified_synonyms_dict.items():

    
    for l in ll:
        all_purified_together.append(l)


all_purified_together_extended_query_weight={}

j=0
for i,val in weight_expanded_query.items():
    for v in val:
        all_purified_together_extended_query_weight[all_purified_together[j]]=v
        j+=1
      
'''

combined_dict={}
combined_dict_temp={}
#combined_dict_temp = {**weighted_keywords, **all_purified_together_extended_query_weight}
combined_dict_temp = {** new_weight_expanded_query,**weighted_keywords,}
combined_dict={**combined_dict_temp, **weight_context}

'''For Java Program'''
ac=str(combined_dict)
acc=ac.split(",")
f = open("/home/zobaed/Desktop/new_research/weighted query BBC/weighted_query_" +sent+ ".txt","w")

for i in acc:
    if ',' in i:
        i=i.replace(',', '')

    if '{' in i:
        i=i.replace("{", '')

    if ("}" in i):
        i=i.replace("}", '')

    if ("'" in i):
        i=i.replace("'", '')

    if (" " in i[0] ):
        i=i[1:]


    if (" " in i[i.index(":")+1] ):
        i1=i[: i.index(":")+1]
        i2=i[i.index(":")+1 :]
        i=i1+i2

        
    if ("-" in i):
        i=i.replace("-", "")


    f.write(i)
    print(i)
    f.write("\n")

f.close()

combined_words=[]
combined_weight=[]
for key, l in combined_dict.items():
    combined_words.append(key)
    combined_weight.append(l)  
      
with open("/home/zobaed/Desktop/new_research/weighted query BBC/kendra/"+"kendra_equery_" +sent+ ".txt","w") as f:
    for word in combined_words:
        f.write(word)
        f.write("\n")
    f.close()
        
