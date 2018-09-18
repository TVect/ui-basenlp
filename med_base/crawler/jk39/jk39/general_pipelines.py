# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from jk39.items import DiseaseItem, ExamItem, DrugItem, OperationItem


class GeneralItemPipeline(object):
    
    def __init__(self, out_file):
        self.out_file = out_file


    @classmethod
    def from_crawler(cls, crawler):
        return cls(out_file=crawler.settings.get('OUT_FILE'))


    def process_item(self, item, spider):
        with open(self.out_file, 'a') as fw:
            if isinstance(item, DiseaseItem):
                spider.logger.info('====== SAVE A Disease: name={} ======'.format(item.get('name', '').strip()))
                if item.get('name', '').strip():
                    fw.write('<{}> <http://wowjoy.com/disease/name> "{}" .\n'.\
                             format(item.get('source_url'), item.get('name').strip()))
                if item.get('describe', '').strip():
                    fw.write('<{}> <http://wowjoy.com/disease/describe> "{}" .\n'.\
                             format(item.get('source_url'), item.get('describe').strip()))
                if item.get('is_infect', '').strip():
                    fw.write('<{}> <http://wowjoy.com/disease/is_infect> "{}" .\n'.\
                             format(item.get('source_url'), item.get('is_infect').strip()))
                if item.get('highrisk_group', '').strip():
                    fw.write('<{}> <http://wowjoy.com/disease/highrisk_group> "{}" .\n'.\
                             format(item.get('source_url'), item.get('highrisk_group').strip()))
                if item.get('treatment_cycle', '').strip():
                    fw.write('<{}> <http://wowjoy.com/disease/treatment_cycle> "{}" .\n'.\
                             format(item.get('source_url'), item.get('treatment_cycle').strip()))
                if item.get('treatment_cost', '').strip():
                    fw.write('<{}> <http://wowjoy.com/disease/treatment_cost> "{}" .\n'.\
                             format(item.get('source_url'), item.get('treatment_cost').strip()))
                if item.get('related_symptom'):
                    for symptom in item.get('related_symptom'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_symptom> <{}> .\n'.\
                                 format(item.get('source_url'), symptom))
                if item.get('related_disease'):
                    for disease in item.get('related_disease'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_disease> <{}> .\n'.\
                                 format(item.get('source_url'), disease))
                if item.get('related_bodypart'):
                    for bodypart in item.get('related_bodypart'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_bodypart> <{}> .\n'.\
                                 format(item.get('source_url'), bodypart))
                if item.get('related_depart'):
                    for depart in item.get('related_depart'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_depart> <{}> .\n'.\
                                 format(item.get('source_url'), depart))
                if item.get('related_exam'):
                    for exam in item.get('related_exam'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_exam> <{}> .\n'.\
                                 format(item.get('source_url'), exam))
                if item.get('related_drug'):
                    for drug in item.get('related_drug'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_drug> <{}> .\n'.\
                                 format(item.get('source_url'), drug))
                if item.get('related_operation'):
                    for operation in item.get('related_operation'):
                        fw.write('<{}> <http://wowjoy.com/disease/related_operation> <{}> .\n'.\
                                 format(item.get('source_url'), operation))
            elif isinstance(item, ExamItem):
                spider.logger.info('====== SAVE A Exam: name={} ======'.format(item.get('name', '').strip()))
                if item.get('name', '').strip():
                    fw.write('<{}> <http://wowjoy.com/exam/name> "{}" .\n'.\
                             format(item.get('source_url'), item.get('name').strip()))
                if item.get('describe', '').strip():
                    fw.write('<{}> <http://wowjoy.com/exam/describe> "{}" .\n'.\
                             format(item.get('source_url'), item.get('describe').strip()))
                if item.get('related_bodypart'):
                    for bodypart in item.get('related_bodypart'):
                        fw.write('<{}> <http://wowjoy.com/exam/related_bodypart> <{}> .\n'.\
                                 format(item.get('source_url'), bodypart))
                if item.get('related_disease'):
                    for disease in item.get('related_disease'):
                        fw.write('<{}> <http://wowjoy.com/exam/related_disease> <{}> .\n'.\
                                 format(item.get('source_url'), disease))
            elif isinstance(item, DrugItem):
                spider.logger.info('====== SAVE A Drug: name={} ======'.format(item.get('name', '').strip()))
                if item.get('name', '').strip():
                    fw.write('<{}> <http://wowjoy.com/drug/name> "{}" .\n'.\
                             format(item.get('source_url'), item.get('name').strip()))
                if item.get('composition', '').strip():
                    fw.write('<{}> <http://wowjoy.com/drug/composition> "{}" .\n'.\
                             format(item.get('source_url'), item.get('composition').strip()))
#                 if item.get('indication', '').strip():
#                     fw.write('<{}> <http://wowjoy.com/drug/indication> "{}" .\n'.\
#                              format(item.get('source_url'), item.get('indication').strip()))
#                 if item.get('usage', '').strip():
#                     fw.write('<{}> <http://wowjoy.com/drug/usage> "{}" .\n'.\
#                              format(item.get('source_url'), item.get('usage').strip()))
            elif isinstance(item, OperationItem):
                spider.logger.info('====== SAVE A Operation: name={} ======'.format(item.get('name', '').strip()))
                if item.get('name', '').strip():
                    fw.write('<{}> <http://wowjoy.com/operation/name> "{}" .\n'.\
                             format(item.get('source_url'), item.get('name').strip()))
                if item.get('describe', '').strip():
                    fw.write('<{}> <http://wowjoy.com/operation/describe> "{}" .\n'.\
                             format(item.get('source_url'), item.get('describe').strip()))
                if item.get('related_depart'):
                    for depart in item.get('related_depart'):
                        fw.write('<{}> <http://wowjoy.com/operation/related_depart> <{}> .\n'.\
                                 format(item.get('source_url'), depart))
                if item.get('related_bodypart'):
                    for bodypart in item.get('related_bodypart'):
                        fw.write('<{}> <http://wowjoy.com/operation/related_bodypart> <{}> .\n'.\
                                 format(item.get('source_url'), bodypart))

