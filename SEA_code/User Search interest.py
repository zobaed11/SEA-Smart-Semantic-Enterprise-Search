#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 04:01:50 2020

@author: zobaed
"""


from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_train_counts.shape
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape


from sklearn.model_selection import GridSearchCV
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],'tfidf__use_idf': (True, False),
              'clf-svm__alpha': (1e-2, 1e-3),
 }
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
text_clf_svm = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()), ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, max_iter=5, random_state=42))])
_ = text_clf_svm.fit(twenty_train.data, twenty_train.target)

from sklearn.model_selection import GridSearchCV
gs_clf = GridSearchCV(text_clf_svm, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(twenty_train.data, twenty_train.target)
gs_clf.best_score_


print(twenty_train.target_names)
text=["latest cloud technologies\n"]


interest=text_clf_svm.predict(text)
value=interest.tolist()


mod_target=twenty_train.target.copy() #20 to 7 label
mod_target_names=['religion','technology', 'vehicle', 'ecom', 'sports', 'medicine', 'politics']

mod_target=[]
for i in twenty_train.target:
    if (i==0 or i==15 or i==19):
        mod_target.append(0)
    elif (i==1 or i==2 or i==3 or i==4 or i==5 or i==11 or i==12 or i==14):
        mod_target.append(1)
    elif (i==6):
        mod_target.append(3)
    elif (i==7 or i==8):
        mod_target.append(2)
    elif (i==9 or i==10):
        mod_target.append(4)
    elif(i==13):
        mod_target.append(5)
    elif (i>=16 and i<=18):
        mod_target.append(6)
        
twenty_train.target=mod_target   
twenty_train.target_names=mod_target_names


     