import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("ui_pic.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class DialogClass(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_load.clicked.connect(self.run_btn_load)
        self.fnameEdit.clear()

    def run_btn_load(self):
        path = 'img' # 시작하려는 폴더가 프로젝트 폴더의 하위에 존재하면 폴더 이름 입력
        filter = "All Images(*.jpg; *.png; *.bmp; *.jfif);;JPG(*.jpg);;PNG(*.png);;BMP(*.bmp);;JFIF(*.jfif)"
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "파일로드", path, filter)
        filename = str(fname[0])
        print(filename)

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(filename)
        self.lbl_photo.setPixmap(self.qPixmapFileVar) # QLabel.setPixmap() 함수로 픽스맵을 설정해주면 문자열 대신 이미지가 표시됩니다.
        self.lbl_photo.setScaledContents(True) # 라벨크기에 맞게 이미지 크기 조절
        self.fnameEdit.setText(filename)

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # DialogClass의 인스턴스 생성
    myDialog = DialogClass()

    # 프로그램 화면을 보여주는 코드
    myDialog.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


