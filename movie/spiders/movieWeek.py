# -*- coding: utf-8 -*-
import scrapy
import json
from movie.items import MovieWeek

class MovieweekSpider(scrapy.Spider):
    name = 'movieWeek'
    allowed_domains = ['endata.com.cn']
    start_urls = []
    for i in range(2010, 2021):
        start_urls.append("http://127.0.0.1:2345/getPage?year={}&MethodName=BoxOffice_getYearInfo_fData".format(i))

    def parse(self, response):
        data = response.text
        data = json.loads(data)
        data = data["Data"]["Table"]
        for i in data:
            item = MovieWeek()
            item['MovieID'] = i["MovieID"]
            item['MovieName'] = i["MovieName"]
            item['BoxOffice'] = i["BoxOffice"]
            item['AvgPeople'] = i["AvgPeople"]
            item['ReleaseTime'] = i["ReleaseTime"]
            yield item
