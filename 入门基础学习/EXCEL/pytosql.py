from sqlalchemy import create_engine
import pymysql.cursors
import pandas as pd
file_name = '/Volumes/[C] Windows 11分行生产/Users/jason/Desktop/模型导航.xlsx'
    #'/Users/jason/Downloads/模型导航.xlsx'
"""
config = {'host': '127.0.0.1',
          'port': 3306,
          'user': 'root',
          'password': '12345678',
          'database': 'contest',
          'charset': 'utf8mb4'
          # 'cursorclass':'pymysql.cursors.cursor',
          # 'read_default_file':'my.cnf'
          }
engine = pymysql.connect(**config)
"""
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/contest')
data = pd.read_excel(file_name, sheet_name=0)
engine.execute("truncate table Navigation_Model")
data.to_sql('Navigation_Model', engine, index=False,if_exists="append")
engine.dispose()
print('存入成功！')
