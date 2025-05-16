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
        if 13<=self.exp.age<=14:
            if self.index>=16.5:
                return txt_res1
            elif 12.5<=self.index<16.4:
                return txt_res2
            elif 7.5<=self.index<12.4:
                return txt_res3
            elif 2<=self.index<7.4:
                return txt_res4
            elif self.index<=1.9:
                return txt_res5
        if 11<=self.exp.age<=12:
            if self.index>=18:
                return txt_res1
            elif 14<=self.index<17.9:
                return txt_res2
            elif 9<=self.index<13.9:
                return txt_res3
            elif 3.5<=self.index<8.9:
                return txt_res4
            elif self.index<=3.4:
                return txt_res5
        if 9<=self.exp.age<=10:
            if self.index>=19.5:
                return txt_res1
            elif 15.5<=self.index<19.4:
                return txt_res2
            elif 10.5<=self.index<15.4:
                return txt_res3
            elif 5<=self.index<10.4:
                return txt_res4
            elif self.index<=4.9:
                return txt_res5
        if 7<=self.exp.age<=8:
            if self.index>=21:
                return txt_res1
            elif 17<=self.index<20.9:
                return txt_res2
            elif 12<=self.index<16.9:
                return txt_res3
            elif 6.5<=self.index<11.9:
                return txt_res4
            elif self.index<=6.4:
                return txt_res5    
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results)
        self.index_text = QLabel(txt_index + str(self.index))
        
        

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
        
