
# train_nlu

## components
Component | name | provide_context | requires | provides
--------- | ---- | --------------- | -------- | --------
SpacyNLP | nlp_spacy | {"spacy_nlp": self.nlp=spacy.load("en")} | [] | ["spacy_doc", "spacy_nlp"]
SpacyTokenizer | tokenizer_spacy | None | [] | ['tokens']
SpacyFeaturizer | intent_featurizer_spacy | None | ["spacy_doc"] | ["text_features"]
SklearnIntentClassifier | intent_classifier_sklearn | None | ['text_features'] | ['intent', 'intent_ranking']
CRFEntityExtractor | ner_crf | None | ['spacy_doc', 'tokens'] | ['entities']
EntitySynonymMapper | ner_synonyms | None | [] | ['entities']


## 训练流程

### 训练数据
training_data.training_example: List<Message>

### train基本流程:

```
for each component in pipeline:
    updates = component.train(working_data, self.config, **context)
```

- SpacyNLP

    在 Message.data 中 添加 {"spacy_doc": spacy.tokens.doc.Doc}

- SpacyTokenizer

    在 Message.data 中 添加 {"tokens": List<rasa_nlu.tokenizers.Token> 记录了每个token的起始位置}

- SpacyFeaturizer

    在所有 intent_example (Message.data中有intent项) 的 Message.data 中 添加 {"text_features": message.get("spacy_doc").vector}

- SklearnIntentClassifier

    训练分类器: 训练数据为 Message.data["text_features"], 标签为 Message.data["intent"]
    
    分类器为 sklearn.SVC, 其中使用了 GridSearch 做超参数选择, 并且保证每个folder样本数>=5
    
    此步骤 未在 Message.data 中添加 'intent', 'intent_ranking'

- CRFEntityExtractor

    过滤出本次的 entity_examples
    
    整理后训练语料格式形如: 
        
        [[('moderately', 'RB', 'U-price', None), 
        
        ('priced', 'VBN', 'O', None), 
        
        ('restaurant', 'NN', 'O', None), 
        
        ('that', 'WDT', 'O', None), 
        
        ('serves', 'VBZ', 'O', None), 
        
        ('creative', 'JJ', 'U-cuisine', None), 
        
        ('food', 'NN', 'O', None)]]
    
    特征化之后的训练数据如下:
    
        [{'BOS': True, '0:bias': 'bias', '0:low': 'moderately', '0:word3': 'ely', '0:word2': 'ly', '0:upper': False, '0:title': False, '0:digit': False, '0:pos': 'RB', '0:pos2': 'RB', '0:pattern': 'N/A', '1:low': 'priced', '1:title': False, '1:upper': False, '1:pos': 'VBN', '1:pos2': 'VB'}, 
        
        {'-1:low': 'moderately', '-1:title': False, '-1:upper': False, '-1:pos': 'RB', '-1:pos2': 'RB', '0:bias': 'bias', '0:low': 'priced', '0:word3': 'ced', '0:word2': 'ed', '0:upper': False, '0:title': False, '0:digit': False, '0:pos': 'VBN', '0:pos2': 'VB', '0:pattern': 'N/A', '1:low': 'restaurant', '1:title': False, '1:upper': False, '1:pos': 'NN', '1:pos2': 'NN'}, 
        
        ...]
    
    特征化之后的训练数据label如下：
    
        ['U-price', 'O', 'O', 'O', 'O', 'U-cuisine', 'O']
    
    使用 sklearn_crfsuite 训练序列标注模型
    
- EntitySynonymMapper

    构造了一个 synonyms 的字典: { original --> replacement }
    
        {'moderately': 'moderate', 'eight': '8', 'six': '6', 'moderate': 'mid', 
        'two': '2', 'cheap': 'lo', 'four': '4', 'expensive': 'hi'}