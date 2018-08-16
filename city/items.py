# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    serial_number = scrapy.Field()
    # 名称
    movie_name = scrapy.Field()
    # 介绍
    introduce = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 评论
    evaluate = scrapy.Field()
    # 描述
    describe = scrapy.Field()
    # 星级
    level_1 = scrapy.Field()
    level_2 = scrapy.Field()
    level_3 = scrapy.Field()
    level_4 = scrapy.Field()
    level_5 = scrapy.Field()
    level_6 = scrapy.Field()
