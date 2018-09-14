from datetime import datetime
from elasticsearch_dsl import DocType, Boolean, analyzer, Keyword, Text
from elasticsearch_dsl.connections import connections

class EntityExam(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    source_url = Text()

    class Meta:
        index = 'med_base'
    
    # bodypart
    # department
    # symptoms
    # examination
    # medicine
