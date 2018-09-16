# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from jk39.items import DiseaseItem, ExamItem, DrugItem, OperationItem

class DiseaseItemPipeline(object):

    def process_item(self, item, spider):
        if item is DiseaseItem:
            print("save a DiseaseItem")
        else:
            return item


class ExamItemPipeline(object):

    def process_item(self, item, spider):
        if item is ExamItem:
            print("save a ExamItem")
        else:
            return item


class DrugItemPipeline(object):

    def process_item(self, item, spider):
        if item is DrugItem:
            print("save a DrugItem")
        else:
            return item


class OperationItemPipeline(object):

    def process_item(self, item, spider):
        if item is OperationItem:
            print("save a OperationItem")
        else:
            return item
