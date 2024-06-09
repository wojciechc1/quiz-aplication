import sqlite3
import json
import os

def setup_database():
    """
    Set up the SQLite database and create the necessary tables if they don't exist.
    """
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    # Create the questions table
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL
        )
    ''')

    # Create the users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def load_questions_from_json(file_path):
    """
    Load questions from a JSON file and insert them into the questions table.

    :param file_path: The path to the JSON file containing the questions.
    """
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    # Open and read the JSON file
    with open(file_path, 'r') as jsonfile:
        questions = json.load(jsonfile)
        for question in questions:
            # Insert each question from the JSON file into the questions table
            c.execute('''
                INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (question['question'], question['option1'], question['option2'], question['option3'], question['option4'], question['correct_option']))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Set up the database and load questions from the JSON file
    setup_database()
    load_questions_from_json('questions.json')
