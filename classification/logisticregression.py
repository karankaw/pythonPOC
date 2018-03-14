# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 08:53:39 2018

@author: 10635683
"""

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import sklearn


ds = pd.read_csv('..\\purchase_data.csv');

# Features

X = ds.iloc[:,2:4].values
Y = ds.iloc[:,4].values

print(X);
print(Y);



# Train test split

from sklearn.cross_validation import train_test_split

X_train , X_test  ,Y_train , Y_test = train_test_split(X,Y, test_size=0.25,random_state=0)

# Scale data
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
print("--------------------------------------")
print(X_train)
print(Y_train)
print("--------------------------------------")
print(X_test)
print(Y_test)
print("--------------------------------------")
X_train = sc.fit_transform(X_train);
X_test= sc.fit_transform(X_test)

print("After Transformation\n",X_train);
print("--------------------------------------")
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression();
classifier.fit(X_train,Y_train);


Y_pred = classifier.predict(X_test)
print(X_test)
print("Output\n",Y_pred)

help(StandardScaler)
