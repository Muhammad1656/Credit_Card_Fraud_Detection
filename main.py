import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from xgboost import XGBClassifier

print("⏳ Loading Dataset... (This might take few moments)")
# 1. Data Load Kar Rahe Hain
df = pd.read_csv('creditcard.csv')

print("✅ Data Loaded Successfully!")
print("-" * 30)

# 2. Data Check (Yahan hum dekhenge ke kitna bada fraud hai)
normal_trans = df[df['Class'] == 0]
fraud_trans = df[df['Class'] == 1]
print(f"Normal Transactions: {len(normal_trans)}")
print(f"Fraud Transactions: {len(fraud_trans)}")
print("-" * 30)

# 3. Data Preprocessing (Scaling)
scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])

# 'Time' column drop kar diya
df = df.drop(['Time'], axis=1)

# 🔥 THE PRO FIX: Ab AI sirf in 5 cheezon par train hoga! 🔥
X = df[['V14', 'V4', 'V10', 'V12', 'Amount']]
y = df['Class']

# 4. Train-Test Split (Data ko 80% training aur 20% testing mein torna)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. The Magic: SMOTE (Data Balancing)
print("⚖️ Applying SMOTE to balance the data... (Wait please)")
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
print("✅ SMOTE Applied! Data is now balanced.")
print("-" * 30)

# 6. Model Training (AI ko sikhana - Upgraded to Random Forest)
print("🧠 Training AI Model (Random Forest)... (This might take 1-2 min)")
model = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
model.fit(X_train_resampled, y_train_resampled)
print("✅ Random Forest Model Trained!")
print("-" * 30)

# 7. Model Testing & Evaluation (Result ka waqt)
print("📊 Testing Model on unseen data...")
y_pred = model.predict(X_test)

print("\n--- CLASSIFICATION REPORT ---")
print(classification_report(y_test, y_pred))

print("--- CONFUSION MATRIX ---")
print(confusion_matrix(y_test, y_pred))
print("\n🎉 Project Step 1 Complete!")

print("\n🔍 Step 8: AI Explainability (Feature Importance)...")
feature_importances = pd.Series(model.feature_importances_, index=X.columns)

# Top 5 Red flags nikalna (Kyunke ab features hi 5 hain)
top_features = feature_importances.nlargest(5)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_features, y=top_features.index, palette="viridis")
plt.title("Top 5 Red Flags (Fraud Indicators) for AI")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.tight_layout()

plt.savefig("fraud_indicators.png")
print("📈 Graph saved as 'fraud_indicators.png'. Close the graph window to continue!")
plt.show() 

print("-" * 30)

# 9. Model Saving (Dimaagh ko export karna)
print("💾 Step 9: Saving the AI Brain for Web App...")
joblib.dump(model, 'random_forest_fraud_model.pkl')
joblib.dump(scaler, 'data_scaler.pkl')

print("✅ Model aur Scaler dono '.pkl' files mein save ho gaye!")
print("🚀 NEXT STOP: STREAMLIT DEPLOYMENT!")