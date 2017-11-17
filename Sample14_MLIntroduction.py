# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:27:23 2017

@author: Sreenivas.J
"""

import os
import pandas as pd
from sklearn import tree
import io
import pydot #if we need to use any external .exe files.... Here we are using dot.exe

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

          
#returns current working directory
os.getcwd()
#changes working directory
os.chdir("D:\\Data Science\\")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()

X_titanic_train = titanic_train[['Pclass', 'Fare']]
y_titanic_train = titanic_train['Survived']

#build the decision tree model
dt = tree.DecisionTreeClassifier()
dt.fit(X_titanic_train, y_titanic_train)

#visualize the decission tree
dot_data = io.StringIO() 
#Pass, Decission Tree, and feture names
tree.export_graphviz(dt, out_file = dot_data, feature_names = X_titanic_train.columns)

graph = pydot.graph_from_dot_data(dot_data.getvalue()) #TypeError: 'Dot' object does not support indexing
graph.write_pdf("Ebix-DS-DT-Charan.pdf")

#predict the outcome using decision tree
titanic_test = pd.read_csv("test.csv")
X_test = titanic_test[['Pclass']]
titanic_test['Survived'] = dt.predict(X_test)
titanic_test.to_csv("submission.csv", columns=['PassengerId','Survived'], index=False)