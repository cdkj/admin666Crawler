from admin666Crawler import Admin666RUCCrawler

if __name__ == "__main__":
    cookie = "csd=e; cod=a.e; _ga=GA1.3.1632699827.1662535486; amplitude_id_9f6c0bb8b82021496164c672a7dc98d6_edmruc.edu.cn=eyJkZXZpY2VJZCI6ImNlYWExZWU2LWJkYWEtNGU2MS05Zjg4LWRjZTFmMDRmNGZiNVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY2MzA1OTM0MTMzMCwibGFzdEV2ZW50VGltZSI6MTY2MzA1OTQ1NjkwOCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MjMsInNlcXVlbmNlTnVtYmVyIjoyM30=; amplitude_id_408774472b1245a7df5814f20e7484d0ruc.edu.cn=eyJkZXZpY2VJZCI6IjQxNGJiYzNlLWIwMzctNGYyZS04ODUzLWJmMzNmMjA3YmM2NiIsInVzZXJJZCI6Ii0yMjQ3MjM1MDgiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2NjMwNTkyOTIwMDEsImxhc3RFdmVudFRpbWUiOjE2NjMwNTk4NzQ4NjcsImV2ZW50SWQiOjYxLCJpZGVudGlmeUlkIjo5OCwic2VxdWVuY2VOdW1iZXIiOjE1OX0=; _hp2_id.1083010732=%7B%22userId%22%3A%224578495411548484%22%2C%22pageviewId%22%3A%222861783230050125%22%2C%22sessionId%22%3A%228204730282163158%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; ASPSESSIONIDAQSRTRRD=EFFIJBPBNKGIEAOAICCJINAB; ASPSESSIONIDASRTQQRC=HBJEKPOBFHBONNLGLNNOIOGI; flag=Teacher; access_token=pcwvEB1VR6u8RaQtlTt3BA; email=Zj%23%232022; realname=zjzj16; password=6796cf70de574e60; username=zjzj16; power=4; id=2149; logintime=2022%2F10%2F12+15%3A49%3A50"
    crawler = Admin666RUCCrawler(cookie, "问卷星数据收集作业（周一班）") # configure your exam name here
    crawler.checkDict()
    crawler.login()
    crawler.getExamID()
    crawler.downloadAppendix()