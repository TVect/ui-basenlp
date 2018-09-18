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
    related_depart = RelatedTo("Department")


class Examination(GraphObject):

    __primarykey__ = "name"

    name = Property()
    id = Property()

    related_bodypart = RelatedTo('Bodypart')


class Disease(GraphObject):
    
    __primarykey__ = "name"
    
    name = Property()
    id = Property()

    related_symptom = RelatedTo('Symptom')
    related_depart = RelatedTo('Department')
    related_bodypart = RelatedTo('Bodypart')
    related_exam = RelatedTo('Examination')
    related_drug = RelatedTo('Drug')
    related_operation = RelatedTo('Operation')
    related_disease = Related('Disease')
