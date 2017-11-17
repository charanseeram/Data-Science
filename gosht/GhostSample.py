# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:21:58 2017

@author: Saicharan.S
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
os.chdir("D:\\Data Science\\gosht\\")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()

X_titanic_train = titanic_train[['bone_length', 'has_soul']]
y_titanic_train = titanic_train['type']

#build the decision tree model
dt = tree.DecisionTreeClassifier()
dt.fit(X_titanic_train, y_titanic_train)

#visualize the decission tree
dot_data = io.StringIO() 
#Pass, Decission Tree, and feture names
tree.export_graphviz(dt, out_file = dot_data, feature_names = X_titanic_train.columns)

graph = pydot.graph_from_dot_data(dot_data.getvalue()) #TypeError: 'Dot' object does not support indexing
graph.write_pdf("Ebix-DS-DT-Ghosts.pdf")

#predict the outcome using decision tree
titanic_test = pd.read_csv("test.csv")
X_test = titanic_test[['bone_length','has_soul']]
titanic_test['type'] = dt.predict(X_test)
titanic_test.to_csv("submissionGhosts.csv", columns=['id','type'], index=False)