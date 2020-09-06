#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:55:01 2019

@author: zobaed
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np






fig = plt.figure(figsize=(8,4.5))
ax  = fig.add_subplot(111)
# ax.set_position([0.15,0.15,0.6,0.83])
# ind = np.arange(3)


ax.bar(0.0 ,1.0, color='lightsteelblue', edgecolor='white', label='S3BD')
ax.bar(0.0 ,1.0, color='burlywood', edgecolor='white', label='Kendra')
ax.bar(0.0 ,1.0, color='salmon', edgecolor="white" ,label='SEA+S3BD')
ax.bar(0.0 ,1.0, color='limegreen', edgecolor='white', label='SEA+Kendra')
ax.bar(0.0 ,0.1, color='white',edgecolor='white', alpha=1)
                
                 
                
edgecols=['magenta','orange','royalsalmon','forestgreen','red','mediumsalmon','limegreen','lightsalmon','limegreen'] #prepared 9 colors                




bbc_kendra=[2.2,1.8, 2.3,1.9, 2.4, 1.9,2.2, 2.1, 1.8,2.3  ]



bbc_s3bd=(7,7.5, 8.3,8.5,7.3,6.8,7.7,7.1,7.8,11)

bbc_ss3bd=(4.6,5.7, 6,6.4,6.9,5.3,5.8,5.9,6.5,5.9,6.1)

bbc_skendra=[4.1,3.7, 4,3.2, 3.4, 3.2,4.1, 3.1, 2.8,3.6 ]




rfc_kendra=[2.3,2.5, 2.5,1.7, 2.2, 1.7,2.4, 2.3, 2.1,2.4  ]

rfc_s3bd=(7.5,8.8, 8.9,9.5,8.5,6.8,8.1,7.9,8.6,7.9)
rfc_ss3bd=(5.6,6.3, 6.5,6.8,7.1,6.56,6.9,6.65,6.72,6.95,7.13)

rfc_skendra=[4.3,4.17, 4.1,3.3, 3.2, 3.8,4.3, 3.5, 2.9,3.7 ]

bbc_kendra=[i*1000 for i in bbc_kendra]
bbc_s3bd=[i*1000 for i in bbc_s3bd]
bbc_skendra=[(i+6.2)*1000 for i in bbc_skendra]
bbc_ss3bd=[i*1000 for i in bbc_ss3bd]
rfc_kendra=[i*1000 for i in rfc_kendra]
rfc_s3bd=[i*1000 for i in rfc_s3bd]
rfc_skendra=[(i+6.8)*1000 for i in rfc_skendra]
rfc_ss3bd=[i*1000 for i in rfc_ss3bd]
# aws=(7,9,15, 13, 11,9,16,4,7,11,7)

# aws_prev=(16,23,13,9,6,12,25,15,14,9)

data_to_plot=[bbc_s3bd, bbc_kendra,bbc_ss3bd, bbc_skendra, rfc_s3bd, rfc_kendra,rfc_ss3bd, rfc_skendra]

label=["Kendra", "S3BD", "SEA+S3BD", "SEA+Kendra","Kendra", "S3BD", "SEA+S3BD", "SEA+Kendra",]
box=ax.boxplot(positions=[0, 1,2,3,6,7,8,9],x=data_to_plot,patch_artist=True,medianprops=dict(color="black"),labels=label)
colors = ['lightsteelblue','burlywood', 'salmon','limegreen', 'lightsteelblue','burlywood','salmon','limegreen']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    



plt.ylabel('Search Time (ms)', fontsize=18)

my_xsticks=['BBC', 'RFC']
ka=np.array([1.5,7.5])
plt.xticks(ka, my_xsticks, fontsize=17)
plt.yticks(fontsize=17)


ax.legend( bbox_to_anchor=(.32, .42), loc=2, borderaxespad=0., fontsize=11)

fig.set_size_inches(6, 4, forward=True)
#plt.tight_layout()

#fig.savefig("Pro_en_box.pdf")

fig.savefig('SearchTime-S3BDvsSea.pdf',bbox_inches='tight', pad_inches=.05)
plt.show()