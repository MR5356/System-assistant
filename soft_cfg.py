import json

# 定义网址
web_site = "https://www.toodo.fun"  # 网站主页
feed_back = "https://www.toodo.fun"  # 反馈网址
help_us = "https://toodo.fun/funs/thanks/"  # 捐赠网址
source_api_url = "http://softapi.toodo.fun/get_source"  # 源码仓库网址
article_api_url = "http://softapi.toodo.fun/get_article"  # 文章教程网址

# 线程配置
time_thread = .5
source_thread = 600  # 不用经常刷新
article_thread = 60

# 测试数据
debug = 0
source_api = json.dumps(
    {'url': ['https://github.com//MR5356/bilibili-up-helper', 'https://github.com//MR5356/MRweidiannao'],
     'title': ['bilibili-up-helper', 'MRweidiannao'], 'info': ['A helper for bilibili uploader', '微电脑安卓APP（已暂停服务）'],
     'language': ['Python', 'Java']})
article_api = json.dumps({'url': [
    'https://toodo.fun/funs/learn/files/article.php?id=58&title=UP%E4%B8%BB%E5%B0%8F%E5%8A%A9%E6%89%8B%20%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E'],
                          'title': ['UP主小助手 使用说明'],
                          'info': ['《UP主小助手 使用说明》是作者 鱼鹰的酒鬼 最后更新于 2020-04-24 的一篇文章，当前阅读量为 1632'],
                          'date': ['2020-04-24']})
