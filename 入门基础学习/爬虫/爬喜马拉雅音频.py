from bs4 import BeautifulSoup
from urllib.request import urlopen
import pickle
import re
import random
import requests
from queue import Queue
import ssl
import concurrent.futures
import time

# ssl._create_default_https_context = ssl._create_unverified_context  #取消ssl认证s

#定义下载程序

def urllib_download(url, filename):

    from urllib.request import urlretrieve #这个是下载文件的库

    import os #这个是用于创建文件目录

    if os.path.exists(filename) == False: #如果文件不存在，创建文件

        urlretrieve(url, filename)

    else:

        pass

#定义爬虫

def download(page,headers):

    session = requests.session()

    r = session.get(page, headers=headers)

    get_audio = 'https://www.ximalaya.com/revision/play/album?albumId=209378&pageNum='+p+'&sort=0&pageSize=30'

        audiodic = requests.get(get_audio, headers=headers) #获取这个字典

        for i in range(0,30):

        try:

            src = audiodic.json()['data']['tracksForAudioPlay'][i]['src'] #获取音频地址

audio_name= audiodic.json()['data']['tracksForAudioPlay'][i]['trackName'] #获取音频名称
        except:
            print('不能解析')
        else:
            print(src)

        filename = './' + audio_name+'.m4a' #别忘记加上文件后缀名

        urllib_download(src, filename) #调用下载函数下载音频并命名

#分析页面

#

# #定义多线程方法

# def multithreading(pages,headers):

#

#    import threading

#    import time

#    threads = []

#    thread_star_time = time.time()

#    for page in pages:

#        t = threading.Thread(target=spider1,args=(page,))#注意这里参数后面要有个逗号，不然报错

#        threads.append(t)

#    print(threads)

#    for thread in threads:

#        thread.start()

#        print('线程',thread,'启动')

#        thread.join()

#    threadtime = '全部下载完成，多线程使用' + str(time.time() - thread_star_time) + '秒'

#    q.put(threadtime)

#定义 多进程方法

def multiprocessing(pages,headers):

    import multiprocessing as mp

    import time

    processes = []

    process_star_time = time.time()

    for page in pages:

        t = mp.Process(target=download,args=(page,headers,))#注意这里参数后面要有个逗号，不然报错

        processes.append(t)

    print(processes)

    for process in processes:

        process.start()

        print( '进程',process,'启动')

        process.join()

    processtime = '全部下载完成，多进程使用' + str(time.time() - process_star_time) + '秒'

    q.put(processtime)

#

if __name__ == "__main__":

    # 解析页面列表

    q=Queue()

    for p in range(1,4):

    page = 'https://www.ximalaya.com/qinggan/209378/p'+p

    headers = {

        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',

        'host': 'www.ximalaya.com',

        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8', 'Accept-Encoding': 'gzip, deflate, br',

        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

        'Upgrade-Insecure-Requests': '1',

        'Connection': 'keep-alive',

        'Cache-Control': 'max-age=0'}

    global pages

    pages = []

    pages.append(page1)

    pages.append(page2)

    pages.append(page3)

    print(pages)

    # multithreading(pages)

    multiprocessing(pages,headers)

    # for i in range(1, 3):

    print(q.get())

    print('程序结束')

#全部下载完成，多进程使用1408.531194448471秒

# 程序结束

