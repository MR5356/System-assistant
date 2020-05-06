import os

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import  QMessageBox
from download_window import Ui_Dialog
from PyQt5 import QtWidgets, QtCore


class Download_UI(Ui_Dialog, QtWidgets.QDialog):
    mySignal = pyqtSignal(list)

    def __init__(self):
        super(Download_UI, self).__init__()
        self.setupUi(self)
        self.m_flag = False
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 窗口始终置顶
        self.pushButton_quit.clicked.connect(self.close)
        self.pushButton_start.clicked.connect(self.startDownload)
        for i in range(16):
            self.comboBox_thread.addItem(str(i+1))
        self.comboBox_thread.setCurrentIndex(7)
        self.textEdit_link.textChanged.connect(self.linkChanged)
        self.pushButton_choose_dir.clicked.connect(self.chooseDir)

    def linkChanged(self):
        if self.textEdit_link.toPlainText().strip()[:4] == 'http':
            self.lineEdit_dir.setText(f"{self.lineEdit_dir.text()}{os.path.basename(self.textEdit_link.toPlainText().strip())}")
        else:
            pass

    def chooseDir(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        fileName = os.path.basename(self.textEdit_link.toPlainText().strip())
        if fileName:
            self.lineEdit_dir.setText(f"{directory}/{fileName}")
        else:
            self.lineEdit_dir.setText(f"{directory}/")

    def startDownload(self):
        url = self.textEdit_link.toPlainText().strip()
        thread = self.comboBox_thread.currentIndex() + 1
        fileName = self.lineEdit_dir.text()
        if url[:4] != 'http':
            self.textEdit_link.clear()
            self.lineEdit_dir.setText('')
            self.textEdit_link.setPlaceholderText("当前程序仅支持http/https协议的下载链接")
        elif fileName == '':
            self.textEdit_link.clear()
            self.textEdit_link.setPlaceholderText("文件保存路径设置不正确，请重新查看")
        else:
            self.mySignal.emit([url, thread, fileName])
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:  # 重写Esc键事件
            pass
        elif e.key() == Qt.Key_Enter:
            pass