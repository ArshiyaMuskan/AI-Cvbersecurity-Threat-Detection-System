import streamlit as st
import requests
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

st.set_page_config(page_title="AI Threat Detection", layout="wide")

st.title("🚨 AI Cyber Threat Detection System")

# --------------------------
# LOAD MODEL
# --------------------------
model = joblib.load("kdd_model.pkl")

# --------------------------
# INPUT SECTION
# --------------------------
st.sidebar.header("Input Features")

features_input = st.sidebar.text_area(
    "Enter features (comma-separated)",
    "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
)

if st.sidebar.button("Predict"):

    feature_list = list(map(float, features_input.split(",")))

    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={"features": feature_list}
    )

    result = response.json()

    if result["prediction"] == "anomaly":
        st.error(f"🚨 ALERT: {result['prediction']}")
    else:
        st.success(f"✅ Status: {result['prediction']}")

# --------------------------
# CONFUSION MATRIX
# --------------------------
st.subheader("📊 Model Performance")

df = pd.read_csv("cleaned_kdd.csv")

X = df.iloc[:, :-1]
y_true = df.iloc[:, -1]
y_pred = model.predict(X)

cm = confusion_matrix(y_true, y_pred)

fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_title("Confusion Matrix")

st.pyplot(fig)