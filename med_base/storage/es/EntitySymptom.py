from datetime import datetime
from elasticsearch_dsl import DocType, Boolean, analyzer, Keyword, Text
from elasticsearch_dsl.connections import connections

class EntitySymptom(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    alias = Keyword()
    source_url = Text()

    class Meta:
        index = 'med_base'
    
    # bodypart
    # examination
