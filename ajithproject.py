# -*- coding: utf-8 -*-
"""AjithProject

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1haIX4UByptxjtBKiHmo66yIvDVaUV_-k
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn

data = pd.read_csv("user_reviews.csv")

data.dropna(inplace = True )

data.columns

data['score'].unique()

# df = df[df['Rating']!= 3]
data['Class Label'] = np.where(data['score']>8.0, 1, 0)
data.head(10)

pd.crosstab(index = data['Class Label'], columns="Total count")



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data['extract'], data['Class Label'], random_state=0)

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer().fit(X_train)

X_train_vectorized = vect.transform(X_train)

from sklearn.linear_model import LogisticRegression,SGDClassifier
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

from sklearn.metrics import roc_curve, roc_auc_score, auc
predictions = model.predict(vect.transform(X_test))
print('AUC: ', roc_auc_score(y_test, predictions))
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)

vect1 = CountVectorizer(min_df= 10, ngram_range=(1,1)).fit(X_train)
X_train_vectorized1 = vect1.transform(X_train)
model1 = LogisticRegression()
model1.fit(X_train_vectorized1, y_train)
predictions1 = model1.predict(vect1.transform(X_test))
false_positive_rate1, true_positive_rate1, thresholds1 = roc_curve(y_test, predictions1)
roc_auc1 = auc(false_positive_rate1, true_positive_rate1)

vect2 = CountVectorizer(min_df= 20, ngram_range=(2,2)).fit(X_train)
X_train_vectorized2 = vect2.transform(X_train)
model2 = LogisticRegression()
model2.fit(X_train_vectorized2, y_train)
predictions2 = model2.predict(vect2.transform(X_test))
false_positive_rate2, true_positive_rate2, thresholds2 = roc_curve(y_test, predictions2)
roc_auc2 = auc(false_positive_rate2, true_positive_rate2)
print(roc_auc2)

vect3 = CountVectorizer(min_df= 30, ngram_range=(3,3)).fit(X_train)
X_train_vectorized3 = vect3.transform(X_train)
model3 = LogisticRegression()
model3.fit(X_train_vectorized3, y_train)
predictions3 = model3.predict(vect3.transform(X_test))
false_positive_rate3, true_positive_rate3, thresholds3 = roc_curve(y_test, predictions3)
roc_auc3 = auc(false_positive_rate3, true_positive_rate3)
print(roc_auc3)

