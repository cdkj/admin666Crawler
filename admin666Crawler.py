import requests
from bs4 import BeautifulSoup
import re
import os
import time

class Admin666RUCCrawler:

    # Read from config.txt, see how to config in Readme.md
    username = 'your username'
    password = 'your password'
    courseName = 'your courseName'
    examName = 'your examName'


    savedir = ".\\appendix"
    baseUrl = 'http://admin666.ruc.edu.cn/Manage407108913Admin323'
    downloadBaseUrl = 'http://admin666.ruc.edu.cn'
    loginUrl = '/check.asp' # login interface
    allCourseUrl = '/kaoshi_course.asp' # list all course in system
    allExamUrl = '/kaoshi.asp?courseid='
    examDetailUrl = '/search_score.asp?kaoshiid=' # exam detail interface, requiring examID
    zongAwardUrl = '/award_score_z.asp?kaoshiid=' # 综合题 score interface, requiring examID
    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control": "max-age=0", "Connection": "keep-alive", "Content-Length": "61", 
    "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Host": "admin666.ruc.edu.cn", "Origin": "http://admin666.ruc.edu.cn", "Referer": "http://admin666.ruc.edu.cn/Manage407108913Admin323/index.asp", "Upgrade-Insecure-Requests": "1"}
    errorLog = ".\\errlog.txt"

    examName = None
    session = None
    examID = None
    courseID = None
    appendixPage = None

    def __init__(self, cookie):
        self.session = requests.Session()
        self.header["Cookie"] = cookie
        self.readConfig()

    def readConfig(self):
        with open(".\\config.txt", 'r', encoding='utf-8') as configFile:
            config = configFile.readlines()
            self.username = config[0].strip().split("=")[1]
            self.password = config[1].strip().split("=")[1]
            self.courseName = config[2].strip().split("=")[1]
            self.examName = config[3].strip().split("=")[1]

    def checkDict(self):
        if os.path.exists(self.savedir):
            return
        os.mkdir(self.savedir)

    def login(self, local=False):

        formData = {"username": self.username, "password": self.password, "images.x": 46, "images.y": 38}
        r = self.session.post(self.baseUrl + self.loginUrl, headers=self.header, data=formData)
        r.encoding = 'gbk'
        if '对不起，帐号或密码不正确，请重新输入' in r.text:
            print(Exception("Error when login. Message: " + r.text))
            exit(0)

    def getExamID(self):

        # --- get Course ID START ---
        time.sleep(1)
        url = self.baseUrl + self.allCourseUrl
        print("--- get Course ID START ---")
        print("Handling url: " + url)

        r = self.session.get(url)
        r.encoding = 'gbk'
        responseData = r.text.split('\n')
        for line in responseData:
            if self.courseName in line:
                # print(line)
                allCourses = line.split('<tr>')
                for course in allCourses:
                    if self.courseName in course:
                        try: 
                            self.courseID = re.findall(r'kaoshi.asp\?courseid=([0-9]+)', course)[0]
                            break
                        except:
                            # only happens when the website interface changes
                            print(Exception("Error when parse line to courseID. Please contact the developper at ahangge@ruc.edu.cn"))
                            exit(0)
                break
        
        if not self.courseID:
            print(Exception("Can't find the course: " + self.courseName))
            exit(0)

        print("You are using course: " + self.courseName + " with courseID " + str(self.courseID))
        print("--- get Course ID END ---\n\n")

        time.sleep(1)
        # --- get Exam ID START ---

        url = self.baseUrl + self.allExamUrl + str(self.courseID)
        print("--- get Exam ID START ---")
        print("Handling url: " + url)

        r = self.session.get(url)
        r.encoding = 'gbk'
        responseData = r.text.split('\n')
        for line in responseData:
            if self.examName in line:
                allExams = line.split('<tr>')
                for exam in allExams:
                    if self.examName in exam:
                        try: 
                            self.examID = re.findall(r'search_score.asp\?kaoshiid=([0-9]+)', exam)[0]
                            break
                        except:
                            # only happens when the website interface changes
                            print(Exception("Error when parse line to examID. Please contact the developper at ahangge@ruc.edu.cn"))
                            exit(0)
                break
        
        if not self.examID:
            print(Exception("Can't find the exam: " + self.examName))
            exit(0)

        print("You are using exam: " + self.examName + "with examID " + str(self.examID))
        print("--- get Exam ID END ---\n\n")

    
    
    """
    考试题目有选择题、简答题、综合题、操作题，目前功能只是下载综合题的附件
    以后可能开发的功能包括但不限于：
    - 一键判分（不推荐开发，判分出错出了问题不好处理，手动判分相对也不会太慢）
    - 下载其他题目的附件，不清楚简答题、操作题存不存在有附件的情况
    """
    def downloadAppendix(self):

        time.sleep(1)
        # goto all papers page in this exam START

        url = self.baseUrl + self.zongAwardUrl + self.examID
        print("--- Go to 综合题 scored page START ---")
        print("Handling url: " + url)


        r = self.session.get(url)
        r.encoding = 'gbk'

        appendixTable = None
        try: 
            pageTable = None
            pageTr = None
            tableIterator = BeautifulSoup(r.text, 'lxml').body.children
            for i, item in enumerate(tableIterator):
                if i == 4:
                    pageTable = item

            for i, item in enumerate(pageTable.children):
                if i == 1:
                    pageTr = item
            
            self.appendixPage = 0

            for i, item in enumerate(pageTr.td.children):
                if i % 3 == 0:
                    self.appendixPage += 1

            # for i, item in enumerate(pageTr.td):
            #     print(i)
            #     print(item)
                    
        # find out how many page
        except:
            # only happens when the website interface changes
            print(Exception("Error when get page number. Please contact the developper at ahangge@ruc.edu.cn"))
            exit(0)


        if not self.appendixPage:
            # only happens when the website interface changes
            print(Exception("Error when get page number. Please contact the developper at ahangge@ruc.edu.cn\nOr there might be nothing needed to be scored."))
            exit(0)

        
        # --- Downloading Appendix Start ---

        errorlog = open(self.errorLog, 'w')
        

        for pageNum in range(1, self.appendixPage+1):
            
            studentID = ''
            appendixAddr = ''

            url = self.baseUrl + self.zongAwardUrl + self.examID + '&page=' + str(pageNum)
            print("\n--- Downloading Appendix of Page" + str(pageNum) + " START ---")
            print("Handling url: " + url)

            time.sleep(1)
            r = self.session.get(url)
            r.encoding = 'gbk'

            try:
                tableIterator = BeautifulSoup(r.text, 'lxml').body.children
                for i, item in enumerate(tableIterator):
                    if i == 3:
                        appendixTable = item
            
            except:
                # only happens when the website interface changes
                print(Exception("Error when parsing 综合题 page. Please contact the developper at ahangge@ruc.edu.cn"))
                exit(0)

            if not appendixTable.children:
                # only happens when the website interface changes
                print(Exception("Error when parsing 综合题 page. Please contact the developper at ahangge@ruc.edu.cn"))
                exit(0)
            
            for i, item in enumerate(appendixTable.children):
                if i < 2:
                    continue
                for j, column in enumerate(item.children):
                    if j == 0: # get StudentID
                        try:
                            studentID = re.findall(r'href="exercise.asp\?username=([0-9]*)', str(column))[0]
                        except:
                            # only happens when the website interface changes
                            print(Exception("Error when get studentID. Please contact the developper at ahangge@ruc.edu.cn"))
                    if j == 4: # get appendix downloading address
                        try:
                            appendixAddr = column.a["href"]
                        except:
                            # only happens when the website interface changes
                            print(Exception("Error when get appendix Address. Please contact the developper at ahangge@ruc.edu.cn"))
                            exit(0)

                # --- save appendix to localDict --- 

                if not studentID or not appendixAddr:
                    # only happens when the website interface changes
                    print(Exception("Error when parsing studentID or appendixAddr. Please contact the developper at ahangge@ruc.edu.cn"))
                    exit(0)
                
                print("\nDownloading " + studentID + "'s appendix")
                savepath = self.savedir + "\\" + studentID + "." + appendixAddr.split('.')[-1]
                
                url = self.downloadBaseUrl + appendixAddr[4:]
                print("Handling url: " + url)

                time.sleep(1)
                r = self.session.get(url)
                
                try:
                    with open(savepath, 'wb') as appendix:
                        appendix.write(r.content)
                    
                    if os.path.exists(savepath):
                        print('Save appendix to ' + savepath)
                    else:
                        print(Exception("Error when saving appendix. Please contact the developper at ahangge@ruc.edu.cn"))
                        exit(0)
                except:
                    print("Error when saving " + savepath + ", write it in error log")
                    errorlog.write(studentID + ": " + savepath + "\n")
        
        
        print("\n\n--- Downloading all Appendix END ---\n\n")
        print("Your files are save as .\\appendix\\studentID.zip or some else zipped format.")
        print("\n\n--- Exit --- \n\n")


    # TODO: Extract all print to a log class
