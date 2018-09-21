
def action_drug2disease(word_objects):
    ''' 寻找 药品 关联的 疾病 '''
    drugs = [word_obj.token for word_obj in word_objects if word_obj.pos == 'nz-entity_drug']
    query_str = "MATCH p=(di)-[r:RELATED_DRUG]->(dr) WHERE dr.name='{name}' RETURN di.name AS name".\
                format(name=drugs[0])
    return query_str


def action_disease2drug(word_objects):
    ''' 寻找 疾病 关联的 药品 '''
    drugs = [word_obj.token for word_obj in word_objects if word_obj.pos == 'nz-entity_disease']
    query_str = "MATCH p=(di)-[r:RELATED_DRUG]->(dr) WHERE di.name='{name}' RETURN dr.name AS name".\
                format(name=drugs[0])
    return query_str
