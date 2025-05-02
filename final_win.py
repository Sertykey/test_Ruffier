
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
        self.work_text = QLabel(txt_workheart + self.results)
        self.index_text = QLabel(txt_index + str(self.index))
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age>=15:
            if self.index>=15:
                return txt_res1
            elif 11<=self.index<15:
                return txt_res2
            elif 6<=self.index<11:
                return txt_res3
            elif 0.5<=self.index<6:
                return txt_res4
            elif self.index<=0.4:
                return txt_res5
        

# from PyQt5.QtCore import Qt
# from instr import *
# from second_win import *
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
# class FinalWin(QWidget):
#     def __init__(self,exp):
#         self.exp = exp
#     def results(self):
#         self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
#         if self.exp.age>=15:
#             if self.index>=15:
#                 return txt_res1
#             elif 11<=self.index<15:
#                 return txt_res2
#             elif 6<=self.index<11:
#                 return txt_res3
#             elif 0.5<=self.index<6:
#                 return txt_res4
#             elif self.index<=0.4:
#                 return txt_res5
#     def initUI(self):
#         self.work_text = QLabel(txt_workheart + self.results)
#         self.index_text = QLabel(txt_index + str(self.index))
        
