# -*- coding: utf-8 -*-
"""classification_problem.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e_uwDonZO7WHpY0lH7x16aQmVpo-xkEm

Loading and Preprocessing
"""

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

#loading the dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

df.head()

#checking missing values
df.isnull().sum()

#feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('target', axis=1))

#DataFrame with scaled features
scaled_df = pd.DataFrame(scaled_features, columns=data.feature_names)
scaled_df['target'] = data.target

scaled_df.head()

"""Explanation:

* Dataset doesn't have missing values, missing value handling avoids potential errors during model training.
* Used StandardScaler to scale the features to work better when the features are scaled to a similar range.

Classification Algorithm Implementation
"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#split the data
X = scaled_df.drop('target', axis=1)
y = scaled_df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#initialize models
models = {
    "Logistic Regression" : LogisticRegression(),
    "Decision Tree" : DecisionTreeClassifier(),
    "Random Forest" : RandomForestClassifier(),
    "SVM" : SVC(),
    "k-NN" : KNeighborsClassifier()
}

#train and evaluate models
results = {}
for name, model in models.items():
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  acc = accuracy_score(y_test, y_pred)
  results[name] = acc
  print(f"{name} : Accuracy = {acc:.2f}")

"""Descriptions:

1. Logistic Regression : A linear model for binary classification that predict probabilities.
2. Decision Tree : A tree-based model that splits data based on feature values. It handles non-linear relationships effectively.
3. Random Forest : An ensemble of decision trees that reduces overfitting and improves generalization.
4. SVM : A model that finds a hyperplane to separate classes with maximum margin. Effective in high-dimensional spaces.
5. k-NN : A distance-based model that assigns a class based on the majority class among the nearest neighbors.

Model Comparison
"""

best_model = max(results, key=results.get)
worst_model = min(results, key=results.get)

print(f"The best performing model is {best_model} with an accoracy of {results[best_model]:.2f}")
print(f"The wors performing model is {worst_model} with an accuracy of {results[worst_model]:.2f}")

