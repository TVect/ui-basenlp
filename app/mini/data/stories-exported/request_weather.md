## story-0001
* greet
  - utter_greet
* request_weather {"city": "����"}
  - slot {"city": "����"}
  - action_weather
  - utter_ask_morehelp
* deny
  - utter_goodbye

## story-0002
* greet
  - utter_greet
* request_weather
  - action_weather
* inform_city {"city": "����"}
  - slot {"city": "����"}
  - action_weather
* inform_city {"city": "����"}
  - slot {"city": "����"}
  - action_weather
* inform_city {"city": "�Ϻ�"}
  - slot {"city": "�Ϻ�"}
  - action_weather
