import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("QT_test_1.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class DialogClass(QDialog, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.run_btn_1)
        self.btn_2.clicked.connect(self.run_btn_2)
        self.btn_3.clicked.connect(self.run_btn_clear)
        self.count = 0

    def run_btn_1(self):
        self.count += 1
        self.label.setText("Count : %02d" % self.count)

    def run_btn_2(self):
        self.count += -1
        self.label.setText("Count : %02d" % self.count)

    def run_btn_clear(self):
        self.count = 0
        self.label.setText("Count : %02d" % self.count)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # DialogClass의 인스턴스 생성
    myDialog = DialogClass()

    # 프로그램 화면을 보여주는 코드
    myDialog.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()