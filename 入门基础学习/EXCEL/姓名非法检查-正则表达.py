
import pandas as pd
import re
import time
dir = '/Users/jason/Downloads/'
df = pd.read_excel('/Users/jason/Downloads/科技数据9月2日（6个月无交易加暂停非柜面锁）.xlsx',dtype = str,sheet_name=0,usecols = [1,3])
df1 = df[[df.columns.values[1],df.columns.values[0]]] #调整字段顺序
# df1.insert(len(list(df1)),"异常标识",'',True) # 新增空列
df1[df1.columns.values[0]] = df1[df1.columns.values[0]].replace(r'[\x00-\xff]$',"",regex=True)
df_end = df1[df1.columns.values[0]].str.contains(r'^[^A-Z]+[a-zA-Z0-9_\s\.\(\)\|\?(\x00-\xff)(\uf800-\uf8ff)]+')
df_excel = df1[~df_end]

df_excel1 = df1.loc[df1.iloc[:,0].str.contains(r'^[^A-Z]+[a-zA-Z0-9_\s\.\(\)\|\?(\x00-\xff)(\uf800-\uf8ff)]+')]

writer=pd.ExcelWriter(dir + str(time.strftime('%Y%m%d'))+".xlsx") #生成一个新 工作簿
df_excel.to_excel(writer,sheet_name="正常",index=False) # 将总表存到新工作簿中
df_excel1.to_excel(writer,sheet_name="异常",index=False) # 将总表存到新工作簿中

writer.save()  #文件保存
print('保存完成!')