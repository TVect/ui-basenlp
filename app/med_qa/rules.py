from refo import finditer, Predicate, Star, Any, Disjunction, Plus
import re
import copy


class Word(object):
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos


class W(Predicate):
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        return m1 and m2


class Rule(object):
    def __init__(self, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action

    def apply(self, sentence):
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            if "victim" in m:
                i, j = m.span("victim")
            self.action(sentence[i:j])


def action_test(word_objects):
    for word_obj in word_objects:
        print(word_obj.token, word_obj.pos)


entity_disease = W(pos="nz-entity_drug")

basic_rules = [Rule(condition=Star(Any(),greedy=True) + entity_disease + Star(Any(),greedy=False), action=action_test)]
