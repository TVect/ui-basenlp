## TrackerWithCachedStates(DialogueStateTracker)

_state 是一个 deque, 其中记录了每一轮的会话状态。具体包含的元素如下：

```
 domain.get_parsing_states(tracker)
      lastest_message 中提到的 entity, 表示为 ('entity_disease', 1.0)
      tracker 中已经记录的 slot 信息, 表示为 ('slot_disease_0', 1.0)
      lastest_message 的 intent, 表示为 ('intent_symptom_statistic', 1.0)
  domain.get_prev_action_states(tracker)
      tracker 中前一个 action_name, 表示为 ('prev_action_listen', 1.0)
```

问题:

这种 dst 做法中是记录了当前 utterence 的 intent. 只用当前 dst 表示做预测可能会有问题。
    
比如:
    
```
user: 我要看杭州今天的天气  // request_weather {"time": 今天, "city": "杭州"}
agent: api("杭州", "今天")
user: 我要再看下武汉的 // inform_city {"city": "武汉"}
agent: ??????
```

上面的例子中第二句 user utterence, 按照单句, 不结合上下文做 nlu, 应该会识别出意图为 inform_time, 而不是 request_weather. 这种不结合上下文做nlu的做法, 差不多也是 rasa_nlu 部分常见的做法. 

这种情况下直接用 当前 dst 表示做 policy 预测, 基本上很难对第二个 user_utterence 做出正确的回应 (api("武汉", "今天")).

所以, rasa_core 的一些官方案例中都是使用 KerasPolicy + MaxHistoryTrackerFeaturizer, 采用 LSTM 网络, 整合前面几轮的 dst 信息来做预测的。
