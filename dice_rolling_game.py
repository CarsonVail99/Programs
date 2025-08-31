import random
import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget
                            ,QLabel, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dice Rolling Game')
        self.setGeometry(1400, 800, 300, 300)

        #create a central widget and main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        #create score display
        self.score_label = QLabel(f'Player score: 0 Computer score: 0')
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setFont(QFont('Arial', 18))

        #create roll results display
        rolldice_widget = QPushButton('Roll Dice', self)
        rolldice_widget.clicked.connect(self.player_roll)
        dice_rolled = QLabel('')
        exit_widget = QPushButton('Exit',self)
        exit_widget.clicked.connect(self.close)

        #Add widgets to a layout
        layout.addWidget(dice_rolled)
        layout.addWidget(self.score_label)
        layout.addWidget(rolldice_widget)
        layout.addWidget(exit_widget)

    @staticmethod
    def computer_roll(self):
        return random.randint(1,12)

    @staticmethod
    def player_roll(self):
        self.computer_roll(self)
        return random.randint(1,12)

    def game(self):
        player_score = 0
        computer_score = 0
        while player_score < 3 and computer_score < 3:
            comp_roll = self.computer_roll(self)
            play_roll = self.player_roll(self)
            if self.computer_roll(self) > self.player_roll(self):
                computer_score += 1
                self.score_label.setText(f'Player score: {player_score} Computer score: {computer_score})

            elif play_roll > comp_roll:
                player_score += 1
                print(f'player rolled: {play_roll}, computer rolled: {comp_roll} \n'
                f'Player won!\nPlayer score is:', player_score, f'Computer score is:', computer_score)
            elif play_roll == comp_roll:
                print(f'Both you and computer rolled same number, Reroll')
            else:
                print("Invalid input")
        if player_score == 3:
            print(f'Player won!\nPlayer score is:', player_score, f'Computer score is:', computer_score)
            return False
        else:
            print(f'Computer won!\nPlayer score is:', player_score, f'Computer score is:', computer_score)
            return False

    # @staticmethod
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
