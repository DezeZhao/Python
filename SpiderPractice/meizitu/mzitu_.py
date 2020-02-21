# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 23:00
# @Software: PyCharm
# @File    : mzitu_.py
# @Author  : DezeZhao
import hashlib
import os

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_page_index(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("Request page index error!")
        return None


def parse_page_index(html):
    soup = BeautifulSoup(html, 'lxml')
    uls = soup.find_all('ul', class_='archives')
    for ul in uls:
        group_urls = ul.find_all('a')
        for group_url in group_urls:
            yield {
                'title': group_url.get_text(),
                'url': group_url['href']
            }


def get_page_detail(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("request page detail error!")
        return None


def get_page_url(html, group_url):
    soup = BeautifulSoup(html, 'lxml')
    max_page_index = soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for index in range(1, int(max_page_index) + 1):
        if index == 1:
            page_url = group_url
        else:
            page_url = group_url + '/' + str(index)
        yield page_url


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    # image_url=soup.select('body > div.main > div.content > div.main-image > p > a > img')['src']
    image_url = soup.find('div', class_='main-image').find('img')['src']
    return image_url


def download_image(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        return None
    except RequestException:
        print("download image error!")
        return None


def save2files(content, url, title):
    path = title + '\\' + hashlib.md5(content).hexdigest() + '.jpg'
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)
            print("正在下载图片:" + str(url))
    else:
        print("图片 " + str(url) + " 已存在!")
        pass


def main():
    url = 'https://www.mzitu.com/all/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://www.mzitu.com/all/'
    }
    html = get_page_index(url, headers)
    for group in parse_page_index(html):
        dir_path = os.getcwd() + '//' + group['title']  # 创建以图片组名为文件夹名的文件夹路径
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print('创建了一个名为\"' + group['title'] + '\"的文件夹！')
        else:
            print("名为\"" + group['title'] + "\"文件夹已存在！")
        html1 = get_page_detail(group['url'], headers)
        for page_url in get_page_url(html1, group['url']):
            html2 = get_page_detail(page_url, headers)
            image_url = parse_page_detail(html2)
            content = download_image(image_url, headers)
            save2files(content, image_url, group['title'])


if __name__ == '__main__':
    main()
