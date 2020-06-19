import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier


train_df = pd.read_csv('./train_preprocessed.csv')
test_df = pd.read_csv('./test_preprocessed.csv')
X_train = train_df.drop("Survived",axis=1)
Y_train = train_df["Survived"]
X_test = test_df.drop("PassengerId",axis=1).copy()
print(train_df[train_df.isnull().any(axis=1)])
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
train_df[['Survived','Sex']].groupby(['Survived'],as_index=False).mean().sort_values(by='Sex',ascending=False)
