# SQL Injection Playground

An educational web application demonstrating SQL injection vulnerabilities and detection techniques.

## 🎯 Project Overview

This project creates a vulnerable web application alongside a detection engine to help understand SQL injection attacks and defenses. It's designed for educational purposes to teach web security concepts.

## 🚀 Features

- **Difficulty-Based Learning**: Three progressive levels of SQL injection complexity
  - 🟢 **Beginner**: Basic authentication bypass techniques
  - 🟡 **Intermediate**: Advanced bypass and data extraction methods  
  - 🔴 **Advanced**: Complex attacks and evasion techniques
- **Professional UI**: Modern black/white/grey theme with improved contrast and readability
- **Interactive Learning**: Expandable payload details with click-to-learn functionality
- **SQL Breakdown**: Step-by-step explanation of how each attack works in the database
- **Security Risk Assessment**: Clear impact analysis for each vulnerability type
- **Enhanced Detection**: Monitors 15+ SQL injection patterns and techniques
- **Secure Implementation**: Parameterized queries demonstration
- **Real-time Logging**: Tracks injection attempts with detailed analysis

## 📁 Project Structure

```
sqli-playground/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── run.sh                # Startup script
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── secure_login.html
│   ├── dashboard.html
│   └── logs.html
├── static/               # CSS and static files
│   └── css/
│       └── styles.css
├── database/             # SQLite database
│   └── vulnerable.db
├── logs/                 # Application logs
│   └── app.log
└── venv/                 # Python virtual environment
```

## 🔧 Setup Instructions

1. **Install Dependencies**:
   ```bash
   cd sqli-playground
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   ./run.sh
   ```
   Or manually:
   ```bash
   source venv/bin/activate
   python app.py
   ```

3. **Access the Application**:
   Open your browser and navigate to: `http://localhost:5001`

## 🔓 Testing SQL Injection

### Sample Users
- **admin** : admin123
- **user1** : password1
- **john_doe** : secret123

### Vulnerable Login Payloads

Try these in the username field:
- `admin' --`
- `' OR '1'='1' --`
- `admin' OR 1=1 --`


## 🛡️ Security Features

### Detection Techniques
- Pattern matching for SQL keywords
- Comment pattern detection
- Quote manipulation detection
- Time-based attack detection
- Error pattern analysis

### Prevention Techniques
- Parameterized queries
- Input validation
- Proper error handling
- Session management
- Logging and monitoring

## 📊 Monitoring

- **Admin Access**: Login as 'admin' to view injection logs
- **Real-time Logging**: All injection attempts are logged
- **Detection Statistics**: View successful vs. failed attempts

## ⚠️ Important Notes

- **Educational Purpose Only**: This application contains intentional vulnerabilities
- **Do Not Use in Production**: Never deploy this code to production environments
- **Local Testing Only**: Designed for local security education

## 🎓 Learning Objectives

1. Understand SQL injection attack vectors
2. Learn to identify vulnerable code patterns
3. Practice secure coding techniques
4. Explore detection and prevention methods
5. Gain hands-on experience with web security

## 🔧 Technical Details

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Jinja2 templates
- **Security**: Intentionally vulnerable for educational purposes

## 📝 Next Steps

After exploring this playground, consider:
1. Implementing additional security measures
2. Adding more complex injection scenarios
3. Creating automated testing scripts
4. Exploring other web vulnerabilities (XSS, CSRF, etc.)

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new vulnerability scenarios
- Improve detection algorithms
- Enhance the UI/UX
- Add more educational content

---

**Remember**: Use this knowledge responsibly and only for educational purposes or authorized security testing.
