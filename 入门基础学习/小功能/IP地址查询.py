from get_ip_info import get_ip_info
import pandas as pd
import time
dir = "/Users/jason/Downloads/"
data = pd.read_excel("/Users/jason/Downloads/IP地址.xlsx")
ip = list(data[data.columns[0]])
for i in ip:
    ip_info = get_ip_info(i)
    print(ip_info)
    time.sleep(2)

#data.loc[len(data)] = ['223.104.50.180']