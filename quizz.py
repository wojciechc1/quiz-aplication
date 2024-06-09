from database_utils import fetch_questions

class QuizGame:
    """
    A class representing the Quiz Game logic.

    Methods:
        __init__: Initializes the QuizGame with a score of 0.
        get_questions: Retrieves questions for the quiz.
        check_answer: Checks the correctness of the user's answer.

    Attributes:
        score: An integer representing the player's current score.
    """
    def __init__(self):
        self.score = 0
    
    def get_questions(self): 
        return fetch_questions()

    def check_answer(self, answer, correct_answer):
        # Check if the answer is correct
        return True if answer == correct_answer else False
                          
