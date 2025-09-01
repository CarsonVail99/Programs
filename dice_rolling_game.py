import random
import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget
                            ,QLabel, QVBoxLayout, QPushButton, QDesktopWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.winning_score = 3
        self.center()
        self.initUI()
        self.show()

    def center(self):
        #Get geometry of the screen
        screen = QDesktopWidget().screenGeometry()

        #Get the geometry of the window
        size = self.geometry()

        #Center the window
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))


    def initUI(self):
        #Create Window
        self.setWindowTitle('Dice Rolling Game')
        self.setGeometry(0, 0, 400, 400)

        #Create a central widget and main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        #Window Icon
        self.setWindowIcon(QIcon('dice.jpeg'))

        #Create score display
        self.score_label = QLabel(f'Player score: {self.player_score} Computer score: {self.computer_score}')
        self.score_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.score_label.setFont(QFont('Arial', 25))

        #Declare Winner
        self.winner_label = QLabel('')
        self.winner_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.winner_label.setFont(QFont('Arial', 25))

        #Create roll results display
        self.dice_rolled = QLabel('')
        self.dice_rolled.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.dice_rolled.setFont(QFont('Arial', 25))

        #Roll dice Widget
        self.rolldice_widget = QPushButton('Roll Dice')
        self.rolldice_widget.clicked.connect(self.roll)
        self.rolldice_widget.setFont(QFont('Arial', 25))

        #Exit Widget
        exit_widget = QPushButton('Exit')
        exit_widget.clicked.connect(self.close)
        exit_widget.setFont(QFont('Arial', 25))

        #New Game Widget
        self.new_game_widget = QPushButton('Play Again')
        self.new_game_widget.clicked.connect(self.play_again)
        self.new_game_widget.setFont(QFont('Arial', 25))
        self.new_game_widget.hide()

        #Add widgets to a layout
        self.layout.addWidget(self.dice_rolled)
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.rolldice_widget)
        self.layout.addWidget(exit_widget)
        self.layout.addWidget(self.new_game_widget)
        self.layout.addWidget(self.winner_label)


    def computer_roll(self):
        return random.randint(1,12)

    def player_roll(self):
        return random.randint(1,12)

    def roll(self):
        while True:
            if self.player_score == self.winning_score:
                self.winner_label.setStyleSheet('color: green')
                self.winner_label.setText('You Won!')
                self.rolldice_widget.setEnabled(False)
                self.new_game_widget.show()

            elif self.computer_score == self.winning_score:
                self.winner_label.setText('Computer Won!')
                self.winner_label.setStyleSheet('color: red')
                self.rolldice_widget.setEnabled(False)
                self.new_game_widget.show()


            player_roll = self.player_roll()
            computer_roll = self.computer_roll()
            self.dice_rolled.setText(f'Player rolled: {player_roll} Computer rolled:{computer_roll}')
            if player_roll > computer_roll:
                self.player_score += 1
                self.score_label.setText(f'Player Score: {self.player_score} Computer Score: {self.computer_score}')
                return self.player_score
            elif computer_roll > player_roll:
                self.computer_score += 1
                self.score_label.setText(f'Player Score: {self.player_score} Computer Score: {self.computer_score}')
                return self.computer_score
            elif player_roll == computer_roll:
                self.score_label.setText(f'Player Score: {self.player_score} Computer Score: {self.computer_score}')
                return None
            else:
                continue

    def play_again(self):
        self.player_score = 0
        self.computer_score = 0
        self.winner_label.setText('')
        self.dice_rolled.setText('')
        self.score_label.setText(f'Player Score: {self.player_score} Computer Score: {self.computer_score}')
        self.rolldice_widget.setEnabled(True)




def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
