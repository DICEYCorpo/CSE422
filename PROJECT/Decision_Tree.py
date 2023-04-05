from pandas.core.common import random_state
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


airline=pd.read_csv("Airlines.csv")
manipulated_plane = pd.get_dummies(airline, columns=['Airline'])
X = manipulated_plane.drop(['Delay', 'id', 'AirportFrom', 'AirportTo'], axis=1)
y = manipulated_plane['Delay']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=112)
cl = DecisionTreeClassifier(criterion='entropy',random_state=1)
cl.fit(X_train, y_train)
y_prediction = cl.predict(X_test)
score = classification_report(y_prediction, y_test)
print(score)