import pandas as pd
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import svm

data=pd.read_csv('./glass.csv')
a=data.drop('Type', axis=1)
b=data['Type']
x_train, x_test, y_train, y_test = model_selection.train_test_split(a, b, test_size=0.2, random_state=20)

lc = svm.SVC(kernel="linear")
lc.fit(x_train, y_train)
y_predict = lc.predict(x_test)
print("accuracy", metrics.accuracy_score(y_test, y_predict))
print("classification_report\n",metrics.classification_report(y_test,y_predict))