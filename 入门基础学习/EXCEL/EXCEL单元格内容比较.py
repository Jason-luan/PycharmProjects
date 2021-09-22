# -*- coding:utf-8 -*-

import pandas as pd
import os

workbook = pd.read_excel('/Users/jason/Downloads/总行提取-济南行业与经营范围不一致数据（济南同城）.xlsx',usecols=[7,10])
# sheet_name = list(workbook.keys())
# sheet1 = sheet_name[0]




frame = []
for i in range(len(workbook)):
    workbook=workbook.reset_index(drop=True)
    if workbook.iloc[i,0:1]!=workbook.iloc[i,1:2]:
        df = workbook.iloc[i]
        frame.append(df)
print(frame)