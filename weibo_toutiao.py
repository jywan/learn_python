# -*- coding: utf-8 -*-
# Time    : 2018/5/5 4:29 PM
__author__ = 'wjy'

import jieba.posseg as pseg
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
import time
from scipy.misc import imread
import re
import requests


def get_weibo_toutiao():
    # titles = []  # 返回的title列表
    BASE_URL = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?\
    ajwvr=6&category=1760&page={}'
    HEADERS = {
        'Host': 'weibo.com',
        'Referer': 'https://weibo.com/?category=1760',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    patt = re.compile(r'class="S_txt1" target="_blank">(.*?)</a>')
    with open('titles.txt', 'w') as fw:
        for i in range(200):
            r = requests.get(BASE_URL.format(i), headers=HEADERS)
            result = r.json()  # 获取返回来的json格式数据
            data = result['data']
            title = patt.findall(data)
            for t in title:
                fw.write(t + '\n')
            # titles.extend(title)
            # time.sleep(2)


def extract_words():
    with open('titles.txt','r') as fr:
        titles = fr.readlines()

    stop_words = set(line.strip() for line in open('stopwords.txt', 'r'))
    title_list = []  # 头条标题词汇列表
    name_list = []  # 人名头条列表
    for title in titles:
        if title.isspace():
            continue
        word_list = pseg.cut(title)
        for word, flag in word_list:
            if not word in stop_words:
                if flag == 'n':  # 名词
                    title_list.append(word)
                if flag == 'nr':  # 人名
                    name_list.append(word)
    d = os.path.dirname(__file__)
    mask_image1 = imread(os.path.join(d, 'background.png'))
    content1 = ' '.join(title_list)
    mask_image2 = imread(os.path.join(d, 'background.png'))
    content2 = ' '.join(name_list)
    wordcloud1 = WordCloud(font_path='PingFang.ttc', background_color='grey', mask=mask_image1, max_words=100).generate(content1)
    wordcloud2 = WordCloud(font_path='PingFang.ttc', background_color='grey', mask=mask_image2, max_words=100).generate(content2)
    plt.imshow(wordcloud1)
    plt.axis('off')
    wordcloud1.to_file('worldcloud1.jpg')
    plt.show()
    plt.imshow(wordcloud2)
    plt.axis('off')
    wordcloud2.to_file('worldcloud2.jpg')
    plt.show()


if __name__ == '__main__':
    get_weibo_toutiao()
    extract_words()