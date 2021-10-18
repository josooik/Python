import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import uic
#from qt_design01 import Ui_dialog

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("user_info.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class DialogClass(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # pushButton과 연결
        self.btn_update.clicked.connect(self.run_btn_update)

        # 체크박스 클릭시 굵기 변경
        self.chk_1.stateChanged.connect(self.run_chk_state_changed)
        self.chk_2.stateChanged.connect(self.run_chk_state_changed)
        self.chk_3.stateChanged.connect(self.run_chk_state_changed)
        self.chk_4.stateChanged.connect(self.run_chk_state_changed)
        self.chk_5.stateChanged.connect(self.run_chk_state_changed)
        self.chk_6.stateChanged.connect(self.run_chk_state_changed)

        # ComboBox와 연결
        self.comboBox.currentIndexChanged.connect(self.comboBox_function)
        self.comboBox.addItem("남자")
        self.comboBox.addItem("여자")

    def run_chk_state_changed(self):
        chk_lists = [self.chk_1, self.chk_2, self.chk_3, self.chk_4, self.chk_5, self.chk_6]
        for list in chk_lists:
            if list.isChecked():
                list.setFont(QtGui.QFont("Gulim", 15, QtGui.QFont.Bold))
            else:
                list.setFont(QtGui.QFont("Gulim", 15))

    def comboBox_function(self):
        #str = f'성별 : {self.comboBox.currentText()}'
        #self.lbl_result.setText(str)
        pass

    def run_btn_update(self):
        age = 2021 - int(self.spinBox.cleanText())
        my_str = f'{self.comboBox.currentText()} {self.spinBox.cleanText()}년 {self.spinBox_2.cleanText()}월 {self.spinBox_3.cleanText()}일 나이 : {str(age)}'

        if self.radio_1.isChecked():
            my_str += " 출생지 : 서울"
        elif self.radio_2.isChecked():
            my_str += " 출생지 : 대구"
        elif self.radio_3.isChecked():
            my_str += " 출생지 : 순천"
        elif self.radio_4.isChecked():
            my_str += " 출생지 : 기타"

        my_str += '\n취미:'

        if self.chk_1.isChecked():
            my_str += " 영화"
        if self.chk_2.isChecked():
            my_str += " 맛집"
        if self.chk_3.isChecked():
            my_str += " 여행"
        if self.chk_4.isChecked():
            my_str += " 노래방"
        if self.chk_5.isChecked():
            my_str += " 유튜브"
        if self.chk_6.isChecked():
            my_str += " 노래"

        self.lbl_result.setText(my_str)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # DialogClass의 인스턴스 생성
    myDialog = DialogClass()

    # 프로그램 화면을 보여주는 코드
    myDialog.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


