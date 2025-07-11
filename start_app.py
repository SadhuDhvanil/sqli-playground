#!/usr/bin/env python3
"""
Simple startup script for the SQL Injection Playground
"""

import os
import sys
import sqlite3
from app import app, init_db

def main():
    print("="*60)
    print("🚀 SQL Injection Playground")
    print("="*60)
    
    # Initialize database
    print("📁 Initializing database...")
    try:
        init_db()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        sys.exit(1)
    
    # Test database connection
    print("🔍 Testing database connection...")
    try:
        conn = sqlite3.connect('database/vulnerable.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        user_count = cursor.fetchone()[0]
        conn.close()
        print(f"✅ Database ready - {user_count} users")
    except Exception as e:
        print(f"❌ Database connection test failed: {e}")
        sys.exit(1)
    
    print("🌐 Starting web server...")
    print("📱 Access the application at: http://localhost:5001")
    print("🔓 Try SQL injection on the login page!")
    print("🛑 Press Ctrl+C to stop the server")
    print("="*60)
    
    try:
        app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
