# -*- coding: utf-8 -*-
import scrapy
from city.items import CityItem

class CitySpiderSpider(scrapy.Spider):
    name = 'city_spider'
    allowed_domains = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9F%8E%E5%B8%82%E6%96%B0%E5%88%86%E7%BA%A7%E5%90%8D%E5%8D%95/12702007?fr=aladdin']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9F%8E%E5%B8%82%E6%96%B0%E5%88%86%E7%BA%A7%E5%90%8D%E5%8D%95/12702007?fr=aladdin/']

    def parse(self, response):
        city_item = CityItem()
        city_list = {}
        city_item['movie_name'] = response.xpath(".//div[@class='para-title level-3']/h3/text()").extract()
        i = 1
        while i <= 6:
            level = ('level_' + str(i))
            xpath = str(".//div[@class='para'][{}]/text()").format(2*i + 6)
            city_item[level] = response.xpath(xpath).extract_first()
            city_name = city_item[level].split('、')
            city_list.update({city_item['movie_name'][i-1]: city_name})
            i += 1
        yield city_list
