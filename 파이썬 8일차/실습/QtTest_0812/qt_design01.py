# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(863, 555)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.lbl_result = QtWidgets.QLabel(dialog)
        self.lbl_result.setGeometry(QtCore.QRect(30, 420, 831, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_result.setFont(font)
        self.lbl_result.setObjectName("lbl_result")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(dialog)
        self.spinBox.setGeometry(QtCore.QRect(190, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1900)
        self.spinBox.setMaximum(2021)
        self.spinBox.setProperty("value", 2000)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(360, 40, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(300, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(12)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(380, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(31)
        self.spinBox_3.setObjectName("spinBox_3")
        self.btn_update = QtWidgets.QPushButton(dialog)
        self.btn_update.setGeometry(QtCore.QRect(470, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_update.setFont(font)
        self.btn_update.setObjectName("btn_update")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 100, 281, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radio_1.setFont(font)
        self.radio_1.setObjectName("radio_1")
        self.horizontalLayout.addWidget(self.radio_1)
        self.radio_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radio_2.setFont(font)
        self.radio_2.setObjectName("radio_2")
        self.horizontalLayout.addWidget(self.radio_2)
        self.radio_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radio_3.setFont(font)
        self.radio_3.setChecked(True)
        self.radio_3.setObjectName("radio_3")
        self.horizontalLayout.addWidget(self.radio_3)
        self.radio_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radio_4.setFont(font)
        self.radio_4.setObjectName("radio_4")
        self.horizontalLayout.addWidget(self.radio_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 200, 411, 171))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_1.setFont(font)
        self.chk_1.setObjectName("chk_1")
        self.verticalLayout.addWidget(self.chk_1)
        self.chk_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_2.setFont(font)
        self.chk_2.setObjectName("chk_2")
        self.verticalLayout.addWidget(self.chk_2)
        self.chk_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_3.setFont(font)
        self.chk_3.setObjectName("chk_3")
        self.verticalLayout.addWidget(self.chk_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chk_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_4.setFont(font)
        self.chk_4.setObjectName("chk_4")
        self.verticalLayout_2.addWidget(self.chk_4)
        self.chk_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_5.setFont(font)
        self.chk_5.setObjectName("chk_5")
        self.verticalLayout_2.addWidget(self.chk_5)
        self.chk_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_6.setFont(font)
        self.chk_6.setObjectName("chk_6")
        self.verticalLayout_2.addWidget(self.chk_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "조수익"))
        self.label.setText(_translate("dialog", "성별"))
        self.lbl_result.setText(_translate("dialog", "성별 생년월일"))
        self.label_2.setText(_translate("dialog", "년"))
        self.label_3.setText(_translate("dialog", "월"))
        self.label_4.setText(_translate("dialog", "일"))
        self.btn_update.setText(_translate("dialog", "업데이트"))
        self.label_5.setText(_translate("dialog", "출생지역"))
        self.radio_1.setText(_translate("dialog", "서울"))
        self.radio_2.setText(_translate("dialog", "대구"))
        self.radio_3.setText(_translate("dialog", "순천"))
        self.radio_4.setText(_translate("dialog", "기타"))
        self.chk_1.setText(_translate("dialog", "영화"))
        self.chk_2.setText(_translate("dialog", "맛집"))
        self.chk_3.setText(_translate("dialog", "여행"))
        self.chk_4.setText(_translate("dialog", "노래방"))
        self.chk_5.setText(_translate("dialog", "유튜브"))
        self.chk_6.setText(_translate("dialog", "노래"))
        self.label_6.setText(_translate("dialog", "취미"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
