from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd

glass_df = pd.read_csv('./glass.csv')
glass_df
X_train = glass_df.drop("Type",axis=1)
Y_train = glass_df["Type"]

X_train, X_test, Y_train, Y_test= train_test_split(X_train, Y_train, test_size=0.4, random_state=0)
model = GaussianNB()
model.fit(X_train,Y_train)

y_pred = model.predict(X_test)


score = accuracy_score(Y_test,y_pred)*100
print("accuracy score: " + str(score))

print(classification_report(Y_test, y_pred))



