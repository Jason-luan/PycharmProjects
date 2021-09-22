

#"2018年销售量"工作表创建一个表头,向其中插入多条数据

import xlsxwriter
# 创建一个名为【demo.xlsx】工作簿
workbook = xlsxwriter.Workbook("测试数据/demo2.xlsx")
# 创建一个名为【2018年销售量】工作表；
worksheet = workbook.add_worksheet("测试")
# worksheet1 = workbook.add_worksheet("2019年销售量")
# 使用write_row方法，为【2018年销售量】工作表，添加一个表头；
# headings = ['产品','销量',"单价"]
headings = ['机构','机构名称']
worksheet.write_row('A1',headings)
# worksheet1.write_row('A1',headings)
# 使用write方法，在【2018年销售量】工作表中插入一条数据；
# write语法格式：worksheet.write(行,列,数据) 
data = [["1601","济南分行营业部"],["1602","济南槐荫支行"],["1603","济南明湖支行"]]
# data1 = [["火龙果",700,6.9],["甘蔗",1000,3.1],["西瓜",2000,2]]
for i in range(len(headings)):
    for j in range(len(data)):
        worksheet.write(j+1,i,data[j][i])
        # worksheet1.write(j+1,i,data1[j][i])
workbook.close()


