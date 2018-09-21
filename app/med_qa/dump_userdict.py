import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

import codecs
import jieba
import jieba.posseg as pseg

from med_base.storage.neo4j.models import Symptom, Drug, Bodypart, Department, \
                            Operation, Examination, Disease
from med_base.storage.es.models import EntityDisease, EntityBodypart, EntityDepartment, \
                            EntityDrug, EntityExam, EntityOperation, EntitySymptom

from elasticsearch_dsl.connections import connections
from py2neo import Graph
from conf.settings import NEO4J_URI, ES_HOST

graph = Graph(NEO4J_URI)
connections.create_connection(hosts=[ES_HOST])


templates = [{"file": "symptom.txt", "node_class": Symptom, "tag": "nz"},
             {"file": "drug.txt", "node_class": Drug, "tag": "nz"},
             {"file": "bodypart.txt", "node_class": Bodypart, "tag": "nz"},
             {"file": "department.txt", "node_class": Department, "tag": "nz"},
             {"file": "operation.txt", "node_class": Operation, "tag": "nz"},
             {"file": "examination.txt", "node_class": Examination, "tag": "nz"},
             {"file": "disease.txt", "node_class": Disease, "tag": "nz"}]

for template in templates:
    with codecs.open(template["file"], "w", encoding="utf-8") as fw:
        for node in template["node_class"].match(graph):
            try:
                fw.write("{} 99999999 {}\n".format(node.name, template["tag"]))
            except Exception as e:
                print(e)

# for node in graph.nodes.match():
#     jieba.suggest_freq(node["name"], tune=True)
