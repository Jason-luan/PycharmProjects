import requests
from lxml import etree
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    'Host': 'www.xbiquge.la',
    'Referer': 'http://www.xbiquge.la/26/26136/',
}

url = "http://www.xbiquge.la/26/26136/"
response = requests.get(url, headers).text
# print(response)

res = etree.HTML(response)
hrefs_list = res.xpath('//dl//dd/a/@href')
# print(hrefs_list)
with open('九星毒奶.txt', 'w+', encoding='utf-8')as f:
    for href in hrefs_list:
        url = "http://www.xbiquge.la"+href
        response = requests.get(url, headers).text.encode('iso-8859-1')
        res = etree.HTML(response)
        title = res.xpath('//div[@class="bookname"]/h1/text()')[0]
        # print(title)
        content = res.xpath('//div[@id="content"]//text()')
        title = ''.join(title)
        content = ''.join(content)
        f.write('\n'+title+'\n')
        f.write('\n'+content+'\n')
        print('正在保存' + title)
        print(url)
        time.sleep(0.3)
print("叮咚~完成啦!!")

