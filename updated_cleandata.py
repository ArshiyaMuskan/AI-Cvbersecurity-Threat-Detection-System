# ==========================
# IMPORTS
# ==========================
print("🚀 Script started...")
import os
print(os.listdir())
import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ==========================
# LOAD DATA
# ==========================
# LOAD DATA (FIXED)
import pandas as pd

df = pd.read_csv('KDDTest+.arff', comment='@', header=None)

# Add column names
df.columns = [f'feature_{i}' for i in range(len(df.columns)-1)] + ['target']

print("Initial Shape:", df.shape)

# ==========================
# CLEANING
# ==========================

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df = df.ffill()

# ==========================
# SEPARATE FEATURES & TARGET
# ==========================
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# ==========================
# ONE-HOT ENCODING (IMPORTANT)
# ==========================
X = pd.get_dummies(X)

# ==========================
# FEATURE SCALING
# ==========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================
# TRAIN-TEST SPLIT
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ==========================
# FINAL OUTPUT
# ==========================
print("\nFinal Shapes:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# ==========================
# SAVE CLEAN DATA
# ==========================
clean_df = pd.DataFrame(X_scaled)
clean_df['target'] = y.values
clean_df.to_csv("cleaned_kdd.csv", index=False)

print("\n✅ Cleaned dataset saved as cleaned_kdd.csv")
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)
import joblib

# Save model
joblib.dump(model, "kdd_model.pkl")

# Save column structure (VERY IMPORTANT)
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("✅ Model and columns saved!")
# Predict
y_pred = model.predict(X_test)

# Results
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n", cm)

# Plot
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
print("🔥 END OF SCRIPT REACHED")

