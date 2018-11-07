from SPARQLWrapper import SPARQLWrapper, JSON


class KBHelper:
    
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.sparql = SPARQLWrapper(self.endpoint)


    def query_relatedSymptom(self, disease_name):
        sparql_tem = """
            SELECT ?symptom_name 
              WHERE {
                ?subject <http://wowjoy.cn/medbase/relation/related_symptom> ?object .
                ?subject <http://wowjoy.cn/medbase/disease/name> "%s" .
                ?object <http://wowjoy.cn/medbase/symptom/name> ?symptom_name .
              }"""
        sparql_str = sparql_tem % disease_name
        self.sparql.setQuery(sparql_str)
        self.sparql.setReturnFormat(JSON)
        rets = self.sparql.query().convert()
        return rets["results"]["bindings"]


if __name__ == "__main__":
    endpoint = "http://192.168.10.132:3030/medbase/query"
    kb_helper = KBHelper(endpoint=endpoint)
    rets = kb_helper.query_relatedSymptom("前列腺炎")
    print(rets)
