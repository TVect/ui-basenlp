from refo import finditer, Predicate, Star, Any, Disjunction, Plus
import re
import copy

import actions

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
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        if matches:
            return self.action(matches)


entity_drug = W(pos="nz-entity_drug")
entity_disease = W(pos="nz-entity_disease")
keyword_disease = (W(token="疾病") | W(token="病"))
keyword_drug = (W(token="药") | W(token="药品") | W(token="药物"))


basic_rules = [Rule(condition=Star(Any(),greedy=False) + keyword_disease + Star(Any(),greedy=True) + 
                            entity_drug + Star(Any(),greedy=False), 
                    action=actions.action_drug2disease), # 寻找药品对应的疾病
               Rule(condition=Star(Any(),greedy=False) + entity_drug + Star(Any(),greedy=False) + 
                            keyword_disease + Star(Any(),greedy=False), # 寻找药品对应的疾病
                    action=actions.action_drug2disease),
               Rule(condition=Star(Any(),greedy=False) + entity_disease + Star(Any(),greedy=False) + 
                            keyword_drug + Star(Any(),greedy=False),
                    action=actions.action_disease2drug),
               Rule(condition=Star(Any(),greedy=False) + keyword_drug + Star(Any(),greedy=False) + 
                            entity_disease + Star(Any(),greedy=False),
                    action=actions.action_disease2drug)]
