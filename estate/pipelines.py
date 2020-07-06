# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class SavePostPipeline(object):
    def __init__(self):
        pass

    def open_spider(self, spider):
        self.client = MongoClient(settings.get("CONNECTION_STRING"))
        self.db = client[settings.get["DB_NAME"]]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        posts = self.db['post']
        posts.insert_one(item)
        return item
