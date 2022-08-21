# 多个工作薄中的表合到一个新表中(每个工作薄只有一个表)(指定路径)

import os
#from sqlite3 import Cursor
#from token import ENCODING
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine 
#dir = "/Users/jason/Documents/测试"  # 设置工作路径(待并表格在同一路径下)
dir = '/Volumes/[C] Windows 11分行生产/Users/jason/Desktop/VBA测试'
# 新建列表，存放文件名
filename_excel = []

# 新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
#frames = []

#连接数据库
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/contest')
for root, dirs, files in os.walk(dir):
    for file in files:
        if os.path.splitext(file)[1] in ['.xls','.xlsx']: #.xlx结尾的EXCEL文件,可改
            file_path = os.path.join(root,file)
            data = pd.read_excel(file_path, sheet_name=0,header=3,engine="openpyxl")
            sql = "truncate table Navigation_Model"
            #result = cursor.fetchall()
            engine.execute(sql)
            data.to_sql('test1', engine, index=False,if_exists="append")
            #print(file_path +'已导入'+str(result)+'条')
            print(file+"已完成！")
            os.remove(file_path)
            print(file+"文件已删除")
engine.dispose()