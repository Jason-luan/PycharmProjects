# -*- coding:utf-8 -*-

import difflib
text1 = '''
计算机软件及辅助设备、电子产品、办公设备、非专控通讯产品、建材的销售;计算机、信息、教育、数据科技领城内的技术开发、技术转让、技术推广、技术服备、技术咨询;数据处理与存储
''' # 定义字串text1
text1_lines = text1.splitlines() # 以行分隔，以便进行对比
text2 = '''
计算机软件及辅助设备、电子产品、办公设备、非专控通讯产品、建材的销售;计算机、信息、教育、数据科技领域内的技术开发、技术转让、技术推广、技术服务、技术咨询;数据处理与存储
''' # 定义字符串2
text2_lines = text2.splitlines() # 以行分隔，以便进行对比
# d = difflib.Differ() # 创建differ()对象
# diff = d.compare(text1_lines,text2_lines) # 采用compare 方法对字符串进行比较
# print (''.join(list(diff))) #打印输出结果
d = difflib.HtmlDiff()
html = d.make_file(text1_lines,text2_lines)
print(html)
with open('diff.html', mode='w',encoding='utf-8') as f:
    f.write(html)