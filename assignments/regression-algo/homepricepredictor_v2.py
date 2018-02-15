# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:40:06 2018

@author: 10635683
"""

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import sklearn
import pylab as pl

# Create an imputer

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

#Import data set
full_dataset = pd.read_csv( "D:\\Python-WS\\practice-examples-3\\train.csv" , nrows = 100 );

#print(full_dataset);

# Consider a smaller dataset
considered_dataset = full_dataset.iloc[:,1:6]
print( considered_dataset );


# Imputer
considered_dataset['MSSubClass'].fillna((considered_dataset['MSSubClass'].mean()), inplace=True)
considered_dataset['LotFrontage'].fillna((considered_dataset['LotFrontage'].mean()), inplace=True)
considered_dataset['LotArea'].fillna((considered_dataset['LotArea'].mean()), inplace=True)
#print( considered_dataset );

# One hot encoder

cols_to_transform = [ 'MSZoning' , 'Street' ]
df_with_dummies = pd.get_dummies( considered_dataset , columns = cols_to_transform )

print(df_with_dummies);
Y = full_dataset.iloc[:,80:81].values
#print(Y)

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( df_with_dummies , Y , test_size=0.2, random_state=0);

from sklearn.linear_model import LinearRegression
regressor = LinearRegression();

regressor.fit(X_train , Y_train);

y_pred = regressor.predict(X_test);

