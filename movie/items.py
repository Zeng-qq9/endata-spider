# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieYear(scrapy.Item):
    movieName = scrapy.Field()
    movieId = scrapy.Field()
    totalPrice = scrapy.Field()
    averPrice = scrapy.Field()
    averPeople = scrapy.Field()
    ReleaseTime = scrapy.Field()
    # Detail
    Genre_Main = scrapy.Field()
    MovieDyan = scrapy.Field()
    MovieYyuan = scrapy.Field()
    MovieZz = scrapy.Field()
    MovieFxAll = scrapy.Field()
    Type2D = scrapy.Field()
    Type3D = scrapy.Field()
    TypeIMAX = scrapy.Field()
    Runtime = scrapy.Field()
    #week
    MovieWeek = scrapy.Field()
    startdate = scrapy.Field()
    enddate = scrapy.Field()
    WeekAmount = scrapy.Field()
    SumWeekAmount = scrapy.Field()
    AvgPeople = scrapy.Field()
    MovieDays = scrapy.Field()


class MovieWeek(scrapy.Item):
    MovieID = scrapy.Field()
    MovieName = scrapy.Field()
    BoxOffice = scrapy.Field()
    AvgPeople = scrapy.Field()
    ReleaseTime = scrapy.Field()
