# -*- coding: utf-8 -*-
import scrapy
import json
from movie.items import MovieYear
import requests


class EndatayearSpider(scrapy.Spider):
    name = 'movieYear'
    allowed_domains = ['endata.com.cn']
    # start_urls = ['http://endata.com.cn/']
    # http://127.0.0.1:2345/getPage?year=2019&MethodName=BoxOffice_GetYearInfoData
    start_urls = []
    for i in range(2010, 2021):
        start_urls.append("http://127.0.0.1:2345/getPage?year={}&MethodName=BoxOffice_GetYearInfoData".format(i))

    def parse(self, response):
        data = response.text
        data = json.loads(data)
        data = data["Data"]["Table"]
        for i in data:
            item = MovieYear()
            item['movieName'] = i["MovieName"]
            item['movieId'] = i["Movieid"]
            item['totalPrice'] = i["BoxOffice"]
            item['averPrice'] = i["AvgPrice"]
            item['averPeople'] = i["AvgPeoPle"]
            item['ReleaseTime'] = i["ReleaseTime"]
            #detail
            data2 = self.sendReq("BoxOffice_GetMovieData_Details", i["Movieid"])
            data2 = json.loads(data2)
            data2 = data2["Data"]["Table"][0]

            t = data2["Genre_Main"].split("/")
            tl = []
            for j in range(len(t)-1):
                tl.append(t[j].split("|")[0])
            item['Genre_Main'] = "|".join(tl)

            t = data2["MovieDyan"].split("/")
            tl = []
            for j in range(len(t)-1):
                tl.append(t[j].split("|")[0].split(" ")[0])
            item['MovieDyan'] = ",".join(tl)
            #演员
            t = data2["MovieYyuan"].split("/")
            tl = []
            for j in range(len(t) - 1):
                tl.append(t[j].split("|")[0].split(" ")[0])
            item['MovieYyuan'] = ",".join(tl)

            try:
                t = data2["MovieZz"].split("/")
                tl = []
                for j in range(len(t) - 1):
                    tl.append(t[j].split("|")[0].split(" ")[0])
                item['MovieZz'] = ",".join(tl)
            except:
                pass

            t = data2["MovieFxAll"].split("/")
            tl = []
            for j in range(len(t) - 1):
                tl.append(t[j].split("|")[0])
            item['MovieFxAll'] = ",".join(tl)

            item['Type2D'] = data2["2D"]
            item['Type3D'] = data2["3D"]
            item['TypeIMAX'] = data2["IMAX"]
            item['Runtime'] = data2["Runtime"]

            #week
            data3 = self.sendReq("BoxOffice_GetMovieData_WeekBoxOffice", i["Movieid"])
            data3 = json.loads(data3)
            data3 = data3["Data"]["Table"]
            data3 = data3[len(data3)-1]
            item['MovieWeek'] = data3["MovieWeek"]
            item['startdate'] = data3["startdate"]
            item['enddate'] = data3["enddate"]
            item['WeekAmount'] = data3["WeekAmount"]
            item['SumWeekAmount'] = data3["SumWeekAmount"]
            item['AvgPeople'] = data3["AvgPeople"]
            item['MovieDays'] = data3["MovieDays"]

            yield item

    def sendReq(self, MethodName, movieId):
        url = "http://www.endata.com.cn/API/GetData.ashx"
        d = {'MethodName': MethodName, "movieId": movieId}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        r = requests.post(url, data=d, headers=headers)
        return r.text
