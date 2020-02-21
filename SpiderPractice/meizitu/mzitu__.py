# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 14:47
# @Software: PyCharm
# @File    : mzitu__.py
# @Author  : DezeZhao
import os
import sys
from multiprocessing import Pool
from multiprocessing import freeze_support

import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}


def find_MaxPage():
    all_url = 'http://www.mzitu.com'
    html_index = requests.get(all_url, headers=header)
    # 找寻最大妹子页面数
    soup1 = BeautifulSoup(html_index.text, "lxml")
    page = soup1.find_all('a', class_='page-numbers')
    max_page_num = page[-2].get_text()
    return max_page_num


def Download(href, title, path):
    html = requests.get(href, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    if soup:
        pic_max = soup.find_all('span')
        pic_max = pic_max[9].text  # 最大页数
        if (os.path.exists(path + title.strip().replace('?', ''))
                and len(os.listdir(path + title.strip().replace('?', ''))) >= int(pic_max)):
            print('妹子已待命，继续准备下一个妹子' + title)
            return 1
        print(f"发现妹子资源{pic_max}个，准备中：" + title)
        os.makedirs(path + title.strip().replace('?', ''))
        os.chdir(path + title.strip().replace('?', ''))
        for num in range(1, int(pic_max) + 1):
            pic = href + '/' + str(num)
            html = requests.get(pic, headers=header)
            mess = BeautifulSoup(html.text, "html.parser")
            pic_url = mess.find('img', alt=title)
            if 'src' not in pic_url.attrs:  # 有些pic_url标签没有src属性，导致操作异常，在次进行过滤
                continue
            print(f"{title}：{pic_url['src']}")
            html = requests.get(pic_url['src'], headers=header)
            file_name = pic_url['src'].split(r'/')[-1]
            f = open(file_name, 'wb')
            f.write(html.content)
            f.close()
        print('妹子已就绪，客官请慢用：' + title)


if __name__ == '__main__':
    freeze_support()  # 防止打包后 运行exe创建进程失败

    # 线程池中线程数
    count = 1
    if len(sys.argv) >= 2:
        count = int(sys.argv[1])

    pool = Pool(count)
    print(f'初始化下载线程个数${count}')

    # http请求头
    path = os.getcwd() + '/mzitu_mutil/'
    max_page = find_MaxPage()  # 获取最大页数  即生成的文件夹数量
    print(max_page)
    print(f'捕获{max_page}页妹子，请耐心等待下载完成')
    same_url = 'http://www.mzitu.com'

    for n in range(1, int(max_page) + 1):
        if n == 1:
            each_url = same_url
        else:
            each_url = same_url + "/page/" + str(n) + "/"
        start_html = requests.get(each_url, headers=header)  # 请求一页中的所有妹子
        soup = BeautifulSoup(start_html.text, "lxml")
        if soup:
            all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
            for a in all_a:  # 遍历每一页中的妹子
                title = a.text  # 提取文本
                if title != '':
                    href = a['href']  # 请求妹子的所有图集
                    pool.apply_async(Download, args=(href, title, path))
    pool.close()
    pool.join()
    print('所有妹子已就绪，客官请慢用')
