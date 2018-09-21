import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

from med_base.storage.neo4j.models import Symptom, Drug, Bodypart, Department, \
                            Operation, Examination, Disease
from med_base.storage.es.models import EntityDisease, EntityBodypart, EntityDepartment, \
                            EntityDrug, EntityExam, EntityOperation, EntitySymptom

from elasticsearch_dsl.connections import connections
from py2neo import Graph
from conf.settings import NEO4J_URI, ES_HOST

from app.med_qa.parser import QueryParser

class QAMain:
    
    def __init__(self):
        self.parser = QueryParser()
        self.graph = Graph(NEO4J_URI)

    def response(self, sentence):
        query_str = self.parser.nl2query(sentence)
        if query_str:
            return [di["name"] for di in self.graph.run(query_str).data()]
        else:
            return "sorry, 我没有听懂您的意思。。。    (灬ꈍ ꈍ灬)"


if __name__ == "__main__":
    qa = QAMain()
    print(qa.response("什么病要吃强肾片?"))
    print(qa.response("强肾片是管什么疾病的?"))
    print(qa.response("多动症要吃什么药?"))
    print(qa.response("慢性胃炎要服用什么药物?"))
