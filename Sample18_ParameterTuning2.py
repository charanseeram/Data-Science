# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:20:34 2017

@author: Saicharan.S
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:21:50 2017

@author: Sreenivas.J
"""
import os
import pandas as pd
from sklearn import tree
from sklearn import model_selection
import io
import pydot

#returns current working directory
os.getcwd()
#changes working directory
os.chdir("D:/Data Science/")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()

titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.info()
titanic_train1.head(6)

X_train = titanic_train1.drop(['PassengerId','Age','Cabin','Ticket', 'Name', 'Survived'], 1)
y_train = titanic_train['Survived']

#automate model tuning process. use grid search method
dt = tree.DecisionTreeClassifier()
param_grid = {'criterion':['entropy'],'max_depth':[3,4,5,6,7,8,9,10], 'min_samples_split':[7,8,9,10,11,12]}
dt_grid = model_selection.GridSearchCV(dt, param_grid, cv=10, n_jobs=5)
dt_grid.fit(X_train, y_train)

#This gives the scores of all param_grid comibinations. 
dt_grid.grid_scores_
#Assign the best_estimator out of all
print(dt_grid.best_estimator_)
final_model = dt_grid.best_estimator_
dt_grid.best_score_ #Best score for the best parameters

dt_grid.score(X_train, y_train) #.Score is on the entire train data. 


dot_data = io.StringIO() 
tree.export_graphviz(final_model, out_file = dot_data, feature_names = X_train.columns)
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("decisiont-tree-tuned1.pdf")