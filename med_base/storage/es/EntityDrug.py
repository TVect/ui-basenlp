from datetime import datetime
from elasticsearch_dsl import DocType, Boolean, analyzer, Keyword, Text
from elasticsearch_dsl.connections import connections

class EntityDrug(DocType):
    name = Keyword()
    composition = Text(analyzer='ik_max_word')
    indication= Text(analyzer="ik_max_word")
    usage = Text(analyzer="ik_max_word")
    source_url = Text()

    class Meta:
        index = 'med_base'
    
    # bodypart
    # examination
