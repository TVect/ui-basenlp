from datetime import datetime
from elasticsearch_dsl import DocType, Boolean, analyzer, Keyword, Text
from elasticsearch_dsl.connections import connections

class EntityDepartment(DocType):
    name = Keyword()
    source_url = Text()

    class Meta:
        index = 'med_base'
