# 多个工作薄中的表合到一个新表中(每个工作薄只有一个表)(指定路径)

import os
import pandas as pd
import numpy as np
dir = "/Users/jason/Documents/测试"  # 设置工作路径(待并表格在同一路径下)

# 新建列表，存放文件名
filename_excel = []

# 新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

for root, dirs, files in os.walk(dir):
    for file in files:
        if os.path.splitext(file)[1] in ['.xls','.xlsx']: #.xlx结尾的EXCEL文件,可改
            file_path = os.path.join(root,file)
            filename_excel.append(file_path)
            df = pd.read_excel(file_path)  # excel转换成DataFrame
            frames.append(df)
 #合并所有数据
result = pd.concat(frames)
row_number = len(result)

# 输出表格合并数量
print("合并表格数量:" + str(len(filename_excel)) + "个")
# 输出合并后数据总量
print("数据共有:" + str(row_number)+"条")

result.to_excel(dir + '/嘚不嘚.xlsx',index = False) #保存合并的数据到原文件夹,并改名
print("叮咚~完成啦!!")
