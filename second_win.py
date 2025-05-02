from PyQt5.QtCore import Qt, QTimer, QTime
from instr import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, 
class TestWin(QWidget):
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
