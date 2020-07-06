# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class CalculateAreaPipeline(object):
    def process_item(self, item, spider):
        if 're_area' not in item or not isinstance(item['re_area'], float):
            if 're_width' in item and 're_length' in item and \
                isinstance(item['re_width'], float) and isinstance(item['re_length'], float):
                item['re_area'] = item['re_width'] * item['re_length']
            elif 're_area_to_use' in item:
                item['re_area'] = item['re_area_to_use']

        return item

class SavePostPipeline(object):
    def __init__(self):
        pass

    def open_spider(self, spider):
        self.client = MongoClient(settings.get("CONNECTION_STRING"))
        self.db = self.client[settings.get("DB_NAME")]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        posts = self.db['post']
        posts.insert_one(dict(item))
        return item
