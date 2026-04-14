# AI-Cvbersecurity-Threat-Detection-System
# 🚨 AI-Powered Cybersecurity Threat Detection System

An end-to-end **AI-based intrusion detection system** that analyzes network traffic and detects cyber threats using Machine Learning.

---

## 📌 Project Overview

This project builds a **Cybersecurity Threat Detection Dashboard** using:

* Machine Learning (Random Forest)
* Streamlit (Web App UI)
* Python (Data Processing & Modeling)

It detects whether network traffic is:

* ✅ Normal
* 🚨 Attack

---

## 🎯 Features

* 🔍 Real-time threat prediction
* 📊 Interactive dashboard (Streamlit)
* 📈 Data visualization (Seaborn & Matplotlib)
* 🧠 ML model integration (Scikit-learn)
* 📂 Dataset preprocessing pipeline
* ⚡ Lightweight deployment (Streamlit Cloud)

---

## 🧠 Tech Stack

| Category        | Tools Used          |
| --------------- | ------------------- |
| Language        | Python              |
| ML Library      | Scikit-learn        |
| Visualization   | Matplotlib, Seaborn |
| Backend         | Flask (optional)    |
| Frontend        | Streamlit           |
| Dataset         | KDD / NSL-KDD       |
| Deployment      | Streamlit Cloud     |
| Version Control | Git & GitHub        |

---

## 📁 Project Structure

```
AI-Cybersecurity-Threat-Detection-System/
│
├── app.py                     # Main Streamlit app
├── dashboard.py              # Dashboard UI
├── analytics_dashboard.py    # Advanced analytics
├── main.py                   # Core execution file
│
├── reduce_data.py            # Dataset reduction (5000 rows)
├── cleandata.py              # Data preprocessing
│
├── cleaned_kdd_small.csv     # Reduced dataset
├── kdd_model.pkl             # Trained ML model
├── model_columns.pkl         # Feature columns
│
├── packet_capture.py         # (Optional) Live packet simulation
│
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Cybersecurity-Threat-Detection-System.git
cd AI-Cybersecurity-Threat-Detection-System
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 📊 Dataset

* Source: KDD / NSL-KDD dataset
* Reduced to 5000 rows for performance
* Preprocessed using Pandas

---

## 🧪 Model Details

* Algorithm: Random Forest Classifier
* Task: Binary Classification (Attack vs Normal)
* Metrics:

  * Accuracy
  * Confusion Matrix

---

## 📈 Dashboard Features

* Attack vs Normal distribution
* Feature importance visualization
* Correlation heatmap
* Real-time predictions

---


```

---

## ⚠️ Common Issues & Fixes

### ❌ FileNotFoundError

👉 Ensure dataset is in repo:

```
cleaned_kdd_small.csv
```

### ❌ Git Push Error

```bash
git remote add origin <repo-url>
git push -u origin main
```

### ❌ ModuleNotFoundError

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Enhancements

* 🔥 Deep Learning (LSTM / Autoencoders)
* 📡 Real-time packet capture (Wireshark integration)
* 🌍 REST API using Flask
* 📊 SOC-level dashboard features
* ☁️ Cloud deployment (AWS / Azure)

---

## 👩‍💻 Author

**Arshiya Muskan**

* 💼 Aspiring AI & Cybersecurity Engineer
* 🌐 GitHub: https://github.com/ArshiyaMuskan

---

## ⭐ Show Your Support

If you like this project:

⭐ Star the repo
🍴 Fork it
📢 Share it

---

## 📜 License

This project is licensed under the MIT License.

---
