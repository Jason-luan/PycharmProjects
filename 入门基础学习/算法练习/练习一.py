import numpy as np
import seaborn as sns
import pandas as pd
# 下载的数据集存放的路径：
income = pd.read_excel(r'/Users/jason/Downloads/income.xlsx')

# 查看数据集是否存在缺失
income.apply(lambda x:np.sum(x.isnull()))


income.fillna(value = {'occupation':income['occupation'].mode()[0]
                       ,'native-country':income['native-country'].mode()[0]},inplace = True)

income.describe()


