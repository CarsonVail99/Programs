import sys
from PyQt5.QtWidgets import QCheckBox, QMainWindow, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from datetime import datetime

data_time=[]
jobs = []
class Second_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,640,480)
        self.setStyleSheet("background-color:grey;")
        self.setWindowTitle("To Do List")
        self.icon = QIcon("who is me.png")
        self.setWindowIcon(self.icon)
        self.initUI()

    def initUI(self):
        self.checkbox()
        self.header()
        self.go_back_button()

    def checkbox(self):
        self.important_widget = QLabel('Talk to Alt\nIts always speaking to you')
        self.important_widget.setGeometry(10, 10, 630, 100)
        self.important_widget.setStyleSheet('font-size: 20px;')
        self.central_widget = QWidget()
        self.central_widget.setGeometry(10, 10, 630, 400)
        self.setCentralWidget(self.central_widget)
        self.vbox = QVBoxLayout(self.central_widget)
        self.vbox.addWidget(self.important_widget)
        for job in jobs:
            self.show_checkbox = QCheckBox(f'{job}', self)
            self.show_checkbox.setStyleSheet('font-size: 20px;')
            self.vbox.addWidget(self.show_checkbox)

    def header(self):
        Title = QLabel("Tasks", self)
        Title.setGeometry(10, 10, 630, 40)
        Title.setStyleSheet('font-size: 30px;')

    def go_back_button(self):
        self.back = QPushButton('Back', self)
        self.back.setGeometry(400, 420, 100, 50)
        self.back.clicked.connect(self.go_back_func)

    def go_back_func(self):
        self.First_Window = First_Window()
        self.First_Window.show()
        self.hide()


class First_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,640,480)
        self.initUI()
        self.Second_Window = None

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.icon = QIcon("who is me.png")
        self.setWindowIcon(self.icon)
        self.setStyleSheet("background-color:grey;")
        self.linedit()
        self.next_button()
        self.add_task_button()
        self.close_button()
    def linedit(self):
        self.line = QLineEdit(self)
        self.line.setPlaceholderText('Enter Task Here...')
        self.line.setGeometry(10, 10, 540, 40)
        self.line.setStyleSheet('font-size: 20px;')

    def add_task_button(self):
        self.add_task = QPushButton('Add Task', self)
        self.add_task.setGeometry(10, 100, 630, 55)
        try:
            self.add_task.clicked.connect(self.handle_add_task)
        except Exception:
            pass

    def handle_add_task(self):
        jobs.append(self.line.text())
        self.line.clear()

    def next_button(self):
        self.next = QPushButton('show tasks', self)
        self.next.setGeometry(5, 420, 630, 50)
        self.next.clicked.connect(self.open_second_window)


    def open_second_window(self):
        self.Second_Window = Second_Window()
        self.Second_Window.show()
        self.hide()

    def close_button(self):
        self.close_button = QPushButton('Close/Save', self)
        self.close_button.setGeometry(5, 360, 630, 50)
        self.close_button.clicked.connect(self.save_data)

    def save_data(self):
        data_extractor()
        self.close()



def data_extractor():
    now = datetime.now()
    current_time = now.strftime('%y-%m-%d %H:%M:%S') + 100*'*'+ ('Alt is always speaking to you')
    with open('important_data.txt', 'a') as f:
        f.write(f'{100*"*"}\n{current_time}\n{jobs}\n{100*"*"}{'Listen'}')



def main():
    app = QApplication(sys.argv)
    window = First_Window()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()





