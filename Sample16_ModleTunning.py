# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:13:02 2017

@author: Saicharan.S
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:40:22 2017

@author: Sreenivas.J
"""

import pandas as pd
from sklearn import tree
from sklearn import model_selection
import io
import pydot
import os
#os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#returns current working directory
os.getcwd()
#changes working directory
os.chdir("D:/Data Science/")

titanic_train = pd.read_csv("train.csv")
print(type(titanic_train))


#EDA
titanic_train.shape
titanic_train.info()

#Apply one hot encoding
titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.info()
titanic_train1.head(6)
titanic_train1.describe()
X_train = titanic_train1.drop(['PassengerId','Age','Cabin','Ticket', 'Name','Survived'], 1)
y_train = titanic_train['Survived']

dt1 = tree.DecisionTreeClassifier()
#Apply K-fold technicque and find out the Cross Validation(CV) score.
cv_scores1 = model_selection.cross_val_score(dt1, X_train, y_train, cv=10)
print(cv_scores1) #Return type is a [List] of 10 scores.
print(cv_scores1.mean()) #Find out the mean of CV scores
dt1.fit(X_train,y_train)
print(dt1.score(X_train,y_train))

#tune model manually by passing differnt values for decision tree arguments
dt2 = tree.DecisionTreeClassifier(max_depth=8) #Here we passed max-depth as argument to the tree
cv_scores2 = model_selection.cross_val_score(dt2, X_train, y_train, cv=10)
print(cv_scores2.mean())
dt2.fit(X_train,y_train)
print(dt2.score(X_train,y_train))

#automate model tuning process. use grid search method
dt = tree.DecisionTreeClassifier()
param_grid = {'max_depth':[3,4,5,6,7,8,9,10], 'min_samples_split':[2,3,4,5,6,7,8,9,10,11,12]} 
print(param_grid)
#max_depth means: Max deapth of the tree to child nodes
#min_samples_split means: If you notice the tree nodes, there is some thing called sample in each node. This is what it is referring to min sample split
dt_grid = model_selection.GridSearchCV(dt, param_grid, cv=10, n_jobs=5)
dt_grid.fit(X_train, y_train)
print(dt_grid.grid_scores_)
final_model = dt_grid.best_estimator_ #This is the estimator of max_deapth and min_sample_split combination
print(dt_grid.best_score_)
print(dt_grid.score(X_train, y_train))


dot_data = io.StringIO() 
tree.export_graphviz(final_model, out_file = dot_data, feature_names = X_train.columns)
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0] 
graph.write_pdf("decisiont-tree-tuned12.pdf")