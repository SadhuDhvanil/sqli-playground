[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-blue?logo=render&style=flat-square)](https://sqli-playground.onrender.com)

> ⚠️ **Educational Use Only**  
> This application is intentionally vulnerable and should only be used for learning or authorized testing environments. Do not deploy it in production.

# SQL Injection Playground

An educational web application demonstrating SQL injection vulnerabilities and detection techniques.

---

## 🎯 Project Overview

This project creates a vulnerable web application alongside a detection engine to help understand SQL injection attacks and defenses. It's designed for educational purposes to teach web security concepts.

---

## 🚀 Features

- **Difficulty-Based Learning**: Three progressive levels of SQL injection complexity  
  - 🟢 Beginner: Basic authentication bypass techniques  
  - 🟡 Intermediate: Advanced bypass and data extraction methods  
  - 🔴 Advanced: Complex attacks and evasion techniques
- **Interactive Learning**: Expandable payload details with click-to-learn functionality
- **SQL Breakdown**: Step-by-step explanation of how each attack works in the database
- **Security Risk Assessment**: Clear impact analysis for each vulnerability type
- **Enhanced Detection**: Monitors 15+ SQL injection patterns and techniques
- **Secure Implementation**: Parameterized queries demonstration
- **Real-time Logging**: Tracks injection attempts with detailed analysis

---

## 📁 Project Structure

```
sqli-playground/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── run.sh                 # Startup script
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── secure_login.html
│   ├── dashboard.html
│   └── logs.html
├── static/                # CSS and static files
│   └── css/
│       └── styles.css
├── database/              # SQLite database
│   └── vulnerable.db
├── logs/                  # Application logs
│   └── app.log
├── venv/                  # Python virtual environment (should be added to .gitignore)
└── Procfile               # For deployment with Render/Heroku
```

---

## 🔧 Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sqli-playground.git
cd sqli-playground
```

### 2. Set Up Virtual Environment (if not already created)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Then open your browser at:  
👉 `http://localhost:5001`

---

## 🧪 Testing SQL Injection

### 🔐 Sample Users

- `admin` : `admin123`  
- `user1` : `password1`  
- `john_doe` : `secret123`

### 💉 Vulnerable Login Payloads

Try these in the username field:

```
admin' --
' OR '1'='1' --
admin' OR 1=1 --
```

---

## 🛡️ Security Features

### 🔍 Detection Techniques

- Pattern matching for SQL keywords
- Comment pattern detection
- Quote manipulation detection
- Time-based attack detection
- Error pattern analysis

### ✅ Prevention Techniques

- Parameterized queries
- Input validation
- Proper error handling
- Session management
- Logging and monitoring

---

## 📊 Monitoring

- **Admin Access**: Login as `'admin'` to view injection logs
- **Real-time Logging**: All injection attempts are logged
- **Detection Statistics**: View successful vs. failed attempts

---
## ⚠️ Important Notes

- **Educational Purpose Only**: This application contains intentional vulnerabilities
- **Do Not Use in Production**: Never deploy this code to real-world environments
- **Local Testing Only**: Designed for local or lab security education

---

## 🎓 Learning Objectives

- Understand SQL injection attack vectors
- Identify vulnerable code patterns
- Practice secure coding techniques
- Explore detection and prevention methods
- Gain hands-on experience with web security

---

## 🤝 Contributing

This is an educational project. Feel free to:

- Add new vulnerability scenarios
- Improve detection algorithms
- Enhance the UI/UX
- Add more educational content

> Remember: Use this knowledge responsibly and only for educational purposes or authorized security testing.

---
