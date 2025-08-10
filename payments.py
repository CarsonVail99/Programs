import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QPushButton
from PyQt5.QtWidgets import QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Checkout')
        self.setGeometry(100, 100, 640, 480)
        self.payment_method = QLabel('Select Payment Method:', self)
        self.setStyleSheet('background-color: lightgray;''font-size: 30px;')
        self.something = QIcon('who is me.png')
        self.setWindowIcon(self.something)
        self.payments()
        self.selected_ship()
        self.selected_pay()
        self.picture()
    def payments(self):
        self.payment1 = (QRadioButton('MasterCard', self))
        self.payment2 = (QRadioButton('Visa', self))
        self.payment3 = (QRadioButton('Discovery', self))
        self.payment4 = (QRadioButton('Paypal', self))
        self.payment1.setGeometry(10, 50, 630, 50)
        self.payment2.setGeometry(10, 100, 630, 50)
        self.payment3.setGeometry(10, 150, 630, 50)
        self.payment4.setGeometry(10, 200, 630, 50)
        self.shipping_method1 = (QRadioButton('5-7 Day Shipping ', self))
        self.shipping_method2 = (QRadioButton('Instant Shipping', self))
        self.payment_method.setGeometry(10, 0, 630, 50)
        for radio in (self.payment1, self.payment2, self.payment3, self.payment4):
            radio.setStyleSheet('font-size: 20px;')
        for shipping in (self.shipping_method1, self.shipping_method2):
            shipping.setStyleSheet('font-size: 20px;')
        self.shipping_method1.setGeometry(10, 335, 630, 25)
        self.shipping_method2.setGeometry(10, 385, 630, 25)
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.payment1)
        self.radio_group.addButton(self.payment2)
        self.radio_group.addButton(self.payment3)
        self.radio_group.addButton(self.payment4)
        self.shipping_group = QButtonGroup()
        self.shipping_group.addButton(self.shipping_method1)
        self.shipping_group.addButton(self.shipping_method2)
        self.next = QPushButton('Next', self)
        self.next.setGeometry(5, 420, 630, 50)
        self.next.setStyleSheet(
            'border-color: black;'
            'background-color: gray;'
            'font-size: 20px;'
            'border-style: solid'
            'border-width: 3px;')
        self.next.clicked.connect(self.confirm)
        self.payment1.toggled.connect(self.radio_toggled)
        self.payment2.toggled.connect(self.radio_toggled)
        self.payment3.toggled.connect(self.radio_toggled)
        self.payment4.toggled.connect(self.radio_toggled)
        self.shipping_method1.toggled.connect(self.shipping_toggled)
        self.shipping_method2.toggled.connect(self.shipping_toggled)

    def radio_toggled(self):
        if self.payment1.isChecked():
            self.selected_payment.setText('MasterCard Selected')
        elif self.payment2.isChecked():
            self.selected_payment.setText('Visa Selected')
        elif self.payment3.isChecked():
            self.selected_payment.setText('Discovery Selected')
        elif self.payment4.isChecked():
            self.selected_payment.setText('Paypal Selected')

    def shipping_toggled(self):
        if self.shipping_method1.isChecked():
            self.selected_shipping.setText('5-7 Day Shipping Selected')
        else:
            self.selected_shipping.setText('Instant Shipping Selected')

    def confirm(self):
        self.setStyleSheet('font-size: 20px')
        self.next.setText('Thank you!\nclick to exit')
        self.next.setStyleSheet('background-color: green;')
        self.next.clicked.connect(self.close)
    def selected_ship(self):
        self.selected_shipping = QLabel('', self)
        self.selected_shipping.setGeometry(10, 300, 630, 25)
        self.selected_shipping.setStyleSheet('font-size: 20px;')
    def selected_pay(self):
        self.selected_payment = QLabel('', self)
        self.selected_payment.setGeometry(10, 250, 630, 25)
        self.selected_payment.setStyleSheet('font-size: 20px;')

    def picture(self):
        self.picture = QLabel(self)
        self.picture.setPixmap(QPixmap('bag.png'))
        self.picture.setScaledContents(True)
        self.picture.setGeometry(582, 422, 44, 44)
        self.picture.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()