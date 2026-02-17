👇

💳 Credit Card Fraud Detection System

An end-to-end Machine Learning project to detect fraudulent credit card transactions using anomaly detection and XGBoost classifier.

This project includes data preprocessing, model training, evaluation (ROC curve & confusion matrix), and deployment as a Streamlit web application.

🚀 Project Overview

Credit card fraud detection is a highly imbalanced classification problem.
This project:

Handles extreme class imbalance

Uses anomaly detection techniques

Trains a powerful XGBoost classifier

Evaluates using ROC-AUC, Precision, Recall

Deploys as a web app

📊 Dataset

Used the Credit Card Fraud Detection Dataset from Kaggle:

🔗 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Dataset Details:

284,807 transactions

492 fraudulent cases

Highly imbalanced dataset

PCA-transformed features (V1–V28)

Target column: Class

0 → Normal

1 → Fraud

🛠 Technologies Used

Python

Pandas

NumPy

Scikit-Learn

XGBoost

Matplotlib

Seaborn

Streamlit

⚙️ Machine Learning Models
1️⃣ Anomaly Detection

Isolation Forest

Local Outlier Factor

2️⃣ Supervised Learning

XGBoost Classifier

Used scale_pos_weight to handle imbalance.

📈 Model Evaluation

Confusion Matrix

Classification Report

ROC Curve

AUC Score

ROC-AUC is used instead of accuracy due to severe class imbalance.
