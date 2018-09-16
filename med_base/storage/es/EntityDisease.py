from datetime import datetime
from elasticsearch_dsl import DocType, Boolean, analyzer, Keyword, Text
from elasticsearch_dsl.connections import connections

class EntityDisease(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    alias = Keyword()
    is_infect = Text()
    highrisk_group = Text()
    source_url = Text()
    treatment_cycle = Text()
    treatment_cost = Text()

    class Meta:
        index = 'med_base'
    
    # bodypart
    # department
    # symptoms
    # examination
    # medicine

if __name__ == "__main__":
    connections.create_connection(hosts=['192.168.10.132'])
    # create the mappings in elasticsearch
    EntityDisease.init()
    
    # create and save and article
    article = EntityDisease(name='心脏病', alias=["心脏病1", "心脏病2"])
    article.save()

    # Display cluster health
    print(connections.get_connection().cluster.health())