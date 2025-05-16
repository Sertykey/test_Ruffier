
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
        self.setStyleSheet('background:rgb(245,12,160)')
    def connects(self):
        pass
    def timer_test(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        pass
    def next_click(self):
        self.hide()
        self.tw = FinalWin()
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())
        self.tw = FinalWin(self.exp)
    def initUI(self):
       
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.btn_next.setStyleSheet('border: 5px solid rgb(133, 85, 230); background:rgb(136, 112, 184); font-size: 30px')
        self.btn_test1.setStyleSheet('border: 5px solid rgb(133,85,230); background:rgb(136,112,184)')
        self.btn_test2.setStyleSheet('border: 5px solid rgb(133,85,230); background:rgb(136,112,184)')
        self.btn_test3.setStyleSheet('border: 5px solid rgb(133,85,230); background:rgb(136,112,184)')
        self.text_name = QLabel(txt_hintname)
        self.text_age = QLabel(txt_hintage)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.line_name = QLineEdit(txt_name)
        self.line_age = QLineEdit()
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



# app =QApplication([])
# Pup = TestWin()
# app.exec_()
