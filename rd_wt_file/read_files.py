# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:53
# @Software: PyCharm
# @File    : read_files.py
# @Author  : DezeZhao

import re

import pandas as pd

data = pd.read_excel("GDP.xlsx")
gdp = []
p_gdp = []

gdp = data['GDP'].values
k = 0
for i in gdp:
    pattern = re.compile(r'.*\((.*?)\)')
    dd = re.findall(pattern, str(i))
    if dd:
        gdp[k] = str(dd[0])
    else:
        gdp[k] = str(dd[0])
    k += 1

p_gdp = data['P-GDP'].values

j = 0
for i in p_gdp:
    pattern = re.compile(r'.*\((.*?)\)')
    dd = re.findall(pattern, str(i))
    if dd:
        p_gdp[j] = str(dd[0])
    else:
        p_gdp[j] = str(p_gdp[j])
    j += 1

k = 0
gdp_ = [0] * 200
for i in gdp:
    if i.find(','):
        g = ''
        l = i.split(',')
        for j in l:
            g += j
        gdp_[k] = int(g)
    else:
        gdp_[k] = int(gdp[k])
    k += 1

k = 0
p_gdp_ = [0] * 200
for i in p_gdp:
    if i.find(','):
        g = ''
        l = i.split(',')
        for j in l:
            g += j
        p_gdp_[k] = int(g)
    else:
        p_gdp_[k] = int(p_gdp[k])
    k += 1

dict1 = {
    'GDP': gdp_,
    'P-GDP': p_gdp_
}
data_ = pd.DataFrame(dict1)
pd.ExcelWriter('GDP.xlsx')
data.to_excel('GDP.xlsx')
