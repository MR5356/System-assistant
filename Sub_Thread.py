from PyQt5.QtCore import QThread, pyqtSignal
import time
import requests
import json
import os
import subprocess
import soft_cfg


def cache_data(name, msm=None):
    if msm:
        with open(f"{name}.json", "w") as f:
            f.write(json.dumps(msm))
    else:
        with open(f"{name}.json", "r") as f:
            return f.readline()


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
                    result = soft_cfg.source_api
                else:
                    result = requests.get(soft_cfg.source_api_url, timeout=15).text
                    cache_data("source", json.loads(result))
            except Exception as e:
                print(f"source result info: {e}, try to use cache")
                try:
                    result = cache_data("source")
                except Exception as e:
                    print(f"cache source error: {e}")
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
                    result = soft_cfg.article_api
                else:
                    result = requests.get(soft_cfg.article_api_url, timeout=3).text
                    cache_data("article", json.loads(result))
            except Exception as e:
                print(f"article result info: {e}, try to use cache")
                try:
                    result = cache_data("article")
                except Exception as e:
                    print(f"cache article error: {e}")
                    result = soft_cfg.article_api
            result = json.loads(result)
            self.thread_signal.emit(result)
            time.sleep(soft_cfg.article_thread)


class Update_Thread(QThread):
    display_signal = pyqtSignal(dict)

    def __init__(self, auto):
        super().__init__()
        self.auto = auto

    def run(self):
        try:
            result = json.loads(requests.get(soft_cfg.update_url, timeout=3).text)
        except:
            result = {"Version": soft_cfg.version}
        if self.auto:
            result["auto"] = True
        else:
            result["auto"] = False
        self.display_signal.emit(result)


class Downloader_Thread(QThread):
    display_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def run(self):
        if os.path.exists('Download'):
            pass
        else:
            os.mkdir('Download')
        if not os.path.exists('aria2.session'):
            open('aria2.session', 'w')
        subprocess.Popen("aria2c.exe --conf-path=aria2.conf")

    def stop(self):
        subprocess.Popen("taskkill /F /IM aria2c.exe")
