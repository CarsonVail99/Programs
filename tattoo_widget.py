from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QImage, QTransform
from PyQt5.QtCore import Qt, QRect
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tattoo")
        self.setGeometry(100, 100, 800, 1100)
        self.initUI()
        self.center()


    def center(self):
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        x = int((screen.width() - size.width()) / 2)
        y = int((screen.height() - size.height()) / 2)
        self.move(x, y)


    def initUI(self):
        # Create and set the central widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        #Create a grid layout
        layout = QGridLayout(main_widget)

        #Load the script as black and white via QImage
        script_png = QPixmap('tattoo_script.png')
        script_image = script_png.toImage()
        grayscale_image = script_image.convertToFormat(QImage.Format_Grayscale8)
        grayscale_image = QPixmap.fromImage(grayscale_image)#convert script to QPixmap
        grayscale_image = grayscale_image.scaled(800, 300)

        #Set the background image Black and White
        background_jpg = QPixmap('tattoo_script_setstylesheet_background.jpg')
        background_image_1 = background_jpg.toImage()
        grayscale_background_1 = background_image_1.convertToFormat(QImage.Format_Grayscale8)

        #crop background image
        crop_area = QRect(5, 250, 650, 1290)
        cropped_image = grayscale_background_1.copy(crop_area)
        grayscale_background_1 = QPixmap.fromImage(cropped_image)#convert background1 back to QPixmap
        grayscale_background_1 = grayscale_background_1.scaled(400, 800)

        #copy the cropped image and flip
        grayscale_background_2 = grayscale_background_1.copy()
        transform = QTransform().scale(-1, 1)
        grayscale_background_2 = grayscale_background_2.transformed(transform)

        #Create new Label and set the image
        black_label = QLabel()
        black_label.setPixmap(grayscale_image)
        background_label1 = QLabel()
        background_label1.setPixmap(grayscale_background_1)
        background_label2 = QLabel()
        background_label2.setPixmap(grayscale_background_2)


        layout.addWidget(black_label, 0, 0, 1, 12)
        layout.addWidget(background_label1, 1, 0, 5, 6)
        layout.addWidget(background_label2, 1, 6, 5, 6)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
