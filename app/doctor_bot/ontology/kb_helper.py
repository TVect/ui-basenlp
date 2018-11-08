from SPARQLWrapper import SPARQLWrapper, JSON


class KBHelper:
    
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.sparql = SPARQLWrapper(self.endpoint)


    def query_relatedSymptom(self, disease_name):
        sparql_tem = """
            SELECT ?object_name
              WHERE {
                ?subject <http://wowjoy.cn/medbase/relation/related_symptom> ?object .
                ?subject <http://wowjoy.cn/medbase/disease/name> "%s" .
                ?object <http://wowjoy.cn/medbase/symptom/name> ?object_name .
              }"""
        sparql_str = sparql_tem % disease_name
        self.sparql.setQuery(sparql_str)
        self.sparql.setReturnFormat(JSON)
        rets = self.sparql.query().convert()
        return rets["results"]["bindings"]


    def query_relatedDepart(self, disease_name):
        sparql_tem = """
            SELECT ?object_name
              WHERE {
                ?subject <http://wowjoy.cn/medbase/relation/related_depart> ?object .
                ?subject <http://wowjoy.cn/medbase/disease/name> "%s" .
                ?object <http://wowjoy.cn/medbase/depart/name> ?object_name .
              }"""
        sparql_str = sparql_tem % disease_name
        self.sparql.setQuery(sparql_str)
        self.sparql.setReturnFormat(JSON)
        rets = self.sparql.query().convert()
        return rets["results"]["bindings"]


    def query_relatedExam(self, disease_name):
        sparql_tem = """
            SELECT ?object_name
              WHERE {
                ?subject <http://wowjoy.cn/medbase/relation/related_exam> ?object .
                ?subject <http://wowjoy.cn/medbase/disease/name> "%s" .
                ?object <http://wowjoy.cn/medbase/exam/name> ?object_name .
              }"""
        sparql_str = sparql_tem % disease_name
        self.sparql.setQuery(sparql_str)
        self.sparql.setReturnFormat(JSON)
        rets = self.sparql.query().convert()
        return rets["results"]["bindings"]


    def query_relatedDrug(self, disease_name):
        sparql_tem = """
            SELECT ?object_name
              WHERE {
                ?subject <http://wowjoy.cn/medbase/relation/related_drug> ?object .
                ?subject <http://wowjoy.cn/medbase/disease/name> "%s" .
                ?object <http://wowjoy.cn/medbase/drug/name> ?object_name .
              }"""
        sparql_str = sparql_tem % disease_name
        self.sparql.setQuery(sparql_str)
        self.sparql.setReturnFormat(JSON)
        rets = self.sparql.query().convert()
        return rets["results"]["bindings"]


    def query_relatedOperation(self, disease_name):
        sparql_tem = """
            SELECT ?object_name
              WHERE {
                ?subject <http://wowjoy.cn/medbase/relation/related_operation> ?object .
                ?subject <http://wowjoy.cn/medbase/disease/name> "%s" .
                ?object <http://wowjoy.cn/medbase/operation/name> ?object_name .
              }"""
        sparql_str = sparql_tem % disease_name
        self.sparql.setQuery(sparql_str)
        self.sparql.setReturnFormat(JSON)
        rets = self.sparql.query().convert()
        return rets["results"]["bindings"]


if __name__ == "__main__":
    import pprint
    endpoint = "http://192.168.10.132:3030/medbase/query"
    kb_helper = KBHelper(endpoint=endpoint)
    # 相关症状
    pprint.pprint(kb_helper.query_relatedSymptom("前列腺炎"))
    # 相关科室
    pprint.pprint(kb_helper.query_relatedDepart("前列腺炎"))
    # 相关检查
    pprint.pprint(kb_helper.query_relatedExam("前列腺炎"))
    # 相关药品
    pprint.pprint(kb_helper.query_relatedDrug("前列腺炎"))
    # 相关手术
    pprint.pprint(kb_helper.query_relatedOperation("前列腺炎"))
