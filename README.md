# 🎬 Netflix Customer Churn Prediction App

## 🔗 Link Streamlit
[Streamlit](https://app-netflix-customer-churn-reyhan.streamlit.app/)

## 📌 Project Description
This project is a **Customer Churn Prediction Web Application** built using Machine Learning and deployed with Streamlit. The application predicts whether a streaming platform customer is likely to churn based on demographic information, subscription details, and viewing behavior.

The model analyzes customer activity patterns such as watch hours, login frequency, subscription type, and payment method to estimate the probability of churn. This allows streaming platforms to identify high-risk customers and implement retention strategies.

---

## 🎯 Project Objectives
- Predict customer churn probability
- Identify customers at risk of leaving the platform
- Provide an interactive interface for customer data input
- Allow batch prediction using CSV or Excel uploads
- Deploy a machine learning model as a web application

---

## ⚙️ Application Features
- Interactive form for customer profile and streaming behavior
- CSV / Excel file upload for batch prediction
- Automatic feature engineering
- Churn probability prediction
- Status output: **STAY ✅ / CHURN ❌**
- Visual **Risk Meter**
- Download prediction results as CSV
- Responsive UI with dark mode design

---

## 📂 Dataset
Dataset source:

🔗 https://www.kaggle.com/datasets/abdulwadood11220/netflix-customer-churn-dataset

Dataset contains:
- Customer demographic information
- Subscription type
- Payment method
- Device usage
- Watch hours
- Login behavior
- Region and usage patterns

These features are used to train a machine learning model for churn prediction.

---

## 🧠 Technologies Used

### Machine Learning
- Scikit-learn
- Feature Encoding
- Feature Scaling
- Classification Model

### Data Processing
- Pandas
- NumPy

### Deployment & Interface
- Streamlit
- Python
- Pickle

---

## 📁 Project Structure

```
Streamlit-Netflix-Customer-Churn-App
│
├── app.py
├── model.pkl
├── encoders.pkl
├── scalers.pkl
├── requirements.txt
│
├── utils
│   ├── load_assets.py
│   ├── predict.py
│   └── preprocess.py
│
├── views
│   ├── prediction.py
│   ├── tentang_project.py
│   ├── tentang_saya.py
│   └── kontak.py
│
└── image
    └── Reyhan.jpeg
```

---

## 🚀 Installation

Clone the repository

```
git clone https://github.com/alzahrareyhan/Streamlit-Netflix-Customer-Churn-App.git
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run app.py
```

---

## 👨‍💻 Author

**Reyhan Nandita Al Zahra**

Aspiring **Data Scientist / Data Analyst** interested in machine learning, predictive analytics, and data-driven decision making.

GitHub  
https://github.com/alzahrareyhan
