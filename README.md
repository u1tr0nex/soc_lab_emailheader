# 📧 Email Header Analysis — SOC Lab

A hands-on cybersecurity lab for the GraySentinel training platform.
Students analyze raw email headers to identify phishing indicators.

---

## 🎯 Lab Objective

Presented with a raw email header and must answer three questions:

1. Is the SPF valid?
2. What is the Return-Path domain?
3. Does the DKIM signature pass?

---

## 🚀 Setup & Run Locally

### Linux (Kali/Ubuntu)

```bash
git clone https://github.com/u1tr0nex/soc_lab_emailheader.git
cd soc_lab_emailheader
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Windows

```bash
git clone https://github.com/u1tr0nex/soc_lab_emailheader.git
cd soc_lab_emailheader
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit: http://127.0.0.1:5000

---

## 🔐 Skills Covered

- Email header analysis
- SPF, DKIM, DMARC authentication
- Typosquatting detection
- Phishing identification

---

## 👤 Author

Abhimanyu Rawat — Technical Research & Cyber Security Operations Intern GraySentinel

---
