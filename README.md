# 💳 Credit Card Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost%20%7C%20Random%20Forest-orange.svg)
![Imbalanced Data](https://img.shields.io/badge/Technique-SMOTE-green.svg)

An enterprise-grade Machine Learning application designed to detect fraudulent credit card transactions in real-time. This project tackles the classic problem of highly imbalanced datasets in the financial sector, ensuring maximum precision and recall to catch anomalies without blocking legitimate users.

---

## ✨ VIP Features
* **🧠 Advanced ML Models:** Utilizes powerful ensemble algorithms like Random Forest and XGBoost to detect hidden patterns in transaction behaviors.
* **⚖️ Imbalanced Data Handling:** Implements **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the dataset, preventing the AI from simply guessing "Not Fraud" every time.
* **📊 Live Dashboard:** Built entirely on Streamlit, offering an interactive UI where users can input transaction parameters and get an instant Fraud/Legit prediction.
* **📈 Deep Analytics:** Displays model confidence scores, feature importance charts, and precision-recall metrics directly on the dashboard.

---

## 🛠️ Tech Stack & Architecture
| Component | Technology Used |
| :--- | :--- |
| **Programming Language** | Python |
| **Frontend UI** | Streamlit |
| **Model Training** | Scikit-Learn, XGBoost |
| **Data Resampling** | Imbalanced-learn (SMOTE) |
| **Data Source** | European Cardholders Dataset (Kaggle) |

---

## 🚀 How to Run Locally

Deploy this banking-level AI engine on your local machine in seconds:

**1. Clone the Repository**
```bash
git clone [https://github.com/Muhammad1656/Credit_Card_Fraud_Detection.git](https://github.com/Muhammad1656/Credit_Card_Fraud_Detection.git)
cd Credit_Card_Fraud_Detection

2. Install Dependencies
Make sure Python is installed, then run the engine setup:

Bash
pip install -r requirements.txt
3. Launch the Dashboard
Start the local Streamlit server:

Bash
streamlit run app.py
💡 How It Works (Under the Hood)
Data Ingestion: Loads the highly anonymized dataset (using PCA components V1-V28, Time, and Amount) to protect user privacy.

Data Balancing: Because frauds are less than 1% of the data, the engine applies SMOTE to synthesize fake fraud cases, teaching the AI exactly what a scam looks like.

Scaling: Transaction amounts and times are heavily scaled (StandardScaler/RobustScaler) so the AI doesn't get biased by large dollar amounts.

Prediction Engine: The user inputs transaction details, the model calculates the probability of anomaly, and triggers an alert if the threshold is breached.

👨‍💻 Developer
Muhammad Bin Nadeem BSAI Data Science & ML Developer Passionate about building hybrid AI systems, scalable machine learning architectures, and solving complex real-world data problems.

If you found this project helpful, don't forget to star ⭐ the repository!