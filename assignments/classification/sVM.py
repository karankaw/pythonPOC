# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:09:04 2018

@author: 10635683
"""

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import sklearn


ds = pd.read_csv('D:\\Python-WS\\recommendersystem\\purchase_data.csv');

# Features

X = ds.iloc[:,2:4].values
Y = ds.iloc[:,4].values

print(X);
print(Y);


from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train , Y_test = train_test_split(X,Y,test_size=0.33,random_state=1);

from sklearn.svm import SVC
svc = SVC( kernel='poly' , random_state=0);
# Fit
svc.fit(X_train,Y_train);
# Predict
y_pred = svc.predict(X_test);

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred,Y_test);



