from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import sqlite3
import hashlib
import os
import time
import logging
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'vulnerable_secret_key_123'  # Intentionally weak secret

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

# Database setup
DATABASE = 'database/vulnerable.db'

def init_db():
    """Initialize the database with sample data"""
    conn = sqlite3.connect(DATABASE, timeout=10.0)
    conn.execute('PRAGMA journal_mode=WAL;')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    
    # Create injection_logs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS injection_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            user_agent TEXT,
            query TEXT,
            payload TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            success BOOLEAN DEFAULT 0
        )
    ''')
    
    # Insert sample users
    sample_users = [
        ('admin', hashlib.md5('admin123'.encode()).hexdigest(), 'admin@example.com', 'admin'),
        ('user1', hashlib.md5('password1'.encode()).hexdigest(), 'user1@example.com', 'user'),
        ('john_doe', hashlib.md5('secret123'.encode()).hexdigest(), 'john@example.com', 'user'),
        ('alice_smith', hashlib.md5('mypassword'.encode()).hexdigest(), 'alice@example.com', 'user'),
        ('bob_wilson', hashlib.md5('password123'.encode()).hexdigest(), 'bob@example.com', 'user'),
        ('sarah_jones', hashlib.md5('test123'.encode()).hexdigest(), 'sarah@example.com', 'user'),
        ('mike_davis', hashlib.md5('qwerty'.encode()).hexdigest(), 'mike@example.com', 'user'),
        ('emily_brown', hashlib.md5('letmein'.encode()).hexdigest(), 'emily@example.com', 'user'),
        ('david_clark', hashlib.md5('123456'.encode()).hexdigest(), 'david@example.com', 'user'),
        ('lisa_white', hashlib.md5('password'.encode()).hexdigest(), 'lisa@example.com', 'user')
    ]
    
    for username, password, email, role in sample_users:
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, password, email, role)
            VALUES (?, ?, ?, ?)
        ''', (username, password, email, role))
    
    
    conn.commit()
    conn.close()

def log_injection_attempt(query, payload, success=False):
    """Log potential SQL injection attempts"""
    try:
        conn = sqlite3.connect(DATABASE, timeout=10.0)
        conn.execute('PRAGMA journal_mode=WAL;')  # Use WAL mode for better concurrency
        cursor = conn.cursor()
        
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')
        
        cursor.execute('''
            INSERT INTO injection_logs (ip_address, user_agent, query, payload, success)
            VALUES (?, ?, ?, ?, ?)
        ''', (ip_address, user_agent, query, payload, success))
        
        conn.commit()
        
        # Also log to file
        logging.warning(f"SQL Injection attempt: IP={ip_address}, Query={query}, Payload={payload}, Success={success}")
        
    except Exception as e:
        logging.error(f"Failed to log injection attempt: {e}")
    finally:
        try:
            conn.close()
        except:
            pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # VULNERABLE: Direct string concatenation in SQL query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{hashlib.md5(password.encode()).hexdigest()}'"
        
        # Log the query for detection
        log_injection_attempt(query, f"username={username}, password={password}")
        
        try:
            conn = sqlite3.connect(DATABASE, timeout=10.0)
            conn.execute('PRAGMA journal_mode=WAL;')
            cursor = conn.cursor()
            
            # Execute the vulnerable query
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                session['role'] = user[4]
                
                # Enhanced injection detection for different difficulty levels
                injection_indicators = [
                    "'", '--', '/*', '*/', 'UNION', 'SELECT', 'OR', 'AND', 
                    'SLEEP', 'EXTRACTVALUE', 'CONCAT', 'LENGTH', 'COUNT',
                    'SUBSTRING', 'ASCII', 'CHAR', 'DATABASE', 'VERSION'
                ]
                
                user_input = f"{username} {password}".upper()
                if any(indicator.upper() in user_input for indicator in injection_indicators):
                    log_injection_attempt(query, f"username={username}, password={password}", success=True)
                
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials!', 'error')
                
        except sqlite3.Error as e:
            # This reveals database errors - another vulnerability
            flash(f'Database error: {str(e)}', 'error')
            log_injection_attempt(query, f"username={username}, password={password}", success=False)
        finally:
            try:
                conn.close()
            except:
                pass
    
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # VULNERABLE: Show user data based on session
    query = f"SELECT * FROM users WHERE id = {session['user_id']}"
    
    try:
        conn = sqlite3.connect(DATABASE, timeout=10.0)
        conn.execute('PRAGMA journal_mode=WAL;')
        cursor = conn.cursor()
        cursor.execute(query)
        user = cursor.fetchone()
        
        # If admin, show all users (for demonstration)
        if session.get('role') == 'admin':
            cursor.execute("SELECT id, username, email, role FROM users")
            all_users = cursor.fetchall()
        else:
            all_users = []
        
        return render_template('dashboard.html', user=user, all_users=all_users)
    
    except sqlite3.Error as e:
        flash(f'Database error: {str(e)}', 'error')
        return redirect(url_for('login'))
    finally:
        try:
            conn.close()
        except:
            pass

@app.route('/secure-login', methods=['GET', 'POST'])
def secure_login():
    """Secure version using parameterized queries"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # SECURE: Using parameterized query
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        try:
            conn = sqlite3.connect(DATABASE, timeout=10.0)
            conn.execute('PRAGMA journal_mode=WAL;')
            cursor = conn.cursor()
            
            # Execute the secure query
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            
            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                session['role'] = user[4]
                flash('Secure login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials!', 'error')
                
        except sqlite3.Error as e:
            flash('Authentication failed!', 'error')  # Don't reveal database errors
            logging.error(f"Secure login error: {e}")
        finally:
            try:
                conn.close()
            except:
                pass
    
    return render_template('secure_login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/logs')
def view_logs():
    """View injection attempt logs (admin only)"""
    if session.get('role') != 'admin':
        flash('Access denied!', 'error')
        return redirect(url_for('index'))
    
    try:
        conn = sqlite3.connect(DATABASE, timeout=10.0)
        conn.execute('PRAGMA journal_mode=WAL;')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM injection_logs ORDER BY timestamp DESC LIMIT 50")
        logs = cursor.fetchall()
        
        return render_template('logs.html', logs=logs)
    
    except sqlite3.Error as e:
        flash(f'Error loading logs: {str(e)}', 'error')
        return redirect(url_for('dashboard'))
    finally:
        try:
            conn.close()
        except:
            pass

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='127.0.0.1', port=5001, threaded=True)
