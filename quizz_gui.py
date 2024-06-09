import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt
from quizz import QuizGame
from auth import register_user, login_user

class QuizApp(QWidget):
    """
    A class representing the Quiz Application GUI.

    Inherits from QWidget.

    Methods:
        __init__
        initUI
        registerUI
        loginUI
        login
        register
        homeUI
        start_quiz
        quizUI
        check_answer
        show_message
        scoreUI
        clearLayout

    Attributes:
        No public attributes.
    """
    def __init__(self):
        """
        Initializes the QuizApp widget.

        This method initializes the QuizApp widget by calling the constructor of the QWidget class,
        setting up the user interface using the initUI method, and initializing the current_user attribute.

        :return: None
        """
        super().__init__()
        self.initUI()
        self.current_user = None

    def initUI(self):
        """
        Initializes the user interface for the Quiz Application.

        This method sets up the window title and geometry, creates buttons for playing as a guest, logging in, and registering,
        connects these buttons to their respective methods (homeUI, loginUI, registerUI), and arranges them vertically centered in the window.

        :return: None
        """
        self.setWindowTitle('Quiz App')
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter) # Center elements

        # Play as guest Button
        guest_button = QPushButton('Play as Guest', self) 
        guest_button.setFixedSize(150,60)
        guest_button.clicked.connect(self.homeUI)
        layout.addWidget(guest_button)

        # Login Button
        login_button = QPushButton('Login', self) 
        login_button.setFixedSize(150,60)
        login_button.clicked.connect(self.loginUI)
        layout.addWidget(login_button)

        # Register Button
        register_button = QPushButton('Register', self) 
        register_button.setFixedSize(150,60)
        register_button.clicked.connect(self.registerUI)
        layout.addWidget(register_button)

        self.setLayout(layout)

    def registerUI(self):
        """
        Sets up the user interface for the registration form.

        This method clears the existing layout, creates input fields for name, password, and confirmation password,
        sets up echo mode for password fields to hide the input, creates a register button,
        connects the register button to the register method, and adds all elements to the layout.

        :return: None
        """
        self.clearLayout(self.layout()) # Clear layout

        layout = QVBoxLayout()

        name_label = QLabel('Name:', self)
        self.name_input = QLineEdit(self)
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)

        confirm_label = QLabel('Confirm Password:', self)
        self.confirm_input = QLineEdit(self)
        self.confirm_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(confirm_label)
        layout.addWidget(self.confirm_input)

        register_button = QPushButton('Register', self)
        register_button.clicked.connect(self.register)
        layout.addWidget(register_button)

        self.layout().addLayout(layout)

    def loginUI(self):
        """
        Sets up the user interface for the login form.

        This method clears the existing layout, creates input fields for username and password,
        sets up echo mode for the password field to hide the input, creates a login button,
        connects the login button to the login method, and adds all elements to the layout.

        :return: None
        """
        self.clearLayout(self.layout()) # Clear layout

        layout = QVBoxLayout()

        name_label = QLabel('Name:', self)
        self.name_input = QLineEdit(self)
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)

        login_button = QPushButton('Login', self)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        self.layout().addLayout(layout)

    def login(self):
        """
        Logs in the user with the provided username and password.

        This method retrieves the username and password entered by the user,
        attempts to log in using the login_user function,
        sets the current_user attribute if login is successful,
        navigates to the home screen (homeUI) if login is successful,
        and displays a success or error message using the show_message method.

        :return: None
        """
        username = self.name_input.text()
        password = self.password_input.text()
        if login_user(username, password):
            self.current_user = username
            self.homeUI()
            self.show_message('Login successful')
        else:
            self.show_message('Invalid username or password')

    def register(self):
        """
        Registers a new user with the provided name and password.

        This method retrieves the name, password, and confirm password entered by the user,
        checks if the password matches the confirm password,
        registers the user using the register_user function if the passwords match,
        navigates to the home screen (homeUI) if registration is successful,
        and displays a success or error message using the show_message method.

        :return: None
        """
        name = self.name_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_input.text()

        if password != confirm_password:
            self.show_message('Passwords do not match')
        else:
            register_user(name, password)
            self.homeUI()
            self.show_message('User registered successfully')

    def homeUI(self):
        """
        Sets up the user interface for the home screen.

        This method clears the existing layout, creates a button to start the quiz,
        connects the button to the start_quiz method, and adds the button to the layout.

        :return: None
        """
        self.clearLayout(self.layout()) # Clear layout

        layout = QVBoxLayout()

        # Start Game Button
        start_button = QPushButton('Start Quiz', self)
        start_button.setFixedSize(150,60)
        start_button.clicked.connect(self.start_quiz)
        layout.addWidget(start_button)

        self.layout().addLayout(layout)

    def start_quiz(self):
        """
        Starts the quiz by initializing the QuizGame, retrieving questions, and setting up the quiz user interface.

        This method initializes a new instance of the QuizGame class,
        retrieves questions from the game using the get_questions method,
        sets the question index to zero to start from the first question,
        and sets up the quiz user interface using the quizUI method.

        :return: None
        """
        self.game = QuizGame()
        self.questions = self.game.get_questions()   # Get questions
        self.question_index = 0
        self.quizUI()

    def quizUI(self):
        """
        Sets up the user interface for the quiz.

        This method clears the existing layout, retrieves the current question from the list of questions,
        creates buttons for each answer option, connects each button to the check_answer method with the corresponding answer index,
        and adds all elements to the layout.

        :return: None
        """
        self.clearLayout(self.layout()) # Clear layout

        q = self.questions[self.question_index]

        layout = QVBoxLayout()

        # Question 
        question_label = QLabel(q[1], self)
        layout.addWidget(question_label)

        # Answers layout (Buttons)
        answer1_button = QPushButton(q[2], self)
        answer2_button = QPushButton(q[3], self)
        answer3_button = QPushButton(q[4], self)
        answer4_button = QPushButton(q[5], self)

        answer1_button.clicked.connect(lambda: self.check_answer(1, q[6]))
        answer2_button.clicked.connect(lambda: self.check_answer(2, q[6]))
        answer3_button.clicked.connect(lambda: self.check_answer(3, q[6]))
        answer4_button.clicked.connect(lambda: self.check_answer(4, q[6]))

        layout.addWidget(answer1_button)
        layout.addWidget(answer2_button)
        layout.addWidget(answer3_button)
        layout.addWidget(answer4_button)

        self.layout().addLayout(layout)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks the user's answer against the correct answer, updates the score, and progresses to the next question or finishes the quiz.

        This method compares the user's answer with the correct answer,
        increments the score if the answer is correct,
        increments the question index to move to the next question,
        calls the quizUI method to display the next question if there are more questions,
        or calls the scoreUI method to display the final score if all questions have been answered.

        :param user_answer: The index of the answer chosen by the user.
        :param correct_answer: The index of the correct answer for the current question.
        :return: None
        """
        if self.game.check_answer(user_answer, correct_answer):
            self.game.score += 1

        self.question_index += 1

        if (self.question_index < len(self.questions)):
            self.quizUI()
        else:
            self.scoreUI()
        
    def show_message(self, message):
        """
        Displays a message dialog with the specified message.

        This method creates a QMessageBox dialog with an information icon,
        sets the message text and title, adds an OK button,
        and displays the dialog to the user.

        :param message: The message to be displayed in the dialog.
        :return: None
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  
        msg.setText(message)  
        msg.setWindowTitle('Message')  
        msg.setStandardButtons(QMessageBox.Ok)  
        msg.exec_()  

        
    def scoreUI(self):
        """
        Sets up the user interface to display the final score.

        This method clears the existing layout, creates a label to display the user's score,
        creates a button to return to the home screen, and adds both elements to the layout.

        :return: None
        """
        self.clearLayout(self.layout())
        
        layout = QVBoxLayout()
        
        # Score message
        score_label = QLabel(f'Zdobyles {self.game.score} punktow na 10', self)
        layout.addWidget(score_label, alignment=Qt.AlignCenter)

        # Restart button
        restart_button = QPushButton('Home', self)
        restart_button.clicked.connect(self.homeUI)
        layout.addWidget(restart_button, alignment=Qt.AlignCenter)

        self.layout().addLayout(layout)
    
    def clearLayout(self, layout):
        """
        Clears all widgets and layouts from the provided layout.

        This method removes all child widgets and layouts recursively from the specified layout.

        :param layout: The layout to be cleared.
        :return: None
        """
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clearLayout(child.layout())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuizApp()
    ex.show()
    sys.exit(app.exec_())
