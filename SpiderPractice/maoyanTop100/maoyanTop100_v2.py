# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 12:15
# @Software: PyCharm
# @File    : maoyanTop100_v2.py
# @Author  : DezeZhao
import json
import re
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool


def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)"'
                         + '.*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'name': item[2],
            'stars': item[3].strip()[3:],
            'releasetime': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def save2file(content):
    with open('top100_v2.json', 'a', encoding='utf-8') as f:
        data = json.dumps(content, ensure_ascii=False)
        f.write(data + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://maoyan.com/board/4'
    }
    html = get_one_page(url, headers)
    # print(html)
    # parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        save2file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i * 10)
# 多进程抓取
# pool = Pool()
# pool.map(main, [i * 10 for i in range(10)])
