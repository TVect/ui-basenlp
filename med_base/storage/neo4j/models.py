from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo, Related

class Symptom(GraphObject):

    __primarykey__ = "name"
    
    name = Property()
    id = Property()


class Drug(GraphObject):
    
    __primarykey__ = "name"
    
    name = Property()
    id = Property()


class Bodypart(GraphObject):

    __primarykey__ = "name"

    name = Property()
    id = Property()

    partof = RelatedTo("Bodypart")


class Department(GraphObject):

    __primarykey__ = "name"

    name = Property()
    id = Property()  

    partof = RelatedTo('Department')


class Operation(GraphObject):

    __primarykey__ = "name"

    name = Property()
    id = Property()  

    related_bodypart = RelatedTo('Bodypart')


class Examination(GraphObject):

    __primarykey__ = "name"

    name = Property()
    id = Property()

    related_bodypart = RelatedTo('Bodypart')


class Disease(GraphObject):
    
    __primarykey__ = "name"
    
    name = Property()
    id = Property()

    related_symptoms = RelatedTo('Symptom')
    related_departs = RelatedTo('Department')
    related_bodypart = RelatedTo('Bodypart')
    related_exams = RelatedTo('Examination')
    related_drugs = RelatedTo('Drug')
    related_operations = RelatedTo('Operation')
    related_diseases = Related('Disease')


if __name__ == "__main__":
    from py2neo import Graph
    graph = Graph("bolt://neo4j:123456@192.168.10.132:7687")

    di = Disease()
    di.name = "Hello-1"

    body = Bodypart()
    body.name = "test-1"
    di.related_bodypart.add(body)

    body = Bodypart()
    body.name = "test-2"
    di.related_bodypart.add(body)

    graph.push(di)
