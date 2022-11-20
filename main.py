import sys
from random import randint


from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint


class NewWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.drawCircleButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            radius = randint(10, 100)
            x = randint(radius, self.width() - radius)
            y = randint(radius, self.height() - radius - self.drawCircleButton.height())
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(QPoint(x, y), radius, radius)
            qp.end()
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wdg = NewWidget()
    wdg.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
