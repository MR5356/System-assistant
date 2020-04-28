from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import qApp, QMessageBox
import qtawesome
from update_ui import Ui_MainWindow


class fun_main(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(fun_main, self).__init__()
        self.setupUi(self)
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 主窗口透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 窗口始终置顶
        self.textEdit.append("界面初始化完成")

        # 初始化参数
        self.m_flag = False
        self.textEdit.append("参数初始化完成")

        # 功能绑定
        self.pushButton_close.clicked.connect(self.close_win)
        self.pushButton_min.clicked.connect(lambda: self.showMinimized())
        # self.pushButton_close.clicked.connect(lambda: self.showMinimized())

        # 图标绑定
        self.pushButton_min.setIcon(qtawesome.icon('fa.window-minimize', color='blank'))
        self.pushButton_close.setIcon(qtawesome.icon('fa.close', color='blank'))
        self.textEdit.append("更新程序初始化完成")
        for i in range(100):
            self.textEdit.append(f"{i}")

    # 界面拖动
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

    def close_win(self):
        res = QMessageBox.question(self, '请再次确认', '更新进行中，请再次确认是否退出', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if res == QMessageBox.Yes:
            qApp.exit(0)
        else:
            pass
