

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

st.set_page_config(page_title="Cyber Threat Dashboard", layout="wide")

st.title("🚨 AI Cyber Threat Detection Dashboard")


# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv("cleaned_kdd.csv")


# ✅ FIX COLUMN NAME HERE
df.rename(columns={df.columns[-1]: "label"}, inplace=True)

# ---------------------------
# SECTION 1: DISTRIBUTION
# ---------------------------
st.subheader("📊 Attack vs Normal Distribution")

col1, col2 = st.columns(2)

with col1:

    fig1, ax1 = plt.subplots()
    sns.countplot(x='label', data=df, palette='coolwarm')
    ax1.set_title("Attack vs Normal")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    df['label'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue','salmon'])
    ax2.set_ylabel("")
    ax2.set_title("Percentage Distribution")
    st.pyplot(fig2)

# ---------------------------
# SECTION 2: HEATMAP
# ---------------------------
st.subheader("🔥 Feature Correlation Heatmap")

# ✅ REMOVE NON-NUMERIC DATA
numeric_df = df.select_dtypes(include=['number'])

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), cmap='coolwarm',linewidths=0.5,)
st.pyplot(fig)

# ---------------------------
# SECTION 3: MODEL PERFORMANCE
# ---------------------------
st.subheader("📈 Model Performance")

model = joblib.load("kdd_model.pkl")

X = df.drop("label", axis=1)
y = df["label"]

y_pred = model.predict(X)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y, y_pred)

fig4, ax4 = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
ax4.set_title("Confusion Matrix")
st.pyplot(fig4)

# ---------------------------
# SECTION 4: FEATURE IMPORTANCE
# ---------------------------
st.subheader("⭐ Feature Importance")

if hasattr(model, "feature_importances_"):
    importance = model.feature_importances_
    features = X.columns

    imp_df = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)

    fig5, ax5 = plt.subplots(figsize=(10,6))
    sns.barplot(x="Importance", y="Feature", data=imp_df.head(10))
    ax5.set_title("Top 10 Important Features")
    st.pyplot(fig5)
else:
    st.warning("Model does not support feature importance")