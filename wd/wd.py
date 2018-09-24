# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:SeekingMini

"""
对1000个问题的类别进行汇总分析，生成云图
"""

import jieba
import wordcloud
import pandas as pd
import matplotlib.pyplot as plt
from scipy.misc import imread


def generate_wd():
    with open(r'..\original data\info.csv', 'r', encoding='utf-8') as file:
        df = pd.read_csv(file)
    type_text = ""
    for t in df['Type']:
        type_text += t
        type_text += "|"

    text = " ".join(jieba.cut(type_text))
    back_coloring_path = "./bg/circle.jpg"
    back_coloring = imread(back_coloring_path)

    wd = wordcloud.WordCloud(font_path='./font/hksn.ttf', background_color='white', mask=back_coloring,
                             width=1000, height=1000).generate(text)

    plt.imshow(wd, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    wd.to_file('./res/type.jpg')


if __name__ == "__main__":
    generate_wd()
