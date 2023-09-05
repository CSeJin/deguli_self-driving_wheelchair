# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'emrCall.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_EmrCall(QMainWindow):
    # 변수 정의
    btn_home = None
        
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1021, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_title = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_title.setContentsMargins(0, 0, 0, 0)
        self.layout_title.setObjectName("layout_title")
        Ui_EmrCall.btn_home = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_EmrCall.btn_home.sizePolicy().hasHeightForWidth())
        Ui_EmrCall.btn_home.setSizePolicy(sizePolicy)
        Ui_EmrCall.btn_home.setMinimumSize(QtCore.QSize(180, 0))
        Ui_EmrCall.btn_home.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        Ui_EmrCall.btn_home.setFont(font)
        Ui_EmrCall.btn_home.setStyleSheet("margin-left: 20px;\n"
                                    "background-color: #cfe3ac;\n"
                                    "padding: 5px 0;")
        Ui_EmrCall.btn_home.setObjectName("btn_home")
        self.layout_title.addWidget(Ui_EmrCall.btn_home)
        self.title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("text-align: center;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.layout_title.addWidget(self.title)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(180, 0))
        self.pushButton_6.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("margin-left: 20px;\n"
"background-color: #cfe3ac;\n"
"padding: 10px 0;")
        self.pushButton_6.setText("")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.layout_title.addWidget(self.pushButton_6)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 119, 1021, 402))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_contents = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.layout_contents.setContentsMargins(0, 0, 0, 0)
        self.layout_contents.setObjectName("layout_contents")
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout_contents.addItem(spacerItem)
        self.layout_contents_inside = QtWidgets.QVBoxLayout()
        self.layout_contents_inside.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout_contents_inside.setObjectName("layout_contents_inside")
        self.emr_light_img = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emr_light_img.sizePolicy().hasHeightForWidth())
        self.emr_light_img.setSizePolicy(sizePolicy)
        self.emr_light_img.setMinimumSize(QtCore.QSize(403, 345))
        self.emr_light_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.emr_light_img.setStyleSheet("background: url(./assets/emr_light.png);\n"
"background-size: cover;")
        self.emr_light_img.setText("")
        self.emr_light_img.setObjectName("emr_light_img")
        self.layout_contents_inside.addWidget(self.emr_light_img)
        self.emr_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emr_label.sizePolicy().hasHeightForWidth())
        self.emr_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.emr_label.setFont(font)
        self.emr_label.setStyleSheet("padding: 10px;")
        self.emr_label.setObjectName("emr_label")
        self.emr_label.setStyleSheet("background-color: none;")
        self.layout_contents_inside.addWidget(self.emr_label, 0, QtCore.Qt.AlignHCenter)
        self.layout_contents.addLayout(self.layout_contents_inside)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout_contents.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 519, 1021, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layout_bottom = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_bottom.setContentsMargins(0, 0, 0, 0)
        self.layout_bottom.setObjectName("layout_bottom")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        Ui_EmrCall.btn_home.setText(_translate("MainWindow", "HOME"))
        self.title.setText(_translate("MainWindow", "긴급호출"))
        self.emr_label.setText(_translate("MainWindow", "관리자 호출 중"))