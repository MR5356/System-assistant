import os

from PyQt5.QtCore import QThread, pyqtSignal
import time
import requests
import json
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


class DownloaderNornal(QThread):
    thread_signal = pyqtSignal(int)

    def __init__(self, choose, url, saveFile, start, end, threadId, chunkSize=10240):
        super().__init__()
        self.choose = choose
        self.saveFile = saveFile
        self.url = url
        self.dstart = start
        self.dend = end
        self.threadId = threadId
        self.chunkSize = chunkSize

    def run(self):
        if self.choose == 1:
            self.run_normal()
        else:
            self.run_special()

    def run_normal(self):
        start = self.dstart
        end = self.dend
        threadId = self.threadId
        chunkSize = self.chunkSize
        for _ in range(30):
            try:
                headers = {'Range': f'bytes={start}-{end}'}
                req = requests.get(self.url, headers=headers, timeout=5, stream=True)
                subSize = 0
                with open(self.saveFile, 'rb+') as fo:
                    fo.seek(start)
                    for chunk in req.iter_content(chunk_size=chunkSize):
                        if chunk:
                            fo.write(chunk)
                            start += chunkSize
                            subSize += chunkSize
                            self.thread_signal.emit(threadId)

                return
            except Exception as e:
                print(f"Download_Thread: {e}")

    def run_special(self):
        start = self.dstart
        end = self.dend
        threadId = self.threadId
        chunkSize = self.chunkSize
        for _ in range(15):
            try:
                req = requests.get(self.url, timeout=30, stream=True)
                subSize = 0
                with open(self.saveFile, 'rb+') as fo:
                    fo.seek(start)
                    for chunk in req.iter_content(chunk_size=chunkSize):
                        if chunk:
                            fo.write(chunk)
                            start += chunkSize
                            subSize += chunkSize
                            self.thread_signal.emit(threadId)

                return
            except Exception as e:
                print(f"Download_Thread: {e}")


class Download_Thread(QThread):
    thread_signal = pyqtSignal(dict)

    def __init__(self, url, threadNum, saveFile):
        super().__init__()
        self.startTime = time.time()
        self.url = url
        self.threadNum = threadNum
        self.saveFile = saveFile
        self.feedback = {
            'info': {
                'size': 0,
                'url': self.url,
                'saveTo': self.saveFile,
                'downloader': 1,
                'started': 0,
                'averageSpeed': 0,
                'thread': self.threadNum
            },
            'main': {
                'data': 0,
                'speed': 0,
            },
            'sub': {
                'data': [[0, 0] for i in range(self.threadNum)],
                'stat': [1 for i in range(self.threadNum)]
            }
        }
        self.threads = {}

        # 302迭代寻址
        req = requests.head(self.url)
        while req.status_code == 302:
            self.url = req.headers['Location']
            self.feedback['info']['url'] = self.url

    def run(self):
        if os.path.exists(self.saveFile):
            self.thread_signal.emit({'fileExists': 1, 'filePath': self.saveFile})
        else:
            try:
                self.runDownloaderNormal()
            except:
                self.downloaderSpecial()

    def downloaderNormal(self, start, end, threadId, chunkSize=10240):
        self.threads[f'thread{threadId}'] = DownloaderNornal(1, self.url, self.saveFile, start, end, threadId)
        self.threads[f'thread{threadId}'].thread_signal.connect(self.resizeThread)
        self.threads[f'thread{threadId}'].start()

    def resizeThread(self, threadId):
        chunkSize = 10240
        if threadId == 99:
            self.feedback['main']['data'] += chunkSize
        else:
            self.feedback['main']['data'] += chunkSize
            self.feedback['sub']['data'][threadId][0] += chunkSize
            self.feedback['sub']['stat'][threadId] = 1

    def runDownloaderNormal(self):
        req = requests.head(self.url)
        self.feedback['info']['size'] = int(req.headers['Content-Length'])
        self.thread_signal.emit(self.feedback)
        # 初始化下载文件, 创建一个与文件大小相同的空间
        fo = open(self.saveFile, 'wb')
        fo.truncate(self.feedback['info']['size'])
        fo.close()
        self.feedback['info']['started'] = 1
        splitPart = self.feedback['info']['size'] // self.threadNum
        for i in range(self.threadNum):
            self.feedback['sub']['data'][i][1] = splitPart

        for i in range(self.threadNum):
            start = splitPart * i
            end = self.feedback['info']['size'] if i == self.threadNum - 1 else start + splitPart - 1
            self.downloaderNormal(start, end, i)
        self.sendSignal()

    def downloaderSpecial(self, chunkSize=10240):
        self.feedback['info']['downloader'] = 0
        self.feedback['info']['started'] = 1
        self.feedback['info']['size'] = 99999
        self.threads[f'thread99'] = DownloaderNornal(0, self.url, self.saveFile, 0, 0, 99)
        self.threads[f'thread99'].thread_signal.connect(self.resizeThread)
        self.threads[f'thread99'].start()
        self.sendSignal()

    def sendSignal(self):
        while True:
            savedData = self.feedback['main']['data']
            time.sleep(.5)
            speed = (self.feedback['main']['data'] - savedData) * 2
            self.feedback['main']['speed'] = speed
            self.thread_signal.emit(self.feedback)
            if self.feedback['main']['data'] >= self.feedback['info']['size']:
                self.feedback['main']['data'] = self.feedback['info']['size']
                endTime = time.time()
                speed = self.feedback['info']['size'] / (endTime - self.startTime)
                self.feedback['info']['averageSpeed'] = speed
                self.thread_signal.emit(self.feedback)
                break
