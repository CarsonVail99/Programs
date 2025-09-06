import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 640, 480)
        self.enter_button = None
        self.length = None
        self.status = None
        self.line_edit = None

        self.initUI()
        self.center()


    def center(self):
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        x = int((screen.width() - size.width()) / 2)
        y = int((screen.height() - size.height()) / 2)
        self.move(x, y)


    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.status = QLabel('')

        self.enter_button = QPushButton('Enter')
        self.enter_button.clicked.connect(self.button_clicked)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Enter Password Length between 8-16')

        icon = QIcon('C:/Users/Admin/PycharmProjects/Programs/password_icon.png')
        self.setWindowIcon(icon)

        image = QPixmap('C:/Users/Admin/PycharmProjects/Programs/password_icon.png')

        image_label = QLabel()
        image_label.setPixmap(image)

        layout = QVBoxLayout()

        central_widget.setLayout(layout)

        layout.addWidget(self.status)

        layout.addWidget(image_label)

        layout.addWidget(self.line_edit)

        layout.addWidget(self.enter_button)


    def button_clicked(self):
        self.length = self.line_edit.text()
        if self.length.isdigit():
            self.length = int(self.length)
            if self.length >= 8 and self.length <= 16:
                self.pw_generate()
            else:
                self.status.setText('That integer is not within the range 8-16')


    def pw_generate(self):
        letters = string.ascii_letters
        digits = string.digits
        special_char = string.punctuation
        all_char = letters + digits + special_char
        password = ''.join(random.choice(all_char) for i in range(self.length))
        self.line_edit.setText(password)
        self.status.setStyleSheet('color: green')
        self.status.setText('Password Generated')


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

