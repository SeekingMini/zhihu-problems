# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:SeekingMini

"""
数据来源：知乎关注人数最高的1000个问题(https://zhuanlan.zhihu.com/p/21103740)
将此专栏中的提到的关注人数最高的1000个问题提取出来，用于之后的数据分析
"""

import re
import csv
import time
import requests

URL = 'https://zhuanlan.zhihu.com/p/21103740'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

PATTERN_Q_ORI_INFO = re.compile('(?<=<ol>).+(?=</ol>)')
PATTERN_Q_URL = re.compile('(?<=a href=").+?(?=" class="internal")')
PATTERN_Q_NAME = re.compile('(?<=class="internal">).+?(?=</a>)')
PATTERN_Q_ID = re.compile('(?<=https://www.zhihu.com/question/).+')


def save_data():
    """
    保存网页源代码到文件中
    """
    with open(r".\original data\ori_info.txt", "w", encoding='utf-8') as file:
        file.write(requests.get(URL, headers=HEADERS).text)


def get_info():
    """
    对保存的网页源代码进行处理，返回一个列表
    """
    with open(r".\original data\ori_info.txt", 'r', encoding='utf-8') as f:
        ori_data = f.read()

    question_list = []  # 用于储存每一个问题的相关信息
    question_ori_info = re.findall(PATTERN_Q_ORI_INFO, ori_data)[0]

    question_url_list = re.findall(PATTERN_Q_URL, question_ori_info)  # 提取出问题的URL
    question_name_list = re.findall(PATTERN_Q_NAME, question_ori_info)  # 提取出问题的名称与种类

    for n in range(1000):
        q_id = re.findall(PATTERN_Q_ID, question_url_list[n])[0]
        q_name, q_type = question_name_list[n].split(' - ')[0], question_name_list[n].split(' - ')[1]  # 分离问题的名称与种类
        question_list.append([q_id, q_name.strip(), q_type.strip()])
    return question_list


def save_info(question_list):
    with open("./original data/info.csv", 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'Name', 'Type'])
        for each in question_list:
            writer.writerow(each)


if __name__ == "__main__":
    save_data()
    time.sleep(2)
    q_list = get_info()
    save_info(q_list)
