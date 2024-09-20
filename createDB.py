import sqlite3

def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS apartments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            apt_no TEXT UNIQUE,
            block TEXT,
            sq_feet INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            apt_no TEXT,
            name TEXT,
            mobile TEXT,
            gender TEXT,
            amount REAL,
            pay_status BOOLEAN,
            FOREIGN KEY (apt_no) REFERENCES apartments (apt_no) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    conn.close()

def add_apartment(apt_no, block, sq_feet):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO apartments (apt_no, block, sq_feet) VALUES (?, ?, ?)
        ''', (apt_no, block, sq_feet))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Apt No must be unique!")
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
        ''', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Username must be unique!")
    conn.close()

def add_user_detail(apt_no, name, mobile, gender, amount, pay_status):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO user_details (apt_no, name, mobile, gender, amount, pay_status) VALUES (?, ?, ?, ?, ?, ?)
        ''', (apt_no, name, mobile, gender, amount, pay_status))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Apartment must exist!")
    conn.close()

create_database()

add_apartment('A201', 'Block A', 1200)
add_apartment('A202', 'Block B', 1300)

add_user('root', 'root')
add_user('raja', 'raja')
add_user('rani', 'rani')

add_user_detail('A201', 'raja', '1234567890', 'M', 20814, False)
add_user_detail('A202', 'rani', '4987654321', 'F', 25000, True)