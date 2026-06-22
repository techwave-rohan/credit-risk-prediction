# 💳 Credit Risk Prediction System

## 📌 Overview

This project is an end-to-end Machine Learning application that predicts whether a customer is a **Good Credit Risk** or **Bad Credit Risk** based on demographic, financial, and loan-related information.

The project includes:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training & Evaluation
* Hyperparameter Tuning
* Streamlit Web Application
* Model Deployment

---

## 🎯 Problem Statement

Financial institutions face significant losses when loans are approved for customers who are likely to default.

The objective of this project is to build a machine learning model that can assess customer credit risk and help lenders make informed decisions.

---

## 📊 Dataset

**German Credit Risk Dataset**

### Features

* Age
* Sex
* Job
* Housing
* Saving Accounts
* Checking Account
* Credit Amount
* Duration
* Purpose

### Target Variable

* Good Risk (1)
* Bad Risk (0)

---

## 🔍 Exploratory Data Analysis

Key findings from EDA:

* Dataset contains approximately 70% Good Risk and 30% Bad Risk customers.
* Missing values were found in:

  * Saving Accounts
  * Checking Account
* Credit Amount distribution is positively skewed.
* Loan Duration shows a strong relationship with credit risk.
* Customers with larger loans and longer durations tend to have higher risk.

---

## ⚙️ Data Preprocessing

### Missing Value Handling

Missing values were replaced with:

```python
"unknown"
```

### Categorical Encoding

Applied One-Hot Encoding using:

```python
pd.get_dummies()
```

### Train-Test Split

```python
test_size = 0.2
random_state = 42
stratify = y
```

---

## 🤖 Models Used

### Logistic Regression

Used as the baseline model.

### Random Forest Classifier

Used for final predictions due to better performance on tabular data.

### Hyperparameter Tuning

Performed using:

```python
GridSearchCV
```

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix
* Cross Validation

---

## 🏆 Feature Importance

Top influential features included:

* Duration
* Credit Amount
* Checking Account Status
* Saving Account Status
* Housing
* Purpose

---

## 🌐 Web Application

A Streamlit-based web application was developed where users can:

1. Enter customer information.
2. Click Predict Risk.
3. Receive a credit risk assessment instantly.

### Inputs

* Age
* Job
* Sex
* Housing
* Saving Account
* Checking Account
* Credit Amount
* Duration
* Purpose

### Output

* ✅ Good Credit Risk
* ⚠️ Bad Credit Risk

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn

### Deployment

* Streamlit

### Model Persistence

* Joblib

---

## 📂 Project Structure

```text
credit-risk-prediction/
│
├── app/
│   └── app.py
│
├── data/
│
├── models/
│   ├── final_credit_risk_model.pkl
│   ├── columns.pkl
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── runtime.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/credit-risk-prediction.git
```

Move into the project directory:

```bash
cd credit-risk-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/app.py
```

---

## 📸 Application Screenshots

Add screenshots here:

<img width="1165" height="857" alt="image" src="https://github.com/user-attachments/assets/694b98f2-8432-4958-98ed-ed2d6df371f4" />
<img width="955" height="666" alt="image" src="https://github.com/user-attachments/assets/215f8ddc-4da4-4f10-aeb9-29ad5c55dc8a" />


---

## 🔮 Future Improvements

* XGBoost Implementation
* Explainable AI using SHAP
* Advanced Risk Dashboard
* Real-Time API Deployment
* Credit Score Recommendation System

---

## 👨‍💻 Author

**Rohan Kashyap**

B.Tech Electronics & Communication Engineering (ECE)

Interested in:

* Machine Learning
* Generative AI
* NLP
* MLOps
* FinTech Applications
