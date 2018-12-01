# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuazisecarItem(scrapy.Item):
    # 设置需要提取的数据为键名 key
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    mile = scrapy.Field()
    price = scrapy.Field()
