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
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def connects(self):
        pass

    def initUI(self):
       
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.l_line.addWidget(self.text_name)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_age,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_age,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_test1,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.btn_test1,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_test1,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_test2,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.btn_test2,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_test3,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.btn_test3,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_test2,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.line_test3,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.btn_next)
        self.r_line.addWidget(self.text_timer,alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)



app =QApplication([])
Pup = TestWin()

app.exec_ ()