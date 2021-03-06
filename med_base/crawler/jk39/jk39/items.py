# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DiseaseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    describe = scrapy.Field()
    # alias = scrapy.Field()
    is_infect = scrapy.Field()
    highrisk_group = scrapy.Field()
    source_url = scrapy.Field()
    treatment_cycle = scrapy.Field()
    treatment_cost = scrapy.Field()

    related_symptom = scrapy.Field()
    related_disease = scrapy.Field()
    related_bodypart = scrapy.Field()
    related_depart = scrapy.Field()
    related_exam = scrapy.Field()
    related_drug = scrapy.Field()
    related_operation = scrapy.Field()


class ExamItem(scrapy.Item):
    name = scrapy.Field()
    describe = scrapy.Field()
    source_url = scrapy.Field()

    related_bodypart = scrapy.Field()
    related_disease = scrapy.Field()


class DrugItem(scrapy.Item):
    name = scrapy.Field()
#     composition = scrapy.Field()
#     indication= scrapy.Field()
#     usage = scrapy.Field()
    source_url = scrapy.Field()


class OperationItem(scrapy.Item):
    name = scrapy.Field()
    describe = scrapy.Field()
    source_url = scrapy.Field()

    related_depart = scrapy.Field()
    related_bodypart = scrapy.Field()


class SymptomItem(scrapy.Item):
    name = scrapy.Field()
    describe = scrapy.Field()
    source_url = scrapy.Field()