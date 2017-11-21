# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:55:14 2017

@author: Saicharan.S
"""

from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.datasets import load_iris
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

train, test = df[df['is_train']==True], df[df['is_train']==False]
features = df.columns[0:4]

forest = RFC(n_jobs=2,n_estimators=50)

	
y, _ = pd.factorize(train['species'])

forest.fit(train[features], y)
preds = iris.target_names[forest.predict(test[features])]
pd.crosstab(index=test['species'], columns=preds, rownames=['actual'], colnames=['preds'])