# !/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pandas as pd
import os.path
import os


def xls2xlsx():
    rootdir = "/Users/jason/Documents/人行反洗钱回头看检查迎检自查数据36_02"
    files = os.listdir(rootdir)
    num = len(files)
    for i in range(num):
        path = rootdir + files[i]
        a = files[i].split('.')
        b = rootdir + a[0] + '.xlsx'
        x = pd.read_excel(path)
        x.to_excel(b, index=False)


xls2xlsx()