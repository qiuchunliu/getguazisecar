# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class GuazisecarPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(host='localhost',
                                       password='1234',
                                       user='root',
                                       database='secar',
                                       port=3306
                                       )
        self.cursor = self.connect.cursor()
        self.cursor.execute('create table if not exists secarscrapy('
                            'id int(10) unsigned not null auto_increment primary key ,'
                            'title varchar(255) not null,'
                            'mile varchar(255) not null,'
                            'price varchar(255) not null);')

    def process_item(self, item, spider):
        sql = 'insert into secarscrapy(title, mile, price) values(%s,%s,%s)'
        self.cursor.execute(sql, (item['title'], item['mile'], item['price']))
        self.connect.commit()
        # self.connect.close()
        return item
