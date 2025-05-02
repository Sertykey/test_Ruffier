from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout,QVBoxLayout
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def connects(self):
        pass

    def initUI(self):
        self.text_index = QLabel(txt_index)
        self.txt_workheart = QLabel(txt_workheart)
        self.c_line = QVBoxLayout()
        self.c_line.addWidget(self.txt_index,alignment=Qt.AlignCenter)
        self.c_line.addWidget(self.txt_workheart,alignment=Qt.AlignCenter)