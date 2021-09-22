# -*- coding: utf-8 -*-

# 一个工作薄中的一个表按指定列拆分数据并保存到多个工作薄中(指定工作薄)

import pandas as pd  #调用pandas包
import xlsxwriter  #调用xlswriter包，用来生成表

dir = "/Users/jason/Downloads/"
data = pd.read_excel("/Users/jason/Downloads/需求一，存量活期结算户/活期结算存量账户.xlsx",usecols=[1,5,13,14,20,23,24,24,28,29,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,60,61,62,63,64,68,69]) #读取存储路径在桌面的工作簿chaifengzb,编码格式为gbk
data.insert(len(list(data)),"公共户管户人",'',True) # 新增空列
data = data.fillna("") # 填补空值
list_data = list(data)

area_list=list(set(data[list_data[1]])) #按机构字段分成列表,集合去重

# writer=pd.ExcelWriter("/EXCEL/测试数据/demo3.xlsx") #生成一个新 工作簿

# data.to_excel(writer,sheet_name="总表",index=False) # 将总表存到新工作簿中

for j in area_list:
    df=data[data[list_data[1]]==j]
    print(str(j)+'机构'+str(len(df))+'条数据!')
    df.to_excel(dir + str(j)+'.xlsx',sheet_name=str(j),index=False) #按分成的列表中的分公司字段进行命名
# writer.save()  #文件保存
print('拆分完成!,共计'+str(len(area_list))+'个文件!!')

