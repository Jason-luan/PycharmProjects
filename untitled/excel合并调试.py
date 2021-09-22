
import os
import pandas as pd
import numpy as np

dir = "/Users/jason/Documents/人行反洗钱回头看检查迎检自查数据36_03"#设置工作路径

#新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []

#新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

for root, dirs, files in os.walk(dir):
    for file in files:
        #print(os.path.join(root,file))
        filename_excel.append(os.path.join(root,file))
        df = pd.read_excel(os.path.join(root,file)) #excel转换成DataFrame
        frames.append(df)
#打印文件名
print(filename_excel)   
 #合并所有数据
result = pd.concat(frames)    

#查看合并后的数据
result.head()
result.shape
result.to_excel(dir+'/合并版.xlsx',index = False)#保存合并的数据到电脑D盘的merge文件夹中，并把合并后的文件命名为a12.csv



