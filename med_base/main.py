import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../")
from med_base.storage.neo4j.models import Disease, Department
from med_base.storage.es.models import EntityDisease, EntityBodypart, EntityDepartment, \
            EntityDrug, EntityExam, EntityOperation, EntitySymptom
from elasticsearch_dsl.connections import connections

from py2neo import Graph
from conf.settings import NEO4J_URI, ES_HOST
graph = Graph(NEO4J_URI)
connections.create_connection(hosts=[ES_HOST])


def dump2nt_disease():
    t_entity = "http://wowjoy.cn/medbase/disease/{}"
    p_name = "http://wowjoy.cn/medbase/disease/name"
    p_describe = "http://wowjoy.cn/medbase/disease/describe"
    # alias = Keyword()
    p_is_infect = "http://wowjoy.cn/medbase/disease/is_infect"
    p_highrisk_group = "http://wowjoy.cn/medbase/disease/highrisk_group"
    p_source_url = "http://wowjoy.cn/medbase/disease/source_url"
    # p_treatment_cycle = "http://wowjoy.cn/medbase/disease/treatment_cycle"
    # p_treatment_cost = "http://wowjoy.cn/medbase/disease/treatment_cost"

    for disease in EntityDisease.search().scan():
        s_entity = "http://wowjoy.cn/medbase/disease/{}".format(disease._id)
        
        print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=disease.name))
        if disease.alias:
            for alias in disease.alias:
                print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=alias))
        
        # if disease.describe:
        #     print("<{s}> <{p}> {o} .".format(s=s_entity, p=p_describe, o=disease.describe))
        if disease.is_infect:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_is_infect, o=disease.is_infect))
        if disease.highrisk_group:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_highrisk_group, o=disease.highrisk_group))
        if disease.source_url:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_source_url, o=disease.source_url))


def dump2nt_department():
    t_entity = "http://wowjoy.cn/medbase/depart/{}"
    p_name = "http://wowjoy.cn/medbase/depart/name"
    
    for depart_item in Department.match(graph):
        s_entity = t_entity.format(depart_item.id)
        print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=depart_item.name))
        
    '''
    for department in EntityDepartment.search().scan():
        s_entity = "http://wowjoy.cn/medbase/depart/{}".format(department._id)
        print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=department.name))
        if department.source_url:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_source_url, o=department.source_url))
    '''

def dump2nt_drug():
    t_entity = "http://wowjoy.cn/medbase/drug/{}"
    p_name = "http://wowjoy.cn/medbase/drug/name"
    p_source_url = "http://wowjoy.cn/medbase/drug/source_url"

    for drug in EntityDrug.search().scan():
        s_entity = "http://wowjoy.cn/medbase/drug/{}".format(drug._id)
        print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=drug.name))
        if drug.source_url:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_source_url, o=drug.source_url))


def dump2nt_exam():
    t_entity = "http://wowjoy.cn/medbase/exam/{}"
    p_name = "http://wowjoy.cn/medbase/exam/name"
    p_source_url = "http://wowjoy.cn/medbase/exam/source_url"

    for exam in EntityExam.search().scan():
        s_entity = "http://wowjoy.cn/medbase/exam/{}".format(exam._id)
        print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=exam.name))
        if exam.source_url:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_source_url, o=exam.source_url))


def dump2nt_operation():
    t_entity = "http://wowjoy.cn/medbase/operation/{}"
    p_name = "http://wowjoy.cn/medbase/operation/name"
    p_source_url = "http://wowjoy.cn/medbase/operation/source_url"

    for operation in EntityOperation.search().scan():
        s_entity = "http://wowjoy.cn/medbase/operation/{}".format(operation._id)
        print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=operation.name))
        if operation.source_url:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_source_url, o=operation.source_url))


def dump2nt_symptom():
    t_entity = "http://wowjoy.cn/medbase/symptom/{}"
    p_name = "http://wowjoy.cn/medbase/symptom/name"
    p_describe = "http://wowjoy.cn/medbase/symptom/describe"
    p_source_url = "http://wowjoy.cn/medbase/symptom/source_url"

    for symptom in EntitySymptom.search().scan():
        s_entity = "http://wowjoy.cn/medbase/symptom/{}".format(symptom._id)
        print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_name, o=symptom.name))
        if symptom.source_url:
            print('<{s}> <{p}> "{o}" .'.format(s=s_entity, p=p_source_url, o=symptom.source_url))
        # if symptom.describe:
        #     print("<{s}> <{p}> {o} .".format(s=s_entity, p=p_describe, o=symptom.describe))


def dump2nt_relations():
    entity_disease = "http://wowjoy.cn/medbase/disease/{}"
    entity_symptom = "http://wowjoy.cn/medbase/symptom/{}"
    entity_depart = "http://wowjoy.cn/medbase/depart/{}"
    entity_exam = "http://wowjoy.cn/medbase/exam/{}"
    entity_drug = "http://wowjoy.cn/medbase/drug/{}"
    entity_operation = "http://wowjoy.cn/medbase/operation/{}"
    for disease_item in Disease.match(graph):
        # related_symptom = RelatedTo('Symptom')
        for symptom_item in disease_item.related_symptom:
            print("<{s}> <{p}> <{o}> .".format(s=entity_disease.format(disease_item.id), 
                                         p="http://wowjoy.cn/medbase/relation/related_symptom", 
                                         o=entity_symptom.format(symptom_item.id)))
        # related_depart = RelatedTo('Department')
        for depart_item in disease_item.related_depart:
            print("<{s}> <{p}> <{o}> .".format(s=entity_disease.format(disease_item.id), 
                                         p="http://wowjoy.cn/medbase/relation/related_depart", 
                                         o=entity_depart.format(depart_item.id)))
        # related_exam = RelatedTo('Examination')
        for exam_item in disease_item.related_exam:
            print("<{s}> <{p}> <{o}> .".format(s=entity_disease.format(disease_item.id), 
                                         p="http://wowjoy.cn/medbase/relation/related_exam", 
                                         o=entity_exam.format(exam_item.id)))
        # related_drug = RelatedTo('Drug')
        for drug_item in disease_item.related_drug:
            print("<{s}> <{p}> <{o}> .".format(s=entity_disease.format(disease_item.id), 
                                         p="http://wowjoy.cn/medbase/relation/related_drug", 
                                         o=entity_drug.format(drug_item.id)))
        # related_operation = RelatedTo('Operation')
        for operation_item in disease_item.related_operation:
            print("<{s}> <{p}> <{o}> .".format(s=entity_disease.format(disease_item.id), 
                                         p="http://wowjoy.cn/medbase/relation/related_operation", 
                                         o=entity_operation.format(operation_item.id)))


def dump2nt():
    dump2nt_disease()
    dump2nt_department()
    dump2nt_drug
    dump2nt_exam()
    dump2nt_operation()
    dump2nt_symptom()


if __name__ == "__main__":
    import codecs
    outputfile=codecs.open("./medbase.nt", mode="a", encoding="utf-8")
    sys.stdout=outputfile
    dump2nt()
    dump2nt_relations()

