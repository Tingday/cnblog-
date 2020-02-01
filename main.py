# -*- coding:utf-8 -*-
"""
显然创建这个程序主要是为了偷懒
同时希望能够把收集的博客文章，制作成epub电子书，方便浏览
联系我：woyufan@163.com
"""
from bs4 import BeautifulSoup
import requests
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def cnblog_content(cnblog_url):
    # cnblog_url = "https://www.cnblogs.com/newcaoguo/p/7103249.html"
    # cnblog_url = "https://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741375.html"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/78.0.3904.108 Safari/537.36 "
    accept_language = "zh-CN,zh;q=0.9,en;q=0.8"
    authority = "www.cnblogs.com"
    headers = {"user_agent": user_agent, "accept-language": accept_language, "authority": authority}
    response = requests.get(cnblog_url, headers=headers)
    # print(response.text)
    # print(response.content)
    soup = BeautifulSoup(response.content, features="html.parser")
    # print(unicode(Soup))
    cnblogs_post_body = unicode(soup.find("div", id="cnblogs_post_body"))
    # get title
    cb_post_title_url = unicode(soup.find("a", id="cb_post_title_url").get_text())
    # save to html file
    # print(cb_post_title_url)
    fo = open(cb_post_title_url + ".html", "wb")
    fo.write(cnblogs_post_body)
    fo.close()
    print(cb_post_title_url)


if __name__ == "__main__":
    cnblog_content("https://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741375.html")
