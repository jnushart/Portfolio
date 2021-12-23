
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

items = pd.read_excel(r'C:\Users\jnushart\OneDrive - Tractor Supply Co\Downloads\Capstone.xlsx', sheet_name = 'Items')
stores = pd.read_excel(r'C:\Users\jnushart\OneDrive - Tractor Supply Co\Downloads\Capstone.xlsx', sheet_name = 'Stores')
inactivestores = pd.read_excel(r'C:\Users\jnushart\OneDrive - Tractor Supply Co\Downloads\Capstone.xlsx', sheet_name = 'Stores Not in Program')


#first Random Forest with all predictor variables in play to output accuracy and most important variables.
stores['classifier'] = np.where(stores['Savings per Shipment'] >= np.percentile(stores['Savings per Shipment'],75),1,0)

x=stores[['Sales%', 'Median HH Income','% in ag','Nearest Store','population', 'density']]
y=stores[['classifier']]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=190)

clf=RandomForestClassifier(n_estimators=10000)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

clf=RandomForestClassifier(n_estimators=10000)

clf.fit(X_train,y_train)

feature_imp = pd.Series(clf.feature_importances_,index=x.columns.values).sort_values(ascending=False)
feature_imp

get_ipython().run_line_magic('matplotlib', 'inline')
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.legend()
plt.show()


#Run model second time with less predictors, by removing low importance predictors to improve accuracy

x=stores[['Sales%','% in ag','Nearest Store','population', 'density']]
y=stores[['classifier']]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=190)
clf=RandomForestClassifier(n_estimators=10000)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
clf=RandomForestClassifier(n_estimators=10000)
clf.fit(X_train,y_train)
feature_imp = pd.Series(clf.feature_importances_,index=x.columns.values).sort_values(ascending=False)
feature_imp
get_ipython().run_line_magic('matplotlib', 'inline')
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.legend()
plt.show()


inactivestores2


#Run inactive stores through the model to create prediction
inactivestores2 = inactivestores
inactivestores2 = inactivestores2.dropna()
inactivestores2.reset_index(drop=False, inplace=True)
inactivestores3 = inactivestores2[['Sales%', '% in ag','population','density','Nearest Store']]
predict = clf.predict(inactivestores3)

#Prepare data for output
inactivestores4 = inactivestores2[['Store No', 'Zip Code']]
inactivestores4 = pd.merge(inactivestores4,inactivestores3,right_index = True, left_index=True)
inactivestores4['prediction'] = predict
yes = inactivestores4['prediction'] ==1
recommendedStores = inactivestores4[yes]
activestores = stores[['Shipment Ship Node', 'Zip Code']]
activestores['Status'] = 'Active'
recommendedStores['Shipment Ship Node'] = recommendedStores['Store No']
recommendedStores = recommendedStores[['Shipment Ship Node', 'Zip Code']]
recommendedStores['Status'] = 'Recommended'

#Output Data
stores_final = activestores.append(recommendedStores, ignore_index=True)
stores_final.to_csv(r'M:\Omnichannel\JNushart\Store Recommendation.csv', index=False)

recommendedStores

from sklearn import tree
plt.figure(figsize=(17,10))
treeplot = tree.plot_tree(clf.estimators_[0], feature_names=x.columns, filled=True,fontsize = 8)

