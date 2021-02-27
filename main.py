import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
        self.qp = QPainter()
        self.sign = False
        self.pushButton.clicked.connect(self.runDraw)

    def runDraw(self):
        self.sign = True
        self.repaint()

    def paintEvent(self, event):
        if self.sign:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(255, 255, 0))
            self.draw()
            self.qp.end()
            self.sign = False

    def get_coords_and_size(self):
        coords = random.randint(10, 420), random.randint(10, 380)
        size = random.randint(20, 70)
        return coords + (size, size)

    def draw(self):
        self.qp.drawEllipse(*self.get_coords_and_size())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.__excepthook__ = except_hook
    sys.exit(app.exec())
