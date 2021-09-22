#!-*- coding:utf-8 -*-
import urllib.request
import bs4
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context # 取消证书验证

#获取页面初始数据

def getHtmlcode(url):

    # 请求头，虽然这个网站不需要，但是这算是反反爬虫的一种最基本手段
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"

    headers = {"User-Agent": user_agent}

    response = urllib.request.Request(url,headers=headers) # 发起请求
    response.encoding = 'iso-8859-1'
    result = urllib.request.urlopen(response) # 打开页面

    html = result.read()#读取页面
    return html #返回页面信息

#分析页面




def paarser(url):
    html=getHtmlcode(url) # 调用getHtmlcode函数
    soup=BeautifulSoup(html,'html.parser') # 用美味汤分析，得到bs文件
    return soup

#获取每章节目录链接

def Charpter_url(url):
    soup=paarser(url) # 调用parser分析页面
    datas=soup.find('div',id="list").find_all('a') # 获得需要的数据
    url_list=[] # 新建列表用来储存url地址
   # print(datas)
    for data in datas:
        page_url = 'http://www.xbiquge.la'+data['href'] # 拼接成真实地址
        page_name = data.text # 每一章的小说名字
        url_list.append(page_url)
       # print(url_list)

    return url_list

#获取文章单章正文

def get_Charpter_text(url):
    soup=paarser(url)#调用parser分析页面

    content = soup.find('div',id="content").text # 获得需要的正文

    content1 = content.strip().replace("<br />", "") # 顺手处理下格式问题

    return content

#保存文件

def save_text(url):

    url_list=Charpter_url(url)

    num=1

    with open('九星毒奶.text','a',encoding='utf-8') as f:
        for page_url in url_list:
            contents=get_Charpter_text(page_url)
            f.write(contents)
            print('第{}章下载完成'.format(num))
            num+=1
            f.close()

if __name__=='__main__':
    url='http://www.xbiquge.la/26/26136/'
    save_text(url)
