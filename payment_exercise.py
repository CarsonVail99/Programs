import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Push Buttons Exercise")
        self.setGeometry(700, 700, 400, 400)
        self.label = clickable_label("Hello", self)
        self.initui()





    def initui(self):
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(100, 150, 200, 100)
        self.button.setStyleSheet("font-size: 20px;")
        self.button.clicked.connect(self.on_click)#signel "clicked" connect to a slot self."on_click"
        self.label.setGeometry(200, 100, 200, 50)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(100, 100, 50, 50)
        self.image_label.setPixmap(QPixmap("bag.png"))
        self.image_label.setScaledContents(True)



    def on_click(self):
        print("Clicked!")
        self.button.setText("Clicked Button!") #changes text on button within initui
        self.button.setDisabled(True) #disable the button after one click

    def clicked_label(self):
        print("Clicked Label!")
        self.label.setText("Clicked Label!")
        self.label.setDisabled(True)

class clickable_label(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.parent = parent

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent.clicked_label()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()