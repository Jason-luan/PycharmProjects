# -*- coding: utf-8 -*-

# 将数据按某列拆分到多个工作薄

import pandas as pd  #调用pandas包
import xlsxwriter  #调用xlswriter包，用来生成表

dir = "/Users/jason/Downloads/"
data = pd.read_excel("/Users/jason/Downloads/1_01济南市.xls",dtype = str,keep_default_na=False) #读取存储路径表格,数据类型均为字符型,NAN值为''
data.insert(len(list(data)),"金融机构代码",'',True) # 新增空列
#data.iloc[:,[-1]] = data.iloc[:,[11]].apply(lambda x:x[0:6])
#data = data.fillna("") # 填补空值
new_col=[]
for i in range(len(data.iloc[1:,[11]])):
    col=str(list(data.iloc[i+1,[11]])[0])[0:5]
    new_col.append(col)
data["金融机构代码"].iloc[1:]=new_col
list_data = list(data)

area_list=list(set(data[list_data[-1]][1:])) #按机构字段分成列表,集合去重

# writer=pd.ExcelWriter("/EXCEL/测试数据/demo3.xlsx") #生成一个新 工作簿

# data.to_excel(writer,sheet_name="总表",index=False) # 将总表存到新工作簿中

for j in area_list:
    df=data[data[list_data[-1]]==j]
    print(str(j)+'机构'+str(len(df))+'条数据!')
    df.to_excel(dir + str(j)+'.xlsx',sheet_name=str(j),index=False) #按分成的列表中的分公司字段进行命名
# writer.save()  #文件保存
print('拆分完成!,共计'+str(len(area_list))+'个文件!!')

