import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Number Guessing Game')
        self.setGeometry(100, 100, 640, 480)
        self.guess_counter = 0
        self.increase_button = None
        self.decrease_button = None
        self.status = None
        self.enter_button = None
        self.computer_number = None
        self.number = None
        self.game_active = True
        self.initUI()
        self.center()

    def center(self):
        size = self.geometry()
        screen = QApplication.desktop().screenGeometry()
        x = (screen.width() - size.width()) / 2
        y = (screen.height() - size.height()) / 2
        self.move(int(x), int(y))


    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        central_widget.setLayout(layout)

        title = QLabel('Number Guessing Game\n Guess a number between 1-10', self)

        self.status = QLabel('Press Enter to Start a new game', self)

        self.increase_button = QPushButton('Increase Guess Count', self)
        self.increase_button.clicked.connect(self.button_clicked)

        self.decrease_button = QPushButton('Decrease Guess Count', self)
        self.decrease_button.clicked.connect(self.button_clicked)

        self.enter_button = QPushButton('Enter', self)
        self.enter_button.clicked.connect(self.button_clicked)

        self.number = QLabel('5', self)


        layout.addWidget(title, 0, 0, 1, 3)
        layout.addWidget(self.status, 0, 1, 1, 3)
        layout.addWidget(self.increase_button, 2, 2, 1, 1)
        layout.addWidget(self.decrease_button, 2, 0, 1, 1)
        layout.addWidget(self.number, 1, 2, 1, 1)
        layout.addWidget(self.enter_button, 2, 1, 1, 1)


    def button_clicked(self):
        action = self.sender()
        if action == self.increase_button:
            current_value = int(self.number.text())
            if current_value < 10:
                self.number.setText(str(current_value + 1))
        elif action == self.decrease_button:
            current_value = int(self.number.text())
            if current_value > 1:
                self.number.setText(str(current_value - 1 ))
        elif action == self.enter_button:
            if not self.game_active:
                self.start_new_game

    def start_new_game(self):
        self.game_active = True
        self.computer_number = random.randint(1,10)
        self.guess_counter = 0
        self.setText('Press Enter to Start a new game')

    def make_guess(self):
        if not self.game_active:
            return

        guessed_number = int(self.number.text())
        self.guess_counter += 1

        while self.guess_counter < 3:
            if self.guessed_number == self.computer_number:
                self.status.setStyleSheet('color: green')
                self.status.setText(f'You guessed the number in {self.guess_counter} tries!')
                break
            elif str(self.number_guessed) > str(self.computer_number):
                self.status.setStyleSheet('color: red')
                self.status.setText('Too high!')
                self.guess_counter += 1
            elif str(self.number_guessed) < str(self.computer_number):
                self.status.setStyleSheet('color: red')
                self.status.setText('Too low!')
                self.guess_counter += 1
        if self.guess_counter > 3:
            self.status.setStyleSheet('color: red')
            self.status.setText(f'You failed to guess the number in {self.guess_counter} tries!')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



