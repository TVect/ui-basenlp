import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

import random
import codecs
import jieba
import jieba.posseg as pseg

from rules import basic_rules, Word

from med_base.storage.neo4j.models import Symptom, Drug, Bodypart, Department, \
                            Operation, Examination, Disease
from med_base.storage.es.models import EntityDisease, EntityBodypart, EntityDepartment, \
                            EntityDrug, EntityExam, EntityOperation, EntitySymptom

from elasticsearch_dsl.connections import connections
from py2neo import Graph
from conf.settings import NEO4J_URI, ES_HOST

graph = Graph(NEO4J_URI)
connections.create_connection(hosts=[ES_HOST])

for filename in os.listdir("user_dict"):
    jieba.load_userdict(os.path.join("user_dict", filename))


from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


class QueryParser:
    
    def __init__(self):
        self.client = Elasticsearch(hosts=[ES_HOST])
    
    
    def nl2query(self, sentence):
        ''' 自然语言转查询表达式 '''
        tokens = pseg.lcut(sentence)
        words = []
        for idx, token in enumerate(tokens):
            if token.flag == "nz":
                recog_token = self.recognize_type(token.word)
                if recog_token:
                    tokens[idx].flag = "nz-{}".format(recog_token[0])
                    tokens[idx].word = recog_token[1]
        words = [Word(token=token.word, pos=token.flag) for token in tokens]
        print("parsed: ", tokens)
        candi_queries = []
        for rule in basic_rules:
            ret = rule.apply(words)
            if ret:
                candi_queries.append(rule.apply(words))
        if candi_queries:
            return random.choice(candi_queries)


    def recognize_type(self, name):
        s = Search(using=self.client, index="med_base").query("match", name=name)
        response = s.execute()

        for hit in response:
            # print(hit.meta.doc_type, hit.meta.score, hit.name)
            return hit.meta.doc_type, hit.name


if __name__ == "__main__":
    qp = QueryParser()
    print(qp.nl2query("什么病要吃定坤丹?"))
#     print(qp.parse("尿路感染要做手术吗?"))
#     print(qp.parse("头痛怎么办"))
#     print(qp.parse("头老是痛怎么办?"))
