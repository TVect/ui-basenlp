## story-0001
* greet
  - utter_greet
* symptom_statistic {"time": "2018-04", "disease": "��Ѫѹ"}
  - slot {"time": "2018-03", "disease": "��Ѫѹ"}
  - action_form_statistic
  - utter_ask_morehelp
* deny
  - utter_goodbye

## story-0002
* greet
  - utter_greet
* symptom_statistic {"time": "2018-04", "disease": "��Ѫѹ"}
  - slot {"time": "2018-03", "disease": "��Ѫѹ"}
  - action_form_statistic
  - utter_ask_morehelp
* symptom_statistic {"time": "2018-04", "disease": "���ಡ"}
  - slot {"time": "2018-03", "disease": "���ಡ"}
  - action_form_statistic
  - utter_ask_morehelp
* deny
  - utter_goodbye

## story-0003
* greet
  - utter_greet
* symptom_statistic {"time": "2018-04", "disease": "��Ѫѹ"}
  - slot {"time": "2018-03", "disease": "��Ѫѹ"}
  - action_form_statistic
  - utter_ask_morehelp
* symptom_statistic {"disease": "���ಡ"}
  - slot {"disease": "���ಡ"}
  - utter_ask_time
* inform_time{"time": "2018-04"}
  - slot{"time": "2018-04"}
  - action_form_statistic
  - utter_ask_morehelp
* deny
  - utter_goodbye
