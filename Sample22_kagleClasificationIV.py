# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:26:02 2017

@author: Saicharan.S
"""

#Refer to 14.feature creation-->feature-creation - FE, EDA
#These 2 are hand in hand programs

import pandas as pd
import os
from sklearn import preprocessing
from sklearn import tree
from sklearn import model_selection

#changes working directory
os.chdir("D:/Data Science")

titanic_train = pd.read_csv("train.csv")
titanic_train.shape
titanic_train.info()

titanic_test = pd.read_csv('test.csv')
titanic_test.shape
titanic_test.info()

titanic_test.Survived = None

#Let's excercise by concatinating both train and test data
#Concatenation is Bcoz to have same number of rows and columns so that our job will be easy
titanic = pd.concat([titanic_train, titanic_test])
titanic.shape
titanic.info()

#Extract and create title column from name
def extract_title(name):
     return name.split(',')[1].split('.')[0].strip()
#The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object 
#and returns a list containing all the function call results.
titanic['Title'] = titanic['Name'].map(extract_title)

mean_imputer = preprocessing.Imputer() #By defalut parameter is mean and let it use default one.
mean_imputer.fit(titanic_train[['Age','Fare']]) 
#Age is missing in both train and test data.
#Fare is NOT missing in train data but missing test data. Since we are playing on tatanic union data, we are applying mean imputer on Fare as well..
titanic[['Age','Fare']] = mean_imputer.transform(titanic[['Age','Fare']])

#creaate categorical age column from age
#It's always a good practice to create functions so that the same can be applied on test data as well
def convert_age(age):
    if(age >= 0 and age <= 10): 
        return 'Child'
    elif(age <= 25): 
        return 'Young'
    elif(age <= 50): 
        return 'Middle'
    else: 
        return 'Old'
#Convert numerical Age column to categorical Age1 column
titanic['Age1'] = titanic['Age'].map(convert_age)

#Create a new column FamilySize by combining SibSp and Parch and seee we get any additioanl pattern recognition than individual
titanic['FamilySize'] = titanic['SibSp'] +  titanic['Parch'] + 1
def convert_familysize(size):
    if(size == 1): 
        return 'Single'
    elif(size <=3): 
        return 'Small'
    elif(size <= 6): 
        return 'Medium'
    else: 
        return 'Large'
#Convert numerical FamilySize column to categorical FamilySize1 column
titanic['FamilySize1'] = titanic['FamilySize'].map(convert_familysize)

#Now we got 3 new columns, Title, Age1, FamilySize1
#convert categorical columns to one-hot encoded columns including  newly created 3 categorical columns
#There is no other choice to convert categorical columns to get_dummies in Python
titanic1 = pd.get_dummies(titanic, columns=['Sex','Pclass','Embarked', 'Age1', 'Title', 'FamilySize1'])
titanic1.shape
titanic1.info()

#Drop un-wanted columns for faster execution and create new set called titanic2
titanic2 = titanic1.drop(['PassengerId','Name','Age','Ticket','Cabin','Survived'], axis=1, inplace=False)
#See how may columns are there after 3 additional columns, one hot encoding and dropping
titanic2.shape 

X_train = titanic2[0:titanic_train.shape[0]]
X_train.shape
X_train.info()
y_train = titanic_train['Survived']

#Let's build the model
#If we don't use random_state parameter, system can pick different values each time and we may get slight difference in accuracy each time you run.
tree_estimator = tree.DecisionTreeClassifier(random_state=2017)
dt_grid = {'criterion':['gini','entropy'], 'max_depth':list(range(3,10))}
grid_tree_estimator = model_selection.GridSearchCV(tree_estimator, dt_grid, cv=10)
grid_tree_estimator.fit(X_train, y_train)
print(grid_tree_estimator.best_score_) #Best score
print(grid_tree_estimator.best_params_)
print(grid_tree_estimator.score(X_train, y_train)) #train score
#Remember: As a Data Scientist the Data Preparation, EDA and FE takes more time. Model building is easy.
     
#exlore feature importances calculated by decision tree algorithm
features = X_train.columns
#best_estimator_ gives final best parameters. 
#feature_importances_: Every feture has an importance with a priority number. Now we want to use best estimator along with very very importance features

importances = grid_tree_estimator.best_estimator_.feature_importances_
#Let's create a DataFrame with fetures and their importances.
#Check in the variable explorer for double click on fe_df variable and see each features importance. Blue color fetures are more important.
fe_df = pd.DataFrame({'feature':features, 'importance': importances}) #You may notice that feature	importance "Title_Mr" has more importance as 0.6152088401351238

#Now let's predict on test data
X_test = titanic2[titanic_train.shape[0]:] #shape[0]: means 0 index to n index. Not specifying end index is nothing but till nth index
X_test.shape
X_test.info()
titanic_test['Survived'] = grid_tree_estimator.predict(X_test)

titanic_test.to_csv('submission.csv', columns=['PassengerId','Survived'],index=False)