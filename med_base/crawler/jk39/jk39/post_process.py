import hashlib
import requests
import random
import urllib
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../../")
from med_base.storage.neo4j.models import Symptom, Drug, Bodypart, Department, \
                            Operation, Examination, Disease
from med_base.storage.es.models import EntityDisease, EntityBodypart, EntityDepartment, \
                            EntityDrug, EntityExam, EntityOperation, EntitySymptom

from elasticsearch_dsl.connections import connections
from py2neo import Graph
from conf.settings import NEO4J_URI, ES_HOST


graph = Graph(NEO4J_URI)
connections.create_connection(hosts=[ES_HOST])

def get_node_by_id(entityType, id):
    entity_node_dict = {"symptom": [EntitySymptom, Symptom],
                        "disease": [EntityDisease, Disease],
                        "exam": [EntityExam, Examination],
                        "drug": [EntityDrug, Drug],
                        "operation": [EntityOperation, Operation],
                        "bodypart": [None, Bodypart],
                        "depart": [None, Department]}
    entityClass = entity_node_dict[entityType][0]
    nodeClass = entity_node_dict[entityType][1]
    
    node = nodeClass.match(graph).where("_.id = '{}'".format(id)).first()
    if not node:
        try:
            entity = entityClass.get(id=id)
            node = nodeClass()
            node.name = entity.name
            node.id = str(entity._id)
        except Exception as e:
            print(e)
    return node


def get_node_by_name(entityType, name):
    node_dict = {"bodypart": Bodypart, "depart": Department}
    return node_dict[entityType].match(graph).where("_.name = '{}'".format(name)).first()


def to_uuid(in_str):
    hl = hashlib.md5()
    hl.update(in_str.encode(encoding="utf-8"))
    return hl.hexdigest()


with open("relations.nt") as fr:
    for line_id, line in enumerate(fr):
        print(line_id, line)
        tokens = line.split()
        from_url = tokens[0][1:-1]
        rel_url = tokens[1][1:-1]
        to_url = tokens[2][1:-1]
        
        from_id = to_uuid(from_url)
        to_id = to_uuid(to_url)
        
        rel_tokens = rel_url.split("/")
        rel_type = rel_tokens[-1]
        from_type = rel_tokens[-2]
        
        if from_type == "disease":
            from_node = get_node_by_id("disease", from_id)
            if not from_node:
                continue
            if rel_type == "related_symptom":
                to_node = get_node_by_id("symptom", to_id)
                if to_node:
                    from_node.related_symptom.add(to_node)
            elif rel_type == "related_disease":
                to_node = get_node_by_id("disease", to_id)
                if to_node:
                    from_node.related_disease.add(to_node)
            elif rel_type == "related_bodypart":
                to_node = get_node_by_id("bodypart", to_id)
                if to_node:
                    from_node.related_bodypart.add(to_node)
            elif rel_type == "related_depart":
                to_node = get_node_by_id("depart", to_id)
                if to_node:
                    from_node.related_depart.add(to_node)
            elif rel_type == "related_exam":
                to_node = get_node_by_id("exam", to_id)
                if to_node:
                    from_node.related_exam.add(to_node)
            elif rel_type == "related_drug":
                to_node = get_node_by_id("drug", to_id)
                if to_node:
                    from_node.related_drug.add(to_node)
            elif rel_type == "related_operation":
                to_node = get_node_by_id("operation", to_id)
                if to_node:
                    from_node.related_operation.add(to_node)
            
        elif from_type == "exam":
            from_node = get_node_by_id("exam", from_id)
            if rel_type == "related_bodypart":
                to_node = get_node_by_id("bodypart", to_id)
                if to_node:
                    from_node.related_bodypart.add(to_node)

        elif from_type == "operation":
            from_node = get_node_by_id("operation", from_id)
            if rel_type == "related_depart":
                to_node = get_node_by_id("depart", to_id)
                if to_node:
                    from_node.related_depart.add(to_node)
            elif rel_type == "related_bodypart":
                to_node = get_node_by_id("bodypart", to_id)
                if to_node:
                    from_node.related_bodypart.add(to_node)

        graph.push(from_node)
