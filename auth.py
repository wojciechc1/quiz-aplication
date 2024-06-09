import sqlite3
import hashlib

def register_user(username, password):
    """
    Registers a new user in the database.
    
    :param username: The username of the new user.
    :param password: The password of the new user.
    :return: True if registration is successful, False if the username already exists.
    """
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    """
    Logs in a user by checking the username and password.
    
    :param username: The username of the user.
    :param password: The password of the user.
    :return: True if login is successful, False otherwise.
    """
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password_hash))
    user = c.fetchone()
    conn.close()
    return user is not None
