from datetime import datetime
from elasticsearch_dsl import DocType, Boolean, analyzer, Keyword, Text
from elasticsearch_dsl.connections import connections
import hashlib

class EntitySymptom(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    source_url = Text()

    class Meta:
        index = 'med_base'
    
    def save(self, ** kwargs):
        if "_id" not in self.meta:
            hl = hashlib.md5()
            hl.update(self.name.encode(encoding="utf-8"))
            self.meta['id'] = hl.hexdigest()
        return super(EntitySymptom, self).save(** kwargs)
