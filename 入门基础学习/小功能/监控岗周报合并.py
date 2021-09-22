# -*- coding:utf-8 -*-

# 自动汇总监控岗周志

import os
import pandas as pd
import numpy as np
import time

dir = "/Volumes/[C] Python/Users/jason/Desktop/履职周报/"+str(time.strftime('%Y%m%d'))  # 设置工作路径(待并表格在同一路径下)
# 汇总表
df=pd.read_excel("/Volumes/[C] Python/Users/jason/Desktop/履职周报/区域监控经理管理周志-X月X日.xlsx",sheet_name=0,header=4,keep_default_na=False,usecols=[0,1,2,3,4,5,6,7,8])

# 新建列表，存放文件名
filename_excel = []
for root, dirs, files in os.walk(dir):
    for file in files:
        if os.path.splitext(file)[1] in ['.xls','.xlsx']:  # .xlx结尾的EXCEL文件,可改
            file_path = os.path.join(root,file)
            filename_excel.append(file_path)
            df1 = pd.read_excel(file_path,sheet_name=0,header=4,keep_default_na=False)  # excel转换成DataFrame
            for org in df1.columns.values[2:]:
                value = df1.loc[0:16,[org]]
                # df1 = df1.fillna("无")  # 填补空值
                if list(value.values[2])[0] != '':
                    df.loc[0:16,[org]] = value
                    df.iloc[2:16,]=df.iloc[2:16,].replace('','无')
#df.iloc[2:16,].replace('',"无")
df.to_excel(dir + '/区域监控经理管理周志-汇总.xlsx',index = False)  # 保存合并的数据到原文件夹,并改名
print("合并表格数量:" + str(len(filename_excel)) + "个")
print("叮咚~完成啦!!")


