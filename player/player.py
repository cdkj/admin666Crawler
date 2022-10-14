import requests

class Player:


    baseUrl = 'http://666.ruc.edu.cn'
    loginUrl = '/check.asp'
    examPageUrl = '/exam.asp'
    username = 'abc016'
    password = '123456'
    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control": "max-age=0", "Connection": "keep-alive", "Content-Length": "53", "Content-Type": "application/x-www-form-urlencoded", "Host": "666.ruc.edu.cn", 
    "Origin": "http://666.ruc.edu.cn", "Referer": "http://666.ruc.edu.cn/index.asp", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    
    session = None

    def __init__(self, cookie):
        # self.header["Cookie"] = cookie
        self.session = requests.Session()
        return

    def login(self):
        formData = {"username": self.username, "password": self.password, "image3.x": 0, "image3.y": 0}
        r = self.session.post(self.baseUrl + self.loginUrl, headers=self.header, data=formData)
        r.encoding = 'gbk'
        if '对不起' in r.text:
            print(Exception("Error when login. Message: " + r.text))
            exit(0)

    def attack(self):
        # this is a failure now
        r = self.session.get(self.baseUrl + self.examPageUrl)
        r.encoding = "gbk"
        print(r.text)
        r = self.session.get(self.baseUrl + "/main.asp")
        r.encoding = "gbk"
        print(r.text)