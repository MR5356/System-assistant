import hashlib
import os
import subprocess
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import qApp, QMessageBox
import qtawesome
import requests
import json
from update_ui import Ui_MainWindow


class fun_main(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, argv):
        super(fun_main, self).__init__()
        self.setupUi(self)
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 主窗口透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 窗口始终置顶
        self.show_message("正在进行初始化...")

        # 初始化参数
        self.m_flag = False
        self.com_flag = False
        self.argv = argv
        self.progressBar.setValue(0)

        # 功能绑定
        self.pushButton_close.clicked.connect(self.close_win)
        self.pushButton_min.clicked.connect(lambda: self.showMinimized())
        # self.pushButton_close.clicked.connect(lambda: self.showMinimized())

        # 图标绑定
        self.pushButton_min.setIcon(qtawesome.icon('fa.window-minimize', color='blank'))
        self.pushButton_close.setIcon(qtawesome.icon('fa.close', color='blank'))
        self.show_message("更新程序初始化完成")
        if len(argv) < 2:
            self.show_message("更新参数初始化失败，请尝试重新进行更新")
        else:
            self.show_message("更新参数初始化完成")
            self.show_message(f"更新网址已经设置为：{argv[1]}")
            self.show_message(f"正在连接更新服务器...")
            self.req_thread(argv[1])

    # 运行展示框添加数据
    def show_message(self, msm):
        self.textEdit.append(msm)

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

    # 线程区
    def req_thread(self, url):
        try:
            self.req_Thread = Requests_Thread(url)
            self.req_Thread.thread_signal.connect(self.Req_UI)
            self.req_Thread.start()
        except Exception as e:
            print(f"Time Thread: {e}")
            self.show_message(f"连接服务器出错，请尝试重新启动。错误信息如下：")
            self.show_message(f"{e}")

    def Req_UI(self, msm):
        if msm.get('error', 0) == 1:
            self.show_message(f"连接服务器出错，请检查网络连接，尝试重启软件进行更新")
        else:
            self.show_message(f"服务器数据获取成功，开始对比更新文件...")
            self.progressBar.setValue(10)
            self.compare_Thread = Compare_Thread(msm, os.path.split(self.argv[1])[0])
            self.compare_Thread.thread_signal.connect(self.Com_UI)
            self.compare_Thread.start()

    def Com_UI(self, msm):
        if "jindu" in msm:
            num = int(msm.replace('jindu', ''))
            self.progressBar.setValue(num)
        if "更新失败" in msm and "jindu" not in msm:
            self.com_flag = True
            self.show_message(msm)
        elif msm == "更新完成" and self.com_flag == False and "jindu" not in msm:
            self.show_message("更新完成，更新程序即将退出")
            subprocess.Popen(f"{self.argv[2]}")
            qApp.exit(0)
        elif not self.com_flag != False and "jindu" not in msm:
            self.show_message(msm)


class Requests_Thread(QThread):
    thread_signal = pyqtSignal(dict)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        for i in range(4):
            try:
                req = requests.get(self.url, timeout=3).text
                result = json.loads(req)
                self.thread_signal.emit(result)
                break
            except Exception as e:
                print(f"req thread: {e}")
                if i == 3:
                    self.thread_signal.emit({'error': 1})


class Compare_Thread(QThread):
    thread_signal = pyqtSignal(str)

    def __init__(self, files, url):
        super().__init__()
        self.files = files
        self.url = url

    def run(self):
        local_files = {}
        path = "./"  # os.path.dirname(os.path.realpath(__file__))
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if ('.git' and 'dist' and '.idea') not in dirpath:
                    file = os.path.join(dirpath.split('./')[1], filename)
                    self.thread_signal.emit(f"{file}")
                    fhash = self.get_file_md5(file)
                    local_files[file] = fhash
        self.thread_signal.emit('jindu20')
        # 进行对比
        up_files = []
        for i in self.files:
            if local_files.get(i) and local_files.get(i) == self.files[i]:
                self.thread_signal.emit(f"{i}：无需更新")
            else:
                up_files.append(i)
        self.thread_signal.emit(f"共有{len(up_files)}个文件需要更新")
        self.thread_signal.emit('jindu25')
        for i in up_files:
            durl = f"{self.url}/{i}"
            self.thread_signal.emit(f"{i}：发现新版本，正在从{durl}下载更新...")
            for j in range(4):
                try:
                    patch = requests.get(durl).content
                    with open(f"{i}", "wb") as f:
                        f.write(patch)
                    self.thread_signal.emit(f"{i}更新完成")
                    break
                except:
                    if j == 3:
                        self.thread_signal.emit(f"{i}更新失败")
            self.thread_signal.emit(f'jindu{25 + int((up_files.index(i) + 1) / len(up_files) * 75)}')
        self.thread_signal.emit(f"更新完成")

    def get_file_md5(self, file_path):
        """
        获取文件md5值
        :param file_path: 文件路径名
        :return: 文件md5值
        """
        with open(file_path, 'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            _hash = md5obj.hexdigest()
        return str(_hash).upper()
