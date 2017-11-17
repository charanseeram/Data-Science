# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:52:57 2017

@author: Saicharan.S
"""

#Refer to 15.kaggle-classification-IV-->titanic-VIII - EDA
#These 2 are hand in hand programs
import pandas as pd
import seaborn as sns
import os
from sklearn import preprocessing

#changes working directory
os.chdir("D:/Data Science/")

titanic_train = pd.read_csv("train.csv")

titanic_train.shape
titanic_train.info()

#create title column from name
def extract_title(name):
     return name.split(',')[1].split('.')[0].strip()
titanic_train['Title'] = titanic_train['Name'].map(extract_title)
sns.factorplot(x="Title", hue="Survived", data=titanic_train, kind="count", size=6)

titanic_train[['Age']].info() #Now you notice Age columns has MISSING data
age_imputer = preprocessing.Imputer()
#Fit the imputer on X.
age_imputer.fit(titanic_train[['Age']])
#.transform(): Impute all missing values in X.
titanic_train[['Age']] = age_imputer.transform(titanic_train[['Age']])
titanic_train[['Age']].info() #Now you notice Age columns has data for entire 891 records

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
titanic_train['Age1'] = titanic_train['Age'].map(convert_age)
titanic_train['Age1'] #Just display and see
sns.factorplot(x="Age1", hue="Survived", data=titanic_train, kind="count", size=6)

#For numberic to Categoric, use FacetGrid
#Let's see whether SibSp and Parch independently are useful or not!
sns.FacetGrid(titanic_train, row="Survived",size=8).map(sns.kdeplot, "SibSp").add_legend() #After looking at kdeplot, SibSp seems not much useful
sns.FacetGrid(titanic_train, row="Survived",size=8).map(sns.kdeplot, "Parch").add_legend() #After looking at kdeplot, Parch can bring some pattern discovery

#Now try to create a new column as FamilySize by combining SibSp and Parch
titanic_train['FamilySize'] = titanic_train['SibSp'] +  titanic_train['Parch'] + 1
titanic_train['FamilySize'].describe()
#Now let's see whether Family Size is giving some pattern recognition or not by plotting
sns.FacetGrid(titanic_train, row="Survived",size=8).map(sns.kdeplot, "FamilySize").add_legend()

def convert_familysize(size):
    if(size == 1): 
        return 'Single'
    elif(size <=3): 
        return 'Small'
    elif(size <= 6): 
        return 'Medium'
    else: 
        return 'Large'
        
#Convert FamilySize numerical column to Categorical column
titanic_train['FamilySize1'] = titanic_train['FamilySize'].map(convert_familysize)
sns.factorplot(x="FamilySize1", hue="Survived", data=titanic_train, kind="count", size=6) #hue is very important for 2d visualization. 
