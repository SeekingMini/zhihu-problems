Zhihu-Problems
-----
数据来源：[知乎关注人数最高的1000个问题](https://zhuanlan.zhihu.com/p/21103740)<br>
感谢[陈鹏举](https://www.zhihu.com/people/chen-peng-ju/activities)的数据！<br>
* 特别说明：该数据集是2016年的数据，2018年可能已经发生较大变化，但是仍不失为一个好的数据分析的素材！
### 目录
* [开发环境](#开发环境)
* [分析过程](#分析过程)
#### 开发环境
* Window10操作系统
* Anaconda3
* 第三方库
  * [zhihu-oauth](https://github.com/7sDream/zhihu-oauth)(知乎API)
  * [jieba](https://github.com/fxsjy/jieba)(中文分词)
  * [wordcloud](https://github.com/amueller/word_cloud)(生成词云)
#### 分析过程
* 保存[知乎关注人数最高的1000个问题](https://zhuanlan.zhihu.com/p/21103740)的网页源码<br>
* 用正则表达式分别提取1000个问题的`ID` `Name` `Type`(参考文件[info](/original%20data/info.csv))，为进一步分析做准备(具体代码以及文件参考[original data](/original%20data))<br>
* 对1000个问题的Type(问题类别)进行汇总统计(具体代码以及文件参考[wd](wd))
* 从1000个问题中筛选出100个具有代表性的，对每一个问题的回答的赞同数进行分析(具体代码以及文件参考[res](/problems%20analysis/res))
