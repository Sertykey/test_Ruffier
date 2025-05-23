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
        self.setStyleSheet("background:rgb(245, 12, 160)")
    def iniUI(self): 
        self.button = QPushButton(txt_next)
        self.button.setStyleSheet("border: 5px solid rgb(133, 85, 230); background:rgb(136, 112, 184); font-size: 30px; padding: 10px; border-radius: 15px")
        self.hello = QLabel(txt_hello)
        self.hello.setStyleSheet('font-size: 30px')
        self.instruction = QLabel(txt_instruction)
        self.instruction.setStyleSheet('font-size: 15px')
        self.v_line = QVBoxLayout()
        self.setLayout(self.v_line)
        self.v_line.addWidget(self.hello, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.button, alignment = Qt.AlignCenter)
        
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    
app =QApplication([])
winpup = MainWin()
app.exec_()
