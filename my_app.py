
from instr import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout,QVBoxLayout
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
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
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)
    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer_sits(self):
        # global time
        time = QTime(0,0,30)
        # self.timer = QTimer
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        # global time
        # time = QTime(0,0,30)
        # self.timer.timeout.connect(self.timer2Event)
        # time = time.addSecs(-1)
        # self.timer.start(1500)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer3Event(self):
        global time
        time = QTime(0,1,0)
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss")[6:8] >= 45 :
            self.text_timer.setStyleSheet("color: rgb(0,255,0")
        elif time.toString("hh:mm:ss") <= 15 :
            self.text_timer.setStyleSheet("color: rgb(0,255,0")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
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
        self.line_name = QLineEdit()
        self.line_name.setPlaceholderText(txt_name)
        self.line_age = QLineEdit()
        self.line_test1 = QLineEdit()
        self.line_age.setPlaceholderText(txt_age)
        # self.line_test1 = QLineEdit()
        self.line_test1.setPlaceholderText(txt_hinttest1)
        self.line_test2 = QLineEdit()
        self.line_test2.setPlaceholderText(txt_hinttest2)
        self.line_test3 = QLineEdit()
        self.line_test3.setPlaceholderText(txt_hinttest3)
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
