
# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from instr import *
from second_win import *
from final_win import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.iniUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
    def initUI(self): 
        self.button = QPushButton(txt_next)
        self.hello = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.v_line = QVBoxLayout()
        v_line.addWidget(self.hello, alignment = Qt.AlignCenter)
        v_line.addWidget(self.instruction, alignment = Qt.AlignCenter)
        v_line.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(v_line)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())
        self.tw = FinalWin(self.exp)


        
