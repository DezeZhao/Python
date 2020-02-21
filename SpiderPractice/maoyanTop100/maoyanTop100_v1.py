# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 12:14
# @Software: PyCharm
# @File    : maoyanTop100_v1.py
# @Author  : DezeZhao
import requests
from lxml import etree
import json


def getOnePage(n):
    # 链接
    url = f'https://maoyan.com/board/4?offset={n * 10}'
    # 告诉服务器，我们是浏览器，字典
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
       }
    # 调用
    r = requests.get(url, headers=header)
    return r.text


def parse(text):
    # print(text)
    html = etree.HTML(text)
    # print(html)
    # names是列表
    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    releasetimes = html.xpath('//p[@class="releasetime"]/text()')
    # zip函数时拉链函数
    item = {}  # dict
    for name, releasetime in zip(names, releasetimes):
        item['name'] = name
        item['releasetime'] = releasetime
        yield item  # 生成器


# 保存数据
def save2File(data):
    with open('top100_v1.json', 'a', encoding='utf-8') as f:
        # 把字典 列表 等转换为字符串  之后才能写入文件
        data = json.dumps(data, ensure_ascii=False) + '\n'
        f.write(data)


if __name__ == '__main__':
    for n in range(0, 10):
        text = getOnePage(n)
        items = parse(text)
        for item in items:
            save2File(item)
