# -*- coding: utf-8 -*-
import scrapy
from guazisecar.items import GuazisecarItem


class SecarcodeSpider(scrapy.Spider):
    name = 'secarcode'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/ningde/buy/o1i7/']
    domain_url = 'https://www.guazi.com'

    def parse(self, response):
        lis = response.xpath('//ul[@class="carlist clearfix js-top"]//li')
        # 每个车辆信息存在一个 li 里
        for each in lis:
            title = each.xpath('./a/@title').get()
            mile = ''.join(each.xpath('.//div[@class="t-i"]/text()').getall())
            price = ''.join(each.xpath('.//div[@class="t-price"]/p//text()').getall())
            item = GuazisecarItem(title=title, mile=mile, price=price)
            yield item
        # print(lis)
        print('爬取了一页')
        next_page_url = (self.domain_url +
                         response.xpath('//ul[@class="pageLink clearfix"]/li[last()]/a/@href').get())
        span = response.xpath('//ul[@class="pageLink clearfix"]/li[last()]/a/span/text()').get()
        if span == '下一页':
            print('****爬取了一页****')
            yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            print('********爬取结束********')
            return
