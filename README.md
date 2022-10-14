### admin666Crawler使用

考试有选择题，简答题，综合题，操作题，目前只有自动下载综合题附件的功能，该功能解决了

- 系统对学生上传附件重命名难以识别
- 一个一个附件点击下载太麻烦，也难以管理

#### 使用配置

- main.py, line 5

  ```python
  crawler = Admin666RUCCrawler(cookie, "Your exam name")
  # e.g.
  crawler = Admin666RUCCrawler(cookie, "问卷星数据收集作业（周二班）")
  ```

  

- admin666Crawler.py, line 9, 10, 11

  ```python
  username = 'Your username'
  password = 'Your password'
  courseName = 'Your courseName'
  # e.g.
  username = 'abc123'
  password = '123456'
  courseName = '数据与信息技术基础'
  ```



#### 运行

```shell
python main.py
```



#### 结果储存

所有附件转存在当前目录下的 ./appendix/ 中，命名格式为 学号.zip/rar



#### TODO:

- 自动判分（不推荐开发）
- 下载其他类型题目的附件，不清楚简答题、操作题存不存在有附件的情况
- 每场考试存在多个综合题时如何下载？考虑新的命名方式
- 综合题附件可以为空，可以上传时如何下载？

- logger class
- 文件中有中文可能出现的编码问题

