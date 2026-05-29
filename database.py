import sqlite3

DB_FILE = 'students.db'

def get_connection():
    """Establish and return a database connection."""
    return sqlite3.connect(DB_FILE)

def initialize_db():
    """Create the students table if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade REAL NOT NULL,
            attendance REAL NOT NULL,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def execute_query(query, params=()):
    """Execute INSERT, UPDATE, or DELETE queries."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
    except sqlite3.IntegrityError as e:
        conn.close()
        raise e  # Passes the error to operations.py to handle duplicate IDs
    finally:
        conn.close()

def fetch_query(query, params=()):
    """Execute SELECT queries and return data."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results