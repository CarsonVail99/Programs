import time
import datetime
import winsound
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMainWindow, QLineEdit
from PyQt5.QtCore import QTimer
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Alarm Clock')
        self.setGeometry(100, 100, 640, 480)
        self.central_widget = None
        self.layout = None
        self.time_label = None
        self.input_timer = None
        self.set_alarm_button = None
        self.alarm_time = None
        self.alarm_dt = None
        self.display_time = None
        self.timer = QTimer()

        self.initui()
        self.center()

    def center(self):
        size = self.geometry()
        screen = QApplication.desktop()
        x = (screen.width() - size.width()) / 2
        y = (screen.height() - size.height()) / 2
        self.move(int(x), int(y))

    def initui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.time_label = QLabel('',self)

        self.input_timer = QLineEdit()
        self.input_timer.setPlaceholderText('%H:%M:%S %m/%d/%Y')

        self.set_alarm_button = QPushButton('Set Alarm', self)
        self.set_alarm_button.clicked.connect(self.button_clicked)

        self.display_time = QLabel('')

        self.layout.addWidget(self.input_timer)
        self.layout.addWidget(self.set_alarm_button)
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.display_time)

        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.check_alarm)

    def button_clicked(self):
        self.alarm_time = self.input_timer.text().strip()
        if not self.alarm_time:
            self.time_label.setStyleSheet('color: red')
            self.time_label.setText('Enter a %H:%M:%S %m/%d/%Y')
            return

        try:
            self.alarm_dt = datetime.datetime.strptime(self.alarm_time, '%H:%M:%S %m/%d/%Y')
        except ValueError:
            self.time_label.setStyleSheet('color: red')
            self.time_label.setText('Invalid Time. Enter a %H:%M:%S %m/%d/%Y')
            self.alarm_dt = None
            return

        now = datetime.datetime.now()
        if now >= self.alarm_dt:
            self.time_label.setStyleSheet('color: red')
            self.time_label.setText('Enter a time in the future')
            return

        self.time_label.setStyleSheet('color: green')
        self.time_label.setText(f'Alarm set for {self.alarm_dt.strftime("%H:%M:%S %m/%d/%Y")}')
        if not self.timer.isActive():
            self.timer.start()

    def check_alarm(self):
        if self.alarm_dt is None:
            self.timer.stop()
            return

        now = datetime.datetime.now()
        if now >= self.alarm_dt:
            self.timer.stop()
            self.time_label.setStyleSheet('color: red')
            self.time_label.setText(f'Wake Up\nThe time is {now.strftime("%H:%M:%S %m/%d/%Y")}')
            try:
                winsound.PlaySound('wakeup.wav',
                               winsound.SND_FILENAME)

            except Exception as e:
                print('e')
                winsound.Beep(1000, 1000)

        else:
            self.display_time.setText(f'The time is {now.strftime("%H:%M:%S %m/%d/%Y")}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
