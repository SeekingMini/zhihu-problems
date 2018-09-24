<<<<<<< HEAD
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:SeekingMini

"""
采用多线程爬虫，爬取1000个问题的相关信息（关注人数、回答个数等）
"""

# 账号：ppxzs988882@163.com
# 密码：guohui0909
# PS:如果不使用代理IP而短时间爬取大量数据，账号会被封而不是IP,所以这个账号是用2元买的测试账号

import csv
import numpy as np
import pandas as pd
from threading import Thread
from zhihu_oauth import ZhihuClient
from zhihu_oauth import NeedCaptchaException
from zhihu_oauth import GetDataErrorException

TOKEN_FILE = './token/token.pkl'
DF = pd.read_csv(r'../original data/info.csv')  # 读取csv文件
ID_LIST = [DF['ID'][n] for n in np.arange(1000)]  # 把每个问题的ID存入列表


class ProblemPopularity(Thread):
    def __init__(self, q_id, client):
        Thread.__init__(self)

        self.client = client
        self.q_id = q_id
        self.result = []

        self.run()

    def get(self):
        try:
            question = self.client.question(self.q_id)
            print("-----{0}-----".format(question.title))
            print("ID：{0} | 关注人数：{1} | 回答个数：{2}".format(self.q_id, question.follower_count, question.answer_count))
            """example
            -----有哪些人性的黑暗面，尤其是男女关系的黑暗面？-----
            ID：37055410 | 关注人数：123,024 | 回答个数：5865
            """
            self.result = [self.q_id, question.title, question.follower_count, question.answer_count]
        except GetDataErrorException:
            print("★★问题不存在！")
            pass

    def run(self):
        self.get()


def login():
    client = ZhihuClient()
    try:
        client.load_token(TOKEN_FILE)
    except FileNotFoundError:
        try:
            client.login('ppxzs988882@163.com', 'guohui0909')
        except NeedCaptchaException:
            # 保存验证码并提示输入，重新登录
            with open('./captcha/a.gif', 'wb') as f:
                f.write(client.get_captcha())
            captcha = input('please input captcha:')
            client.login('ppxzs988882@163.com', 'guohui0909', captcha)
            client.save_token('./token/token.pkl')
    finally:
        return client


if __name__ == "__main__":
    CLIENT = login()
    with open(r'./res/result.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'NAME', 'FOLLOWER_COUNT', 'ANSWER_COUNT'])
        for q_id in ID_LIST:
            result = ProblemPopularity(int(q_id), CLIENT).result
            writer.writerow(result)
=======
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:SeekingMini

"""
采用多线程爬虫，爬取1000个问题的相关信息（关注人数、回答个数等）
"""

# 账号：ppxzs988882@163.com
# 密码：guohui0909
# PS:如果不使用代理IP而短时间爬取大量数据，账号会被封而不是IP,所以这个账号是用2元买的测试账号

import csv
import numpy as np
import pandas as pd
from threading import Thread
from zhihu_oauth import ZhihuClient
from zhihu_oauth import NeedCaptchaException
from zhihu_oauth import GetDataErrorException

TOKEN_FILE = './token/token.pkl'
DF = pd.read_csv(r'../original data/info.csv')  # 读取csv文件
ID_LIST = [DF['ID'][n] for n in np.arange(1000)]  # 把每个问题的ID存入列表


class ProblemPopularity(Thread):
    def __init__(self, q_id, client):
        Thread.__init__(self)

        self.client = client
        self.q_id = q_id
        self.result = []

        self.run()

    def get(self):
        try:
            question = self.client.question(self.q_id)
            print("-----{0}-----".format(question.title))
            print("ID：{0} | 关注人数：{1} | 回答个数：{2}".format(self.q_id, question.follower_count, question.answer_count))
            """example
            -----有哪些人性的黑暗面，尤其是男女关系的黑暗面？-----
            ID：37055410 | 关注人数：123,024 | 回答个数：5865
            """
            self.result = [self.q_id, question.title, question.follower_count, question.answer_count]
        except GetDataErrorException:
            print("★★问题不存在！")
            pass

    def run(self):
        self.get()


def login():
    client = ZhihuClient()
    try:
        client.load_token(TOKEN_FILE)
    except FileNotFoundError:
        try:
            client.login('ppxzs988882@163.com', 'guohui0909')
        except NeedCaptchaException:
            # 保存验证码并提示输入，重新登录
            with open('./captcha/a.gif', 'wb') as f:
                f.write(client.get_captcha())
            captcha = input('please input captcha:')
            client.login('ppxzs988882@163.com', 'guohui0909', captcha)
            client.save_token('./token/token.pkl')
    finally:
        return client


if __name__ == "__main__":
    CLIENT = login()
    with open(r'./res/result.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'NAME', 'FOLLOWER_COUNT', 'ANSWER_COUNT'])
        for q_id in ID_LIST:
            result = ProblemPopularity(int(q_id), CLIENT).result
            writer.writerow(result)
>>>>>>> origin/master
