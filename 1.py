import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Knopka1.ui", self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.start)
        self.x, self.y, self.r = 100, 100, 0

    def start(self):
        self.paintEvent(self.event)
        self.x, self.y, self.r = randint(0, 700), randint(0, 500), randint(0, 300)

    def paintEvent(self, event):
        ris = QPainter()
        ris.begin(self)
        ris.setBrush(QColor(255, 255, 0))
        ris.drawEllipse(self.x, self.y, self.r, self.r)
        self.update()
        ris.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
