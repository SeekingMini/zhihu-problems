# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:SeekingMini

"""
对1000个问题进行筛选，选取回答超过1000个的问题
"""

# 账号1：ppxzs988882@163.com | 密码1：guohui0909
# 账号2：rengshizhi3@163.com | 密码2：taiping83
# 账号3：oftdtf000400@163.com | 密码3：longfan18
# 账号4：meiyandou48@163.com | 密码4：gu19961996
# 账号5：rbnzov04832@163.com | 密码5：feiche1121
# 账号6：woquecang5277@163.com | 密码6：hong0906
# 账号7：zhaobimi7242@163.com | leyou1985
# 账号8：ywkc91945533@163.com | 密码8：dong2018
# PS:如果不使用代理IP而短时间爬取大量数据，账号会被封而不是IP被封。所以要多准备几个备用账号！
# PS:如果一个账号被封了，记得先删除原来保存的TOKEN文件再换一个新账号！

import csv
import time
import pandas as pd
from threading import Thread
from zhihu_oauth import ZhihuClient
from zhihu_oauth import NeedCaptchaException
from zhihu_oauth import GetDataErrorException

ACCOUNT = 'woquecang5277@163.com'
PASSWORD = 'hong0906'

TOKEN_FILE = './token/token.pkl'
DF = pd.read_csv(r'res/follower_top_100.csv')  # 读取csv文件


def login(account, password):
    client = ZhihuClient()
    try:
        client.load_token(TOKEN_FILE)
    except FileNotFoundError:
        try:
            client.login(account, password)
        except NeedCaptchaException:
            # 保存验证码并提示输入，重新登录
            with open('./captcha/a.gif', 'wb') as f:
                f.write(client.get_captcha())
            captcha = input('please input captcha:')
            client.login(account, password, captcha)
            client.save_token('./token/token.pkl')
    finally:
        return client


class Quans(Thread):
    def __init__(self, q_id, client):
        Thread.__init__(self)

        self.q_id = q_id  # 传入问题的ID
        self.client = client
        self.result = []

    def get_info(self):
        with open(r'./res/list/{0}.csv'.format(self.q_id), 'w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['作者', '赞同数', '感谢数', '评论数'])
            try:
                question = self.client.question(self.q_id)
                '''print("-----{0}-----".format(question.title))'''
                for answer in question.answers:
                    '''print("作者：{0} | 赞同数：{1} | 感谢数：{2} | 评论数：{3}".
                          format(answer.author.name, answer.voteup_count, answer.thanks_count,
                                 answer.comment_count))'''
                    writer.writerow([answer.author.name, answer.voteup_count, answer.thanks_count,
                                     answer.comment_count])
                print("★★ID：{}爬取结束！".format(self.q_id))
            except GetDataErrorException:
                print("★★问题不存在！")

    def run(self):
        self.get_info()


if __name__ == "__main__":
    CLIENT = login(ACCOUNT, PASSWORD)
    for q_id in DF['ID']:
        print("ID：{}开始爬取！".format(q_id))
        Quans(q_id, CLIENT).start()
        time.sleep(3)

