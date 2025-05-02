from PyQt5.QtCore import Qt
from instr import *
from second_win import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
class FinalWin(QWidget):
    def __init__(self,exp):
        self.exp = exp
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
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results)
        self.index_text = QLabel(txt_index + str(self.index))
        