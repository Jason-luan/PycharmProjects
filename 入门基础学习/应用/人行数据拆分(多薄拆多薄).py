# -*- coding: utf-8 -*-

# 将多个工作薄中的多个工作表按某一列拆分成多个单工作薄(超60000条分SHEET表)
import os
import pandas as pd
import numpy as np
dir = "/Users/jason/Documents/人行数据/"  # 设置工作路径(待并表格在同一路径下)

# 新建列表，存放文件名
filename_excel = []

# 新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

for root, dirs, files in os.walk(dir):
    for file in files:
        if os.path.splitext(file)[1] in ['.xls','.xlsx']: #.xlx结尾的EXCEL文件,可改
            file_path = os.path.join(root,file)
            filename_excel.append(file_path)
            df = pd.read_excel(file_path,dtype = str,keep_default_na=False,usecols = [0,2,8,11,15,17,18,20])  # excel转换成DataFrame
            frames.append(df)
data = pd.concat(frames) #合并所有数据
data = data.rename (columns = {"Unnamed: 0":"账号","Unnamed: 2":"户名","Unnamed: 8":"证件号码","Unnamed: 11":"机构行号","Unnamed: 15":"机构名称","Unnamed: 17":"开户日期","Unnamed: 18":"销户日期","Unnamed: 20":"账户状态"})
data = data.drop(0,axis=0).reset_index()#重置Index
data.drop('index',axis=1,inplace=True) #删除原index
row_number = len(data)
print("共计" + str(len(filename_excel)) + "个文件.")
print("共计" + str(row_number) + "条数据.")
data.insert(len(list(data)),"金融机构代码",'',True) # 新增空列
new_col=[]
for i in range(len(data.iloc[:,[3]])):
    col=str(list(data.iloc[i,[3]])[0])[0:5]
    new_col.append(col)
data["金融机构代码"]=new_col
list_data = list(data)

area_list=list(set(data[list_data[-1]])) #按机构字段分成列表,集合去重

# writer=pd.ExcelWriter(dir + file + "拆分后.xlsx") #生成一个新 工作簿

# data.to_excel(writer,sheet_name="原表",index=False) # 将总表存到新工作簿中

for j in area_list:
    df=data[data[list_data[-1]]==j]
    print(str(j)+'机构'+str(len(df))+'条数据!')
    writer = pd.ExcelWriter(dir + str(j) + ".xlsx")
    row_numbers = int(df.shape[0])
    for i in range(0,row_numbers,60000):#超6万条数据分SHEET保存
        k = i + 60000 if i + 60000 < row_numbers else row_numbers
        df[i:k].to_excel(writer,sheet_name=str(int(i/60000)),index=False)
    # df.to_excel(writer, sheet_name=str(j), index=False)
    writer.save()  #文件保存
print('拆分完成!,共计'+str(len(area_list))+'个文件!!')

