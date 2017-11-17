#Data Frames1

import pandas as pd
print(pd.__version__)
titanic_train = pd.read_csv("D:/Data Science/train.csv")
print(type(titanic_train))

#explore the dataframe
titanic_train.shape
titanic_train.info()
titanic_train.describe

#access column/columns of a dataframe
titanic_train['Sex']
titanic_train[['Fare']]
titanic_train.Sex
titanic_train[['Survived','Fare']]

#access rows of a data frame
titanic_train.iloc[0]
titanic_train[0:3] #You can read the data from DataFrames using iloC(Ilocation)
titanic_train.iloc[0:3]
titanic_train.iloc[885:891]
titanic_train.tail(6)
titanic_train.head(6)

#access both rows and columns of a dataframe
titanic_train.iloc[0:3,4]
titanic_train.iloc[0:4,3:5]
titanic_train.loc[0:3,'Name'] #Ideal usage

#conditional access of dataframe
#titanic_train.iloc[titanic_train.Sex == 'female', 4] #iLocation based boolean indexing on an integer type is not available
titanic_train.loc[titanic_train.Sex == 'female', 'Sex']