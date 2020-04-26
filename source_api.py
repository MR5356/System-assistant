# 此文件为自动获取github源码信息的Demo代码，未在项目中使用
# Author：Rui Ma

import requests
from bs4 import BeautifulSoup


def get_info():
    url = "https://github.com/MR5356"
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
    img_src = soup.findAll("a", {'class': 'text-bold flex-auto min-width-0'})
    for img in img_src:
        img = img.get('href')  # 抓取src
        result['url'].append(f"https://github.com/{img}")
    img_src = soup.findAll("span", {'class': 'repo'})
    for img in img_src:
        img = img.text.strip()  # 抓取src
        result['title'].append(img)
    img_src = soup.findAll("p", {'class': 'pinned-item-desc text-gray text-small d-block mt-2 mb-3'})
    for img in img_src:
        img = img.text.strip()  # 抓取src
        result['info'].append(img)
    img_src = soup.findAll("span", {'itemprop': 'programmingLanguage'})
    for img in img_src:
        img = img.text.strip()  # 抓取src
        result['language'].append(img)
    result['language'] = result['language'][:len(result['title'])]
    return result


if __name__ == '__main__':
    result = get_info()
    print(result)