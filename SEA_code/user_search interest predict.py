#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:33:27 2020

@author: zobaed
"""

from mchain import MarkovChain
import sys
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding

data = "religion\nsports\nreligion\npolitics\nvehicle\nsports\nreligion\ntechnology\nsports\nreligion\nvehicle\nvehicle\nsports\nreligion\nsports\ntechnology\nsports\nreligion\nmedicine\npolitics\nreligion\nmedicine"   

data2=data.split("\n")

data2=data2[:-1]
def count(string):
    i=0
    for word in data:
        if word==string:
            i+=1
    return i

def seq(a,b):
    i=0
    for j in range(len(data2)-1):
        if(data2[j]==a and data2[j+1]==b):
            i+=1
    return i

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# create state space and initial state probabilities

states = ['religion', 'sports','technology','vehicle', 'politics', 'medicine']
pi = [0.3, 0.35, 0.15, .1, .05, .05]
state_space = pd.Series(pi, index=states, name='states')
print(state_space)
print(state_space.sum())

a=seq("religion", "religion")+seq("religion","sports")+seq("religion","technology")+seq("religion","vehicle")+ seq("religion","politics")+seq("religion","medicine")

b=seq("sports", "religion")+seq("sports","sports")+seq("sports","technology")+seq("sports","vehicle")+ seq("sports","politics")+seq("sports","medicine")
c=seq("technology", "religion")+seq("technology","sports")+seq("technology","technology")+seq("technology","vehicle")+ seq("technology","politics")+seq("technology","medicine")
d=seq("vehicle", "religion")+seq("vehicle","sports")+seq("vehicle","technology")+seq("vehicle","vehicle")+ seq("vehicle","politics")+seq("vehicle","medicine")
e=seq("politics", "religion")+seq("politics","sports")+seq("politics","technology")+seq("politics","vehicle")+ seq("politics","politics")+seq("politics","medicine")
f=seq("medicine", "religion")+seq("medicine","sports")+seq("medicine","technology")+seq("medicine","vehicle")+ seq("medicine","politics")+seq("medicine","medicine")


q_df = pd.DataFrame(columns=states, index=states)
q_df.loc[states[0]] = [seq("religion", "religion")/a, seq("religion","sports")/a, seq("religion","technology")/a, seq("religion","vehicle")/a, seq("religion","politics")/a, seq("religion","medicine")/a]
q_df.loc[states[1]] = [seq("sports", "religion")/b, seq("sports","sports")/b, seq("sports","technology")/b, seq("sports","vehicle")/b, seq("sports","politics")/b, seq("sports","medicine")/b]
q_df.loc[states[2]] = [seq("technology", "religion")/c, seq("technology","sports")/c, seq("technology","technology")/c, seq("technology","vehicle")/c, seq("technology","politics")/c, seq("technology","medicine")/c]
q_df.loc[states[3]] = [seq("vehicle", "religion")/d, seq("vehicle","sports")/d, seq("vehicle","technology")/d, seq("vehicle","vehicle")/d, seq("vehicle","politics")/d, seq("vehicle","medicine")/d]
q_df.loc[states[4]] = [seq("politics", "religion")/e, seq("politics","sports")/e, seq("politics","technology")/e, seq("politics","vehicle")/e, seq("politics","politics")/e, seq("politics","medicine")/e]
q_df.loc[states[5]] = [seq("medicine", "religion")/f, seq("medicine","sports")/f, seq("medicine","technology")/f, seq("medicine","vehicle")/f, seq("medicine","politics")/f, seq("medicine","medicine")/f]


form_chain = MarkovChain(transition_matrix=np.array(q_df.values).tolist(), states=states)
interest=form_chain.next_state(current_state='religion')
print(interest)