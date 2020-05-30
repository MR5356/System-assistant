import hashlib
import os
import subprocess
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import qApp, QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QListWidgetItem
import qtawesome
from main_window import Ui_MainWindow
from Sub_Thread import Time_Thread
from Sub_Thread import Source_Thread
from Sub_Thread import Article_Thread
from Sub_Thread import Update_Thread
from Sub_Thread import Downloader_Thread
import soft_cfg

md5obj = hashlib.md5()
file = os.path.realpath(__file__)


def open_browser(url):
    QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))


# 源码仓库item
def get_item_source(msms):
    # 读取属性
    title = msms[0]
    info = msms[1]
    language = msms[2]
    url = msms[3]

    wight = QWidget()
    wight.setObjectName("widget_main")
    wight.setStyleSheet(
        "QWidget#widget_main{background:Transparent;border:0px solid grey;}QWidget#widget_main:hover{background-color:rgba(240,245,255,0.8);}")
    wight.setMinimumSize(QtCore.QSize(0, 100))
    wight.setMaximumSize(QtCore.QSize(16777215, 100))
    layout_main = QHBoxLayout()
    layout_main.setContentsMargins(11, 0, 11, 0)
    layout_main.setSpacing(6)
    layout_right = QVBoxLayout()
    layout_right_down = QHBoxLayout()  # 右下的横向布局

    pushButton_info = QtWidgets.QPushButton()
    pushButton_info.setStyleSheet(
        "QPushButton{background:Transparent;border:0px solid grey;text-align:left;color:Gray}")
    pushButton_info.setIcon(qtawesome.icon('fa.info-circle', color="Green"))
    pushButton_info.setText("")
    # pushButton_info.setWordWrap(True)
    layout_right_down.addWidget(pushButton_info)

    label_info = QtWidgets.QLabel()
    label_info.setStyleSheet("QLabel{background:Transparent;border:0px solid grey;}")
    font = QtGui.QFont()
    font.setFamily("微软雅黑")
    # font.setPointSize(7)
    label_info.setFont(font)
    label_info.setText(info)
    # label_info.setWordWrap(True)
    layout_right_down.addWidget(label_info)

    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    layout_right_down.addItem(spacerItem)

    layout_right_up = QHBoxLayout()  # 右上的横向布局
    label_tag = QtWidgets.QLabel()
    label_tag.setAlignment(QtCore.Qt.AlignCenter)
    label_tag.setStyleSheet("QLabel{background:Transparent;border:1px solid grey;border-radius:5px;}")
    label_tag.setMaximumHeight(20)
    font = QtGui.QFont()
    font.setFamily("微软雅黑")
    font.setPointSize(7)
    label_tag.setFont(font)
    label_tag.setText(f" {language} ")
    layout_right_up.addWidget(label_tag)
    label_title = QtWidgets.QLabel()
    font = QtGui.QFont()
    font.setFamily("微软雅黑")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(50)
    label_title.setFont(font)
    label_title.setText(title)
    layout_right_up.addWidget(label_title)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    layout_right_up.addItem(spacerItem)
    layout_right.addLayout(layout_right_up)  # 右边的纵向布局
    layout_right.addLayout(layout_right_down)  # 右下角横向布局
    layout_main.addLayout(layout_right)  # 右边的布局
    wight.setLayout(layout_main)  # 布局给wight
    return wight  # 返回wight


class fun_main(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(fun_main, self).__init__()
        self.setupUi(self)
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 主窗口透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 窗口始终置顶

        # 初始化功能
        self.signal_on_btn()
        self.icon_on_btn()

        # 初始化参数
        self.m_flag = False
        self.source_url = []  # 源码仓库链接初始化
        self.article_url = []  # 文章教程链接初始化
        self.label_10.hide()
        self.label_sys_info.hide()
        self.label_welcome.setText(soft_cfg.welcome)

        # 线程启动
        self.time_thread()
        self.source_thread()
        self.article_thread()
        self.webDownloader_Thread = Downloader_Thread()
        self.webDownloader_Thread.start()
        self.update_thread()

    def signal_on_btn(self):
        # 基础按钮事件绑定
        self.pushButton_close.clicked.connect(lambda: self.window_close(0))
        self.pushButton_min.clicked.connect(lambda: self.showMinimized())
        self.pushButton_feedback.clicked.connect(lambda: open_browser(soft_cfg.feed_back))
        self.pushButton_web_site.clicked.connect(lambda: open_browser(soft_cfg.web_site))
        self.pushButton_help_us.clicked.connect(lambda: open_browser(soft_cfg.help_us))
        self.pushButton_web_rights.clicked.connect(self.licenses)
        self.pushButton_update.clicked.connect(self.update_thread)

        # List Widget点击事件
        self.listWidget_source.itemClicked.connect(self.source_item_clicked)
        self.listWidget_article.itemClicked.connect(self.article_item_clicked)

        # 界面转换
        self.pushButton_menu_soft.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        # self.pushButton_menu_api.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_menu_api.clicked.connect(self.open_api_site)
        self.pushButton_menu_article.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_menu_source.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_menu_about_us.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        # self.pushButton_menu_downloader.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.pushButton_menu_downloader.clicked.connect(lambda: open_browser(soft_cfg.download_url))

    def icon_on_btn(self):
        self.pushButton_feedback.setIcon(qtawesome.icon('fa.envelope-o', color="blank"))
        self.pushButton_min.setIcon(qtawesome.icon('fa.window-minimize', color='blank'))
        self.pushButton_close.setIcon(qtawesome.icon('fa.close', color='blank'))
        self.pushButton_update.setIcon(qtawesome.icon('fa.arrow-circle-up', color='blank'))
        # 菜单栏图标
        self.pushButton_menu_about_us.setIcon(qtawesome.icon('fa.yelp', color='white'))
        self.pushButton_menu_api.setIcon(qtawesome.icon('fa.link', color='white'))
        self.pushButton_menu_article.setIcon(qtawesome.icon('fa.file-text', color='white'))
        self.pushButton_menu_source.setIcon(qtawesome.icon('fa.code', color='white'))
        self.pushButton_menu_soft.setIcon(qtawesome.icon('fa.th-large', color='white'))
        self.pushButton_menu_downloader.setIcon(qtawesome.icon('fa.download', color='white'))

    # 自定义功能区
    def window_close(self, code):
        res = QMessageBox.question(self, '是否关闭程序', '请确保没有下载任务', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if res == QMessageBox.Yes:
            self.webDownloader_Thread.stop()
            qApp.exit(code)
        else:
            pass

    def open_api_site(self):  # 接口文档 --跳转到API网页
        res = QMessageBox.question(self, '提示', '即将在浏览器中打开接口文档，需登录后才可使用本站API，是否继续？', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if res == QMessageBox.Yes:
            open_browser(soft_cfg.api_site)
        else:
            pass

    def licenses(self):
        self.stackedWidget.setCurrentIndex(1)
        self.textEdit_licenses.append(soft_cfg.licenses)
        scrollbar = self.textEdit_licenses.verticalScrollBar()
        scrollbar.setSliderPosition(0)

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

    # 线程区
    def time_thread(self):
        try:
            self.time_Thread = Time_Thread()
            self.time_Thread.thread_signal.connect(self.Time_UI)
            self.time_Thread.start()
        except Exception as e:
            print(f"Time Thread: {e}")
            QMessageBox.information(self, '时间进程发生错误', f'错误信息{e}，请尝试重启客户端，如问题还未解决，请点击反馈按钮留言')

    def Time_UI(self, msm):
        self.label_time.setText(f"{msm}")

    def source_thread(self):
        try:
            self.source_Thread = Source_Thread()
            self.source_Thread.thread_signal.connect(self.Source_UI)
            self.source_Thread.start()
        except Exception as e:
            print(f"Source Thread: {e}")
            QMessageBox.information(self, '源码仓库发生错误', f'错误信息{e}，请确定网络连接是否正常，然后尝试重启客户端，如问题还未解决，请点击反馈按钮留言')

    def Source_UI(self, msm):
        self.source_url = msm['url']
        try:
            self.listWidget_source.clear()
        except Exception as e:
            print(f"source function.py: {e}")
        for i in zip(msm['title'], msm['info'], msm['language'], msm['url']):
            item = QListWidgetItem()
            widget = get_item_source(i)
            item.setSizeHint(QSize(widget.width(), widget.height()))
            self.listWidget_source.addItem(item)
            self.listWidget_source.setItemWidget(item, widget)

    def source_item_clicked(self, item):
        open_browser(self.source_url[self.listWidget_source.currentIndex().row()])

    def article_thread(self):
        try:
            self.article_Thread = Article_Thread()
            self.article_Thread.thread_signal.connect(self.Article_UI)
            self.article_Thread.start()
        except Exception as e:
            print(f"Article Thread: {e}")
            QMessageBox.information(self, '文章教程发生错误', f'错误信息{e}，请确定网络连接是否正常，然后尝试重启客户端，如问题还未解决，请点击反馈按钮留言')

    def Article_UI(self, msm):
        self.article_url = msm['url']
        try:
            self.listWidget_article.clear()
        except Exception as e:
            print(f"article function.py: {e}")
        for i in zip(msm['title'], msm['info'], msm['date'], msm['url']):
            item = QListWidgetItem()
            widget = get_item_source(i)
            item.setSizeHint(QSize(widget.width(), widget.height()))
            self.listWidget_article.addItem(item)
            self.listWidget_article.setItemWidget(item, widget)

    def article_item_clicked(self, item):
        open_browser(self.article_url[self.listWidget_article.currentIndex().row()])

    def update_thread(self, auto=True):
        try:
            self.update_Thread = Update_Thread(auto)
            self.update_Thread.display_signal.connect(self.Update_UI)
            self.update_Thread.start()
        except:
            QMessageBox.information(self, '小助手提示', '程序运行异常，请确定网络连接是否正常，然后尝试重启客户端，如问题还未解决，请点击反馈按钮留言')

    def Update_UI(self, msm):
        if msm['Version'] <= soft_cfg.version:
            if not msm["auto"] != False:
                QMessageBox.information(self, '小助手提示', '已经是最新版本')
            else:
                pass
        else:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '发现新版本，是否立即更新',
                                                   f'发现新版本：V{msm["Version"]}，更新内容如下：\n\n{msm["Update_des"]}\n\n是否立即更新?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                subprocess.Popen(f"update_main.exe {msm['Update_url']} {soft_cfg.name}")
                qApp.exit(0)
            else:
                pass
