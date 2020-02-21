# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 23:38
# @Software: PyCharm
# @File    : jiepai,py
# @Author  : DezeZhao
import json
import os
import re
from hashlib import md5
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from multiprocessing import Pool
from config1 import *


def get_index_page(offset, keyword):
    data = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1580791013872'
    }
    url = url1 + urlencode(data)
    print(url)
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("request index page error!")
        return None


def parse_index_page(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            url = item.get('article_url')
            if url:
                url_pattern = re.compile(r'^http.*?/(\d+)/$', re.S)
                result = re.match(url_pattern, url)
                if result:
                    url = 'https://www.toutiao.com/a' + result.group(1) + '/'
                    yield url


def get_page_detail(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("request page detail error!")
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    if soup.title:
        title = soup.title.string
        images_pattern = re.compile('gallery:.*?JSON.parse\("(.*?)"\),', re.S)
        result = re.search(images_pattern, html)
        if result:  # json格式数据的键key必须是双引号，二dict型数据的key必须是单引号
            str1 = result.group(1).replace('\\\"', '\"')
            str1 = str1.replace('\\\\\\', '\\')
            data = json.loads(str1)
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images = [item.get('url') for item in sub_images]
                return {
                    'title': title,
                    'url': url,
                    'images': images
                }


def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return None
    except RequestException:
        print("download image error!")
        return None


def save_image2file(title, content, url):
    # path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    path = title + '\\' + md5(content).hexdigest() + '.jpg'
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)
            print("正在下载图片:" + str(url))
    else:
        print("该图片已存在！")
        pass


def main(offset):
    keyword = '街拍性感美女'
    html = get_index_page(offset, keyword)
    # print(html)
    for url in parse_index_page(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            if result:
                title = result.get('title')
                print(str(title) + " 开始下载...")
                path = os.getcwd() + '\\' + title
                if not os.path.exists(path):
                    os.mkdir(path)
                pass
                for image_url in result.get('images'):
                    content = download_image(image_url)
                    save_image2file(title, content, image_url)


# print(os.getcwd())#C:\Users\ZhaoDeze\PycharmProjects\pytest1\Spider\JinRiTouTiao
if __name__ == '__main__':
    # for offset in range(5):
    #     main(offset * 20)
    # 多进程
    groups = [20 * x for x in range(10)]
    pool = Pool()
    pool.map(main, groups)
