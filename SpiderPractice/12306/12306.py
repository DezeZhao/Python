# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 12:12
# @Software: PyCharm
# @File    : 12306.py
# @Author  : DezeZhao

import requests

import requests
from urllib.parse import urlencode

data = {
    "leftTicketDTO.train_date": "2020-02-17",
    "leftTicketDTO.from_station": "SHH",
    "leftTicketDTO.to_station": "XMS",
    "purpose_codes": "ADULT"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'cookie': 'JSESSIONID=FE94E50760F1AFEAB18FEA77A0CD19CF; '
              '_jc_save_fromStation=%u4E0A%u6D77%2CSHH; '
              '_jc_save_toStation=%u53A6%u95E8%2CXMS; '
              '_jc_save_wfdc_flag=dc; '
              'BIGipServerotn=1373176074.64545.0000; '
              'RAIL_EXPIRATION=1581140160574; '
              'RAIL_DEVICEID=XT_171HPivmNFTGyxG3_wO-7cmQy8vve46DU1GiPL6N6whd7hve1UBVLlhfQLHr2NqElMqu-eICn0I'
              'kvoI7uQ26vBug1-XmYQrh9f_T1jajdNdzDAyRAhVFv5swK0bjpSbVGfZukiNH9qYc8fEHf4RoMvzAlyTDZ; '
              'BIGipServerpassport=887619850.50215.0000;'
              ' route=6f50b51faa11b987e576cdb301e545c4; '
              '_jc_save_fromDate=2020-02-15; _jc_save_toDate=2020-02-04',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,'
               'SHH&ts=%E5%8E%A6%E9%97%A8,XMS&date=2020-02-15&flag=N,N,Y'
}
url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?' + urlencode(data)
print(url)
html = requests.get(url, headers=headers)
print(html.text)
