#enconding:uft8
import requests
def get_ip_info(ip):
    r = requests.get('http://ip.taobao.com//outGetIpInfo?ip=%s' %ip)
    if r.json()['code'] == 0:
        i = r.json()['data']
        country = i['country']
        area = i['area']
        region = i['region']
        city = i['city']
        isp = i['isp']
        print(u'国家:%s\n区域:%s\n省份:%s\n城市:%s\n运营商:%s\n'%(country,area,region,city,isp))
    else:
        print("ERROR!ip:%s"%ip)

