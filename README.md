# 🛡️ Browsing Hijack Detection System

## 📌 Project Title

**Enhancing Trust in Online Browsing Environments**

---

## 📖 Description

This project is a real-time cybersecurity system designed to detect malicious browsing behavior such as browser hijacking, suspicious redirects, and abnormal user activity.

The system uses behavioral analysis and machine learning concepts to classify browsing activity as **Normal** or **Hijacked**, and provides **real-time alerts** through a monitoring dashboard.

---

## 🎯 Objectives

* Detect browser hijacking in real time
* Monitor user behavior (clicks, scrolls, redirects)
* Classify activity using detection logic / ML
* Display results in a dashboard
* Generate alerts when threats are detected

---

## 🏗️ System Architecture

1. **Chrome Extension**

   * Collects user browsing data
   * Sends data to backend every second

2. **Flask Backend**

   * Receives data via API
   * Performs detection logic
   * Stores logs (in-memory)

3. **Detection Model**

   * Uses rule-based + ML concept
   * Classifies activity:

     * Normal
     * Hijacked

4. **Tkinter Dashboard**

   * Displays logs in real time
   * Shows graph (Normal vs Hijacked)
   * Generates alert popups

---

## ⚙️ Technologies Used

* Python 3
* Flask
* Tkinter
* Matplotlib
* JavaScript
* Google Chrome Extension (Manifest V3)

---

## 📂 Project Structure

```
enhancing-trust-browser-security/

├── extension/
│   ├── manifest.json
│   ├── content.js
│
├── backend/
│   ├── server.py
│
├── dashboard/
│   ├── dashboard.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Install Requirements

```bash
pip install flask flask-cors matplotlib requests
```

---

### 2️⃣ Run Backend Server

```bash
cd backend
python server.py
```

---

### 3️⃣ Run Dashboard

```bash
cd dashboard
python dashboard.py
```

---

### 4️⃣ Load Chrome Extension

1. Open Chrome
2. Go to `chrome://extensions/`
3. Enable **Developer Mode**
4. Click **Load unpacked**
5. Select the `extension` folder

---

## ▶️ How It Works

1. User browses websites
2. Extension collects activity data
3. Data is sent to Flask backend
4. Backend processes and classifies data
5. Dashboard displays logs and graph
6. Alerts are shown if hijacking detected

---

## 📊 Features

* Real-time monitoring
* Live dashboard with table
* Graph visualization
* Start / Stop monitoring
* Multiple alert popups
* Fast detection (<1 second)

---

## ⚠️ Limitations

* Uses rule-based detection (basic ML concept)
* Accuracy depends on thresholds
* Works in local environment
* Limited scalability

---

## 🔮 Future Enhancements

* Full machine learning model integration
* Database support (SQLite/MySQL)
* Cloud deployment
* Advanced threat detection
* Cross-browser support

---
## 📸 Screenshots

### 🔹 Dashboard UI
![Dashboard](screenshots/dashboard.png)

### 🔹 Detection Graph
![Graph](screenshots/graph.png)

### 🔹 Alert Notification
![Alert](screenshots/alert.png)

---
## 👩‍💻 Authors

* V. Ankitha
* B. Sowmya
* N. Naga Sahithi
* A. Kavya Reddy

Department of CSE (Cyber Security)
Sphoorthy Engineering College, Hyderabad

---

## 📜 License

This project is developed for academic purposes.

---

## ⭐ Acknowledgement

We thank our faculty and institution for their guidance and support in completing this project successfully.

---
