import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix

flight = pd.read_csv("Airlines.csv")
dummies = pd.get_dummies(flight, columns=["Airline", "AirportFrom", "AirportTo"])

X = dummies.drop(['Delay'], axis=1)
y = dummies['Delay']

#Training:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
NBModel = GaussianNB()
NBModel.fit(X_train, y_train)
y_predicted = NBModel.predict(X_test)

print(y_predicted)
print(accuracy_score(y_test, y_predicted)*100)

print(metrics.classification_report(y_test, y_predicted))
print(metrics.confusion_matrix(y_test, y_predicted))