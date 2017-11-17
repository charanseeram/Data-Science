# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:13:11 2017

@author: Saicharan.S
"""

import os
import pandas as pd
from sklearn.externals import joblib

#returns current working directory
os.getcwd()
#changes working directory
os.chdir("D:/Data Science/")
#predict the outcome using decision tree
titanic_test = pd.read_csv("test.csv")
titanic_test.Fare[titanic_test['Fare'].isnull()] = titanic_test['Fare'].mean()


titanic_test1 = pd.get_dummies(titanic_test, columns=['Pclass', 'Sex', 'Embarked'])
titanic_test1.shape
titanic_test1.info()
titanic_test1.head(6)

X_test = titanic_test1.drop(['PassengerId','Age','Cabin','Ticket', 'Name'], 1)

#Use load method to load Pickle file
dtree = joblib.load("tree1.pkl")
titanic_test['Survived'] = dtree.predict(X_test)
titanic_test.to_csv("submissionothermodel.csv", columns=['PassengerId','Survived'], index=False)