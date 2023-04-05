

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


plane = pd.read_csv('Airlines.csv')
manipulated_plane = pd.get_dummies(plane, columns=['Airline'])
X = manipulated_plane.drop(['Delay','id','AirportFrom','AirportTo'], axis=1)
y = manipulated_plane['Delay']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=2)
LogisticModel = LogisticRegression()
logistic_fit = LogisticModel.fit(X_train,y_train)
prediction = LogisticModel.predict(X_test)
print(classification_report(y_test,prediction))


