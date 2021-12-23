
# coding: utf-8

#Import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
from sklearn import metrics
from sklearn import tree

#Load data and run first Item Model
items = pd.read_excel(r'C:\Users\Jordan\Desktop\Capstone\Capstone.xlsx', sheet_name = 'Items')

items['Dim Weight'] = items['Largest Side'] + 2*items['Middle Side'] + 2*items['Smallest Side']
x1= items[['Item Type']]
x2= items[['Unit Weight','Largest Side', 'Smallest Side','Dim Weight','Zone Improvement per Order']]
#x= items[['Unit Weight','Dim Weight']]
y= items [['Savings Per Order']]
x = pd.get_dummies(data=x1, drop_first=True)
x = x.merge(x2,left_index=True, right_index=True)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.25, random_state=768)

model = RandomForestRegressor(n_estimators=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
rmse
feature_imp = pd.Series(model.feature_importances_,index=x.columns.values).sort_values(ascending=False)
print(feature_imp)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

get_ipython().run_line_magic('matplotlib', 'inline')
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.legend()
plt.show()


#Start second model after removing lowest importance variables and increasing accuracy
x= items[['Unit Weight','Largest Side', 'Smallest Side','Dim Weight','Zone Improvement per Order']]
y= items [['Savings Per Order']]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.25, random_state=768)

model = RandomForestRegressor(n_estimators=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
rmse
feature_imp = pd.Series(model.feature_importances_,index=x.columns.values).sort_values(ascending=False)
print(feature_imp)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

get_ipython().run_line_magic('matplotlib', 'inline')
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.legend()
plt.show()


#Accuracy Plot & output
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
predictions = model.predict(X_test)
items['predictions'] = predictions.tolist()
items.to_csv(r'C:\Users\Jordan\Desktop\Capstone\Items Recommendation.csv', index=False)

