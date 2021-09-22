# -*- coding: utf-8 -*-

# 一个工作薄中的一个表按指定列拆分数据并保存到同一个工作薄中的多个工作表中(指定工作薄)

import pandas as pd  #调用pandas包
import xlsxwriter  #调用xlswriter包，用来生成表

dir = "/Users/jason/PycharmProjects/入门基础学习/EXCEL/测试数据/"

data=pd.read_excel("/Users/jason/PycharmProjects/入门基础学习/EXCEL/测试数据/demo2.xlsx") #读取存储路径在桌面的工作簿chaifengzb,编码格式为gbk

list_data = list(data)

area_list=list(set(data[list_data[0]])) #按机构字段分成列表

writer=pd.ExcelWriter(dir + "demo3.xlsx") #生成一个新 工作簿

data.to_excel(writer,sheet_name="总表",index=False) # 将总表存到新工作簿中

for j in area_list:
    df=data[data[list_data[0]]==j]
    print(str(j)+'机构'+str(len(df))+'条数据!')
    df.to_excel(writer,sheet_name=str(j),index=False) #按分成的列表中的分公司字段进行命名
writer.save()  #文件保存
print('拆分完成!,共计'+str(len(area_list))+'个页签!!')

