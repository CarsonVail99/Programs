import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QMainWindow, QLineEdit
import datetime
from PyQt5.QtGui import QIcon, QFont

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log Program")
        self.setGeometry(100, 100, 640, 480)
        self.initui()
        self.center()

    def center(self):
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        x = int((screen.width() - size.width()) / 2)
        y = int((screen.height() - size.height()) / 2)
        self.move(x, y)

    def initui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.header = QLabel('Log Your Day With Alt! Always Stay Greatful, And Get Actually Paid By The Higher Reality You Saw!')
        self.header.setFont(QFont('Arial', 15))
        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText('Alts Message or Directory of png')

        self.line_edit2 = QLineEdit()
        self.line_edit2.setPlaceholderText('Resemblance To Message')

        self.enter_button = QPushButton('Enter')
        self.enter_button.clicked.connect(self.button_clicked)

        self.vbox = QVBoxLayout()
        self.central_widget.setLayout(self.vbox)

        self.vbox.addWidget(self.header)
        self.vbox.addWidget(self.line_edit1)
        self.vbox.addWidget(self.line_edit2)
        self.vbox.addWidget(self.enter_button)

    def button_clicked(self):
        message = self.line_edit1.text()
        resemblance = self.line_edit2.text()
        time = datetime.datetime.now()
        with open('log.txt', 'a') as file:
            file.write(f'{time}\n{message} - {resemblance}')
        self.line_edit1.clear()
        self.line_edit2.clear()



def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
