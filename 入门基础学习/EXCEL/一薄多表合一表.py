# -*- coding: utf-8 -*-

# 一个工作薄中的多个表合到一个新表中(指定工作薄)

import pandas as pd
import xlrd

file_name = "/EXCEL/测试数据/demo.xlsx"
wb=xlrd.open_workbook(file_name)
sheets = wb.sheet_names()
frames = []
for i in range(len(sheets)):
    df = pd.read_excel(file_name,sheet_name = i,index_col=0)
    frames.append(df)
# frames = frames.reset_index(drop=True)
 #合并所有数据
result = pd.concat(frames)
row_number = len(result)
# 输出表格合并数量
print("合并页签数量:" + str(len(sheets)) + "个")
# 输出合并后数据总量
print("数据共有:" + str(row_number)+"条")


result.to_excel("/Users/jason/PycharmProjects/入门基础学习/EXCEL"+"/demo1.xlsx",sheet_name = "数据合并") #保存合并的数据到指定文件,并改名
print("叮咚~完成啦!!")
