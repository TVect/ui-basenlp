from datetime import datetime
from elasticsearch_dsl import DocType, Boolean, analyzer, Keyword, Text
from elasticsearch_dsl.connections import connections
import hashlib


class EntityDisease(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    alias = Keyword()
    is_infect = Text(analyzer='ik_max_word')
    highrisk_group = Text(analyzer='ik_max_word')
    source_url = Text()
    treatment_cycle = Text(analyzer='ik_max_word')
    treatment_cost = Text(analyzer='ik_max_word')

    class Meta:
        index = 'med_base'

    def save(self, ** kwargs):
        if "_id" not in self.meta:
            hl = hashlib.md5()
            hl.update(self.source_url.encode(encoding="utf-8"))
            self.meta['id'] = hl.hexdigest()
        return super(EntityDisease, self).save(** kwargs)


class EntityBodypart(DocType):
    name = Keyword()
    source_url = Text()

    class Meta:
        index = 'med_base'


class EntityDepartment(DocType):
    name = Keyword()
    source_url = Text()

    class Meta:
        index = 'med_base'


class EntityDrug(DocType):
    name = Keyword()
    composition = Text(analyzer='ik_max_word')
    indication= Text(analyzer="ik_max_word")
    usage = Text(analyzer="ik_max_word")
    source_url = Text()

    class Meta:
        index = 'med_base'

    def save(self, ** kwargs):
        if "_id" not in self.meta:
            hl = hashlib.md5()
            hl.update(self.source_url.encode(encoding="utf-8"))
            self.meta['id'] = hl.hexdigest()
        return super(EntityDrug, self).save(** kwargs)



class EntityExam(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    source_url = Text()

    class Meta:
        index = 'med_base'

    def save(self, ** kwargs):
        if "_id" not in self.meta:
            hl = hashlib.md5()
            hl.update(self.source_url.encode(encoding="utf-8"))
            self.meta['id'] = hl.hexdigest()
        return super(EntityExam, self).save(** kwargs)


class EntityOperation(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    source_url = Text()

    class Meta:
        index = 'med_base'
    
    def save(self, ** kwargs):
        if "_id" not in self.meta:
            hl = hashlib.md5()
            hl.update(self.source_url.encode(encoding="utf-8"))
            self.meta['id'] = hl.hexdigest()
        return super(EntityOperation, self).save(** kwargs)


class EntitySymptom(DocType):
    name = Keyword()
    describe = Text(analyzer='ik_max_word')
    source_url = Text()

    class Meta:
        index = 'med_base'

    def save(self, ** kwargs):
        if "_id" not in self.meta:
            hl = hashlib.md5()
            hl.update(self.source_url.encode(encoding="utf-8"))
            self.meta['id'] = hl.hexdigest()
        return super(EntitySymptom, self).save(** kwargs)
