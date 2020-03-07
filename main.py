# -*- coding:utf-8 -*-
'''
显然创建这个程序主要是为收藏博客的好文章
联系我：woyufan@163.com
'''
from bs4 import BeautifulSoup
import requests
import os
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')


def cnblogs_content(cnblog_url):
    '''
    cnblog_url为文章地址
    输入博客地址，返回博客内容 
    '''
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/78.0.3904.108 Safari/537.36 "
    accept_language = "zh-CN,zh;q=0.9,en;q=0.8"
    authority = "www.cnblogs.com"
    headers = {"user_agent": user_agent, "accept-language": accept_language, "authority": authority}
    # print("requests...")
    response = requests.get(cnblog_url, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")
    # 内容
    cnblogs_post_body = soup.find("div", id="cnblogs_post_body")
    cnblogs_post_body_text = cnblogs_post_body.get_text()
    # 标题
    cb_post_title_url = soup.find("a", id="cb_post_title_url").get_text()
    cnblogs_data = {"title":str(cb_post_title_url), "body":str(cnblogs_post_body), "body_text":str(cnblogs_post_body_text), "html":response.text}
    '''
    # 关于unicode这里有两个
    第一个是bs4会把内容统一使用unicode编码
    另一个是python3 会把封装的dict也统一使用unicode编码。
    如果需要字符串的方法显示，那么只需要把字典中特定的key返回即可
    '''
    return cnblogs_data

def save_to_file(filename, txt):
    '''
    两个参数filenae和要保存的内容txt
    无返回值
    '''
    #print(type(txt))
    # print("saving...")
    fo = open(filename, "w")
    fo.write(txt)
    fo.close()

if __name__ == "__main__":
    cnblogs_data = cnblogs_content("https://www.cnblogs.com/extjs4/p/12381467.html")
    save_to_file("articles/" + cnblogs_data["title"] + ".html", cnblogs_data["body"])
    print("done.")
    #print(json.dumps(cnblogs_data, ensure_ascii=False))






