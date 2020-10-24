# 此文件为自动获取github源码信息的Demo代码，未在项目中使用
# Author：Rui Ma

import requests
from bs4 import BeautifulSoup


def get_info():
    url = "https://github.com/MR5356?tab=repositories"
    for i in range(4):
        try:
            req = requests.get(url, timeout=30).text
            break
        except Exception as e:
            print(f"Github api: {e}")
            if i == 3:
                return False

    soup = BeautifulSoup(req, 'html.parser')
    result = {
        'url': [],
        'title': [],
        'info': [],
        'language': [],
    }
    info1, info2 = [], []
    info = soup.findAll("a", {'itemprop': 'name codeRepository'})
    for i in info:
        title = i.text.strip()  # 抓取src
        url = f"https://github.com/{i.get('href')}"
        result['title'].append(title)
        result['url'].append(url)
    info = soup.findAll("p", {'class': 'col-9 d-inline-block text-gray mb-2 pr-4'})
    for i in info:
        desc = i.text.strip()  # 抓取src
        info1.append(desc)
    info = soup.findAll("span", {'itemprop': 'programmingLanguage'})
    for i in info:
        desc = i.text.strip()  # 抓取src
        result['language'].append(desc)
    info = soup.findAll("relative-time")
    for i in info:
        desc = i.text.strip()  # 抓取src
        info2.append(desc)
    for i in zip(info1, info2):
        result['info'].append(f"最后更新于 <span style='color:green'>{i[1]}</span> {i[0]}")
    return result


if __name__ == '__main__':
    result = get_info()
    print(result)
