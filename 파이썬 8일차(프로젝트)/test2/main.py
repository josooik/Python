import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("design.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class DialogClass(QDialog, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_blue.clicked.connect(self.run_btn_blue)
        self.btn_red.clicked.connect(self.run_btn_red)
        self.btn_green.clicked.connect(self.run_btn_green)
        self.btn_clear.clicked.connect(self.run_btn_clear)
        self.btn_undo.clicked.connect(self.run_btn_undo)

        self.btn_blue.setStyleSheet('QPushButton {color: blue;}')
        self.btn_red.setStyleSheet('QPushButton {color: red;}')
        self.btn_green.setStyleSheet('QPushButton {color: green;}')

        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.totalC = self.count1 + self.count2 + self.count3
        self.action = []

    def run_btn_blue(self):
        self.action.append('Blue')
        print(self.action)
        self.count1 += 1
        self.totalC += 1
        self.totalCount.setText("Count : %02d" % self.totalC)
        self.label_1.setText("%02d" % self.count1)

    def run_btn_red(self):
        self.action.append('Red')
        print(self.action)
        self.count2 += 1
        self.totalC += 1
        self.totalCount.setText("Count : %02d" % self.totalC)
        self.label_2.setText("%02d" % self.count2)

    def run_btn_green(self):
        self.action.append('green')
        print(self.action)
        self.count3 += 1
        self.totalC += 1
        self.totalCount.setText("Count : %02d" % self.totalC)
        self.label_3.setText("%02d" % self.count3)

    def run_btn_clear(self):
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.totalC = 0
        self.action = []
        print(self.action)
        self.totalCount.setText("Count : %02d" % self.totalC)
        self.label_1.setText("%02d" % self.count1)
        self.label_2.setText("%02d" % self.count2)
        self.label_3.setText("%02d" % self.count3)

    def run_btn_undo(self):

        if len(self.action) != 0:
            last_action = self.action.pop()
        else:
            return

        if last_action == 'Blue':
            self.count1 -= 1
            self.label_1.setText("%02d" % self.count1)

        if last_action == 'Red':
            self.count2 -= 1
            self.label_2.setText("%02d" % self.count2)

        if last_action == 'green':
            self.count3 -= 1
            self.label_3.setText("%02d" % self.count3)



if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # DialogClass의 인스턴스 생성
    myDialog = DialogClass()

    # 프로그램 화면을 보여주는 코드
    myDialog.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()