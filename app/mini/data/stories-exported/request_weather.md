## story-0001
* greet
  - utter_greet
* request_weather {"city": "杭州"}
  - slot {"city": "杭州"}
  - action_weather
  - utter_ask_morehelp
* deny
  - utter_goodbye

## story-0002
* greet
  - utter_greet
* request_weather
  - action_weather
* inform_city {"city": "杭州"}
  - slot {"city": "杭州"}
  - action_weather
* inform_city {"city": "苏州"}
  - slot {"city": "苏州"}
  - action_weather
* inform_city {"city": "上海"}
  - slot {"city": "上海"}
  - action_weather
