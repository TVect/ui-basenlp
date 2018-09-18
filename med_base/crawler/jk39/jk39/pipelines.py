# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import hashlib
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../../")

from med_base.storage.es.models import EntityDisease, EntityBodypart, EntityDepartment, \
                            EntityDrug, EntityExam, EntityOperation, EntitySymptom

from elasticsearch_dsl.connections import connections
from conf.settings import ES_HOST

connections.create_connection(hosts=[ES_HOST])


from jk39.items import DiseaseItem, ExamItem, DrugItem, OperationItem, SymptomItem


class EntityItemPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, DiseaseItem):
            spider.logger.info('====== SAVE A Entity Disease: name={} ======'.format(item.get('name', '').strip()))
            meta_dict = {}
            for key in ['name', 'describe', 'is_infect', 'highrisk_group', 
                        'source_url', 'treatment_cycle', 'treatment_cost']:
                if item.get(key, '').strip():
                    meta_dict[key] = item.get(key, '').strip()
            disease_item = EntityDisease(**meta_dict)
            disease_item.save()
        elif isinstance(item, ExamItem):
            spider.logger.info('====== SAVE A Entity Exam: name={} ======'.format(item.get('name', '').strip()))
            meta_dict = {}
            for key in ['name', 'describe', 'source_url']:
                if item.get(key, '').strip():
                    meta_dict[key] = item.get(key, '').strip()
            exam_item = EntityExam(**meta_dict)
            exam_item.save()
        elif isinstance(item, DrugItem):
            spider.logger.info('====== SAVE A Entity Drug: name={} ======'.format(item.get('name', '').strip()))
            meta_dict = {}
            for key in ['name', 'source_url']:
                if item.get(key, '').strip():
                    meta_dict[key] = item.get(key, '').strip()
            drug_item = EntityDrug(**item)
            drug_item.save()
        elif isinstance(item, OperationItem):
            spider.logger.info('====== SAVE A Entity Operation: name={} ======'.format(item.get('name', '').strip()))
            meta_dict = {}
            for key in ['name', 'describe', 'source_url']:
                if item.get(key, '').strip():
                    meta_dict[key] = item.get(key, '').strip()
            operation_item = EntityOperation(**meta_dict)
            operation_item.save()
        elif isinstance(item, SymptomItem):
            pass
        yield item


class RelationItemPipeline(object):
    
    def __init__(self, relation_file):
        self.relation_file = relation_file


    @classmethod
    def from_crawler(cls, crawler):
        return cls(relation_file=crawler.settings.get('RELATION_FILE'))


    def process_item(self, item, spider):
        with open(self.relation_file, 'a') as fw:
            if isinstance(item, DiseaseItem):
                spider.logger.info('====== SAVE A Disease Relation: name={} ======'.format(item.get('name', '').strip()))
                if item.get('related_symptom'):
                    for symptom in item.get('related_symptom'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_symptom> <{}> .\n'.\
                                 format(item.get('source_url').strip(), symptom))
                if item.get('related_disease'):
                    for disease in item.get('related_disease'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_disease> <{}> .\n'.\
                                 format(item.get('source_url').strip(), disease))
                if item.get('related_bodypart'):
                    for bodypart in item.get('related_bodypart'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_bodypart> <{}> .\n'.\
                                 format(item.get('source_url').strip(), bodypart))
                if item.get('related_depart'):
                    for depart in item.get('related_depart'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_depart> <{}> .\n'.\
                                 format(item.get('source_url').strip(), depart))
                if item.get('related_exam'):
                    for exam in item.get('related_exam'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_exam> <{}> .\n'.\
                                 format(item.get('source_url').strip(), exam))
                if item.get('related_drug'):
                    for drug in item.get('related_drug'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_drug> <{}> .\n'.\
                                 format(item.get('source_url').strip(), drug))
                if item.get('related_operation'):
                    for operation in item.get('related_operation'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_operation> <{}> .\n'.\
                                 format(item.get('source_url').strip(), operation))
            elif isinstance(item, ExamItem):
                spider.logger.info('====== SAVE A Exam Relation: name={} ======'.format(item.get('name', '').strip()))
                if item.get('related_bodypart'):
                    for bodypart in item.get('related_bodypart'):
                        fw.write('<{}> <http://wowjoy.com/exam/related_bodypart> <{}> .\n'.\
                                 format(item.get('source_url').strip(), bodypart))
                if item.get('related_disease'):
                    for disease in item.get('related_disease'):
                        fw.write('<{}> <http://wowjoy.com/exam/related_disease> <{}> .\n'.\
                                 format(item.get('source_url').strip(), disease))
            elif isinstance(item, DrugItem):
                pass
            elif isinstance(item, OperationItem):
                spider.logger.info('====== SAVE A Operation Relation: name={} ======'.format(item.get('name', '').strip()))
                if item.get('related_depart'):
                    for depart in item.get('related_depart'):
                        fw.write('<{}> <http://wowjoy.com/operation/related_depart> <{}> .\n'.\
                                 format(item.get('source_url').strip(), depart))
                if item.get('related_bodypart'):
                    for bodypart in item.get('related_bodypart'):
                        fw.write('<{}> <http://wowjoy.com/operation/related_bodypart> <{}> .\n'.\
                                 format(item.get('source_url').strip(), bodypart))
