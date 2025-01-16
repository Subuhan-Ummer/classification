# classification

# Breast Cancer Classification

This project implements a supervised machine learning to classify breast cancer using the dataset available in the `sklearn` library. Multiple classification algorithms are used and their performances compared.

---

## Dataset

The dataset used is the Breast Cancer dataset from `sklearn.datasets`. It contains features derived from digitized images of a fine needle aspirate (FNA) of a breast mass, including:

- 30 numeric features (e.g., mean radius, texture, area).
- A binary target: `0` (Malignant) and `1` (Benign).

---

## Features

1. **Loading and Preprocessing**
   - Checked for missing values.
   - Applied `StandardScaler` to normalize the features for improved performance of distance-based models.

2. **Classification Algorithms Implemented**
   - **Logistic Regression**: Linear model for binary classification.
   - **Decision Tree**: Tree-based model handling non-linear relationships.
   - **Random Forest**: Ensemble of decision trees to reduce overfitting.
   - **Support Vector Machine (SVM)**: Finds a hyperplane for maximum margin separation.
   - **k-Nearest Neighbors (k-NN)**: Distance-based model classifying based on nearest neighbors.

3. **Model Evaluation**
   - Accuracy score used as the evaluation metric.
   - Identified the best and worst-performing models based on their accuracy.

---

## Results

After training and evaluating the models:
- **Best Performing Model**: `<Insert Best Model>` with an accuracy of `<Insert Accuracy>`.
- **Worst Performing Model**: `<Insert Worst Model>` with an accuracy of `<Insert Accuracy>`.

---

