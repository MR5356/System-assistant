from PyQt5.QtCore import QThread, pyqtSignal
import time
import requests, json
import soft_cfg


class Time_Thread(QThread):
    thread_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.thread_signal.emit(result)
            time.sleep(soft_cfg.time_thread)


class Source_Thread(QThread):
    thread_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                if soft_cfg.debug:
                    raise ConnectionError("测试数据")
                result = requests.get(soft_cfg.source_api_url, timeout=3).text
            except Exception as e:
                print(f"source result info: {e}")
                result = soft_cfg.source_api
            result = json.loads(result)
            self.thread_signal.emit(result)
            time.sleep(soft_cfg.source_thread)


class Article_Thread(QThread):
    thread_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                if soft_cfg.debug:
                    raise ConnectionError("测试数据")
                result = requests.get(soft_cfg.article_api_url, timeout=3).text
            except Exception as e:
                print(f"source result info: {e}")
                result = soft_cfg.article_api
            result = json.loads(result)
            self.thread_signal.emit(result)
            time.sleep(soft_cfg.article_thread)