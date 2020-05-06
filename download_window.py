# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 360)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("QWidget#widget{background:#FFFFFF;border-radius:3px;box-shadow: 0 0 10px #f00; border:1px solid green}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_link = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit_link.setFont(font)
        self.textEdit_link.setStyleSheet("QTextEdit{background:Transparent;border:1px solid grey;}")
        self.textEdit_link.setObjectName("textEdit_link")
        self.verticalLayout.addWidget(self.textEdit_link)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_dir = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_dir.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_dir.setStyleSheet("QLineEdit{background:Transparent;border:1px solid grey}")
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.horizontalLayout_2.addWidget(self.lineEdit_dir)
        self.pushButton_choose_dir = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_choose_dir.setMinimumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_choose_dir.setFont(font)
        self.pushButton_choose_dir.setStyleSheet("QPushButton{background:Transparent;border:1px solid grey;border-radius:3px}\n"
"QPushButton:hover{background-color:rgba(102,153,255,0.6);}")
        self.pushButton_choose_dir.setObjectName("pushButton_choose_dir")
        self.horizontalLayout_2.addWidget(self.pushButton_choose_dir)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_thread = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_thread.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_thread.setFont(font)
        self.comboBox_thread.setStyleSheet("QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"")
        self.comboBox_thread.setObjectName("comboBox_thread")
        self.horizontalLayout_2.addWidget(self.comboBox_thread)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(373, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_start = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_start.setMinimumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton{background:Transparent;border:1px solid grey;border-radius:3px}\n"
"QPushButton:hover{background-color:rgba(102,153,255,0.6);}")
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_3.addWidget(self.pushButton_start)
        self.pushButton_quit = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_quit.setMinimumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_quit.setFont(font)
        self.pushButton_quit.setStyleSheet("QPushButton{background:Transparent;border:1px solid grey;border-radius:3px}\n"
"QPushButton:hover{background-color:rgba(102,153,255,0.6);}")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout_3.addWidget(self.pushButton_quit)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit_link.setPlaceholderText(_translate("Dialog", "请输入网址(目前支持http/https下载链接)"))
        self.pushButton_choose_dir.setToolTip(_translate("Dialog", "<html><head/><body><p>选择文件保存路径</p></body></html>"))
        self.pushButton_choose_dir.setText(_translate("Dialog", "选择目录"))
        self.label.setText(_translate("Dialog", "使用线程："))
        self.label_2.setText(_translate("Dialog", "请确保链接填写正确"))
        self.pushButton_start.setText(_translate("Dialog", "开始下载"))
        self.pushButton_quit.setText(_translate("Dialog", "取消"))
