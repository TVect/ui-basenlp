## nlu pipeline

conf 文件夹下列举并尝试了下面几种的 nlu pipeline: 

### nlu_mitie_pipeline

- 依赖:

mitie 中文模型, 参考自 [MITIE_Chinese_Wikipedia_corpus](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus)		

### nlu_spacy_pipeline

- 依赖: 

spacy 的中文模型, 参考自 [Chinese_models_for_SpaCy](https://github.com/howl-anderson/Chinese_models_for_SpaCy)

### nlu_tfembed_pipeline

当前的 rasa_nlu.classifier.embedding_intent_classifier.EmbeddingIntentClassifier 似乎还没有很好的处理 multiple intents 的问题.

代码中会根据 intent_split_symbol 将 intent 拆分为子意图, 进一步根据 one-hot 表示得到 intent 的表示. 但在整个预测过程当中还是只针对所有出现过的意图 (组合的意图) 来计算相似度, 给出 intent_ranking.

比如说, 如果训练样本中只出现了意图 intentA_intentB, 没有单独出现 intentA 和 intentB. 那么, 在预测过程当中, 只会计算当前 utterence 和 intentA_intentB 的相似度, 而不会单独计算 utterence 与 intentA 和 intentB 的相似度. 从而最后输出的 intent_rank 中不会有 intentA 或 intentB 的排名. 这可能并不是我想要的 multiple intents.
