from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QGridLayout, QDesktopWidget,
                             QMainWindow, QLineEdit,QButtonGroup)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status = QLineEdit('')
        self.number1 = None
        self.number2 = None
        self.operator = None
        self.initui()
        self.center()


    def center(self):
        #Move to Center of screen
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x = int((screen.width() - size.width()) / 2)
        y = int((screen.height() - size.height()) / 2)
        self.move(x, y)


    def initui(self):
        #Create Base Window w/ Layout

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid = QGridLayout()
        central_widget.setLayout(grid)

        #Create 1-9 Buttons
        for i in range(9):
            button = QPushButton(str(i + 1))
            button.clicked.connect(self.number_clicked)
            grid.addWidget(button, i // 3, i % 3)

        #create 0 Button
        button_zero = QPushButton('0')
        button_zero.clicked.connect(self.number_clicked)
        grid.addWidget(button_zero, 0, 3)

        #Create Operating Buttons
        operating_buttons = ['+', '-', '*', '/']
        for i, op in enumerate(operating_buttons):
            op_button = QPushButton(op)#creates the buttons with operator text
            op_button.clicked.connect(self.operator_clicked)
            grid.addWidget(op_button, 4, i)

        #Create Status Bar
        self.status = QLineEdit()
        self.status.setReadOnly(True)
        grid.addWidget(self.status, 5, 0, 1, 4)#x and y placement then dimensions

        #Enter Button
        enter = QPushButton("Enter")
        enter.clicked.connect(self.enter_clicked)
        grid.addWidget(enter, 2, 3)

        #Clear Button
        clear = QPushButton("Clear")
        clear.clicked.connect(self.clear_clicked)
        grid.addWidget(clear, 1, 3, 1, 1)


    def number_clicked(self):
        button = self.sender()
        current_text = self.status.text()

        if self.operator is None:
            # First Number input
            if self.number1 is None:
                self.status.setText(button.text())
                self.number1 = int(button.text())
                #More than a single digit
            else:
                #appending old numbers to new numbers, more than a single digit
                self.number1 = int(str(self.number1) + button.text())
                self.status.setText(str(self.number1))

        else:
            #Second Number input
            if self.number2 is None:
                self.status.setText(button.text())
                self.number2 = int(button.text())
            else:#Appending old numbers to new numbers, more than a single digit
                self.number2 = int(str(self.number2) + button.text())
                self.status.setText(str(button.text()))


    def enter_clicked(self):
        if self.number1 is not None and self.number2 is not None:
            try:
                result = None
                if self.operator == '+':
                    result = self.number1 + self.number2
                elif self.operator == '-':
                    result = self.number1 - self.number2
                elif self.operator == '*':
                    result = self.number1 * self.number2
                elif self.operator == '/':
                    if self.number2 == 0:
                        self.status.setText('Cannot divide by zero!')
                        return
                    result = self.number1 / self.number2

                if result is not None:
                    self.status.setText(str(result))
                    self.number1 = result
                    self.number2 = None
                    self.operator = None

            except ValueError as e:
                self.status.setText(e)


    def clear_clicked(self):
        self.number1 = None
        self.number2 = None
        self.operator = None
        self.status.clear()


    def operator_clicked(self):
        button = self.sender()
        self.operator = button.text()
        self.status.clear()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


