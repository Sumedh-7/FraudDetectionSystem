# Real-Time Fraud Detection System with Explainable AI

## Project Overview

This project is an end-to-end machine learning fraud detection system designed to identify suspicious financial transactions using advanced analytics and explainable AI techniques.

The system combines:
- Fraud prediction
- Explainable AI (SHAP)
- Risk segmentation
- Interactive Streamlit dashboard

This project simulates a real-world fintech fraud detection pipeline.

---

## Features

- Fraud detection using machine learning
- Explainable AI using SHAP
- Risk tier segmentation
- Interactive Streamlit dashboard
- Threshold optimization
- Fraud analytics visualizations

---

## Models Used

- LightGBM
- XGBoost
- Isolation Forest

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- XGBoost
- SHAP
- Streamlit
- Plotly
- Matplotlib
- Seaborn

---

## Dashboard Features

- Fraud overview analytics
- Transaction explorer
- Risk analysis
- Interactive visualizations
- Fraud probability insights

---

## Dataset

IEEE-CIS Fraud Detection Dataset from Kaggle.

Dataset Files Used:
- train_transaction.csv
- train_identity.csv

## Dataset Note

The complete IEEE-CIS Fraud Detection dataset was used locally during model training and experimentation.

Due to GitHub and Streamlit Cloud file size limitations, the full dataset was not uploaded to the repository.

A smaller sampled dataset (`sample_transactions.csv`) is used only for dashboard deployment and demonstration purposes.

Original Dataset:
https://www.kaggle.com/c/ieee-fraud-detection/data
---

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run dashboard:

cd dashboard

streamlit run app.py

---

## Live Dashboard

https://frauddetectionsystem1930.streamlit.app/

---

## Project Structure

FraudDetectionSystem/

├── analysis.ipynb  
├── README.md  
├── requirements.txt  
├── summary.docx 


├── charts/  
│   ├── shap_summary.png  
│   ├── fraud_rate_hour.png  
│   ├── transaction_distribution.png  
│   ├── risk_tier_donut.png  
│   └── pr_curve.png  

├── dashboard/  
│   ├── app.py  
│   └── sample_transactions.csv  


---

## Author

Sumedh Pednekar
