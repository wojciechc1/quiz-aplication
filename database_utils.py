import sqlite3

def fetch_questions():
    """
    Fetch 10 random questions from the questions table in the SQLite database.

    :return: A list of tuples, where each tuple represents a question and its options.
    """
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 10')    
    questions = c.fetchall()
    conn.close()
    return questions
