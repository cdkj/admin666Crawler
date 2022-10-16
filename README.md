### admin666Crawler使用

考试有选择题，简答题，综合题，操作题，目前只有自动下载综合题附件的功能，该功能解决了

- 系统对学生上传附件重命名难以识别
- 一个一个附件点击下载太麻烦，也难以管理



#### 使用配置

- 配置config.txt，项目根目录下创建config.txt并配置如下内容，注意每行的顺序不要调换，不要添加多余的空格

  ```
  username=Your username
  password=Your password
  courseName=Your courseName
  examName=Your examName
  ```

  例如

  ```
  username=zjzj99
  password=Zj##9099
  courseName=信息与基础数据
  examName=（周二班）数据作业收集问卷星
  ```

  - **Notice**: 由于有中文课程名和考试名，读取时注意潜在编码问题，代码中默认config.txt是utf-8编码格式（admin666Crawler line 41）,如果需要请自行修改编码格式


#### 运行

```shell
python main.py
```

- cookie是我本地运行的cookie，目前没有测试过不用cookie仅靠request库的session能否登录，如果直接运行无法登录，请手动登录并拷贝自己浏览器的cookie替换main.py中的cookie，或联系开发人员。




#### 结果储存

所有附件转存在当前目录下的 ./appendix/ 中，命名格式为 学号.zip/rar



#### TODO:

- 自动判分（不推荐开发）
- 下载其他类型题目的附件，不清楚简答题、操作题存不存在有附件的情况
- 每场考试存在多个综合题时如何下载？考虑新的命名方式
- logger class
- 文件中有中文可能出现的编码问题

