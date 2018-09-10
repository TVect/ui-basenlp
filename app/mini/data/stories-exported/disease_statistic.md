## story-0001
* greet
  - utter_greet
* symptom_statistic {"time": "2018-04", "disease": "¸ßÑªÑ¹"}
  - slot {"time": "2018-03", "disease": "¸ßÑªÑ¹"}
  - action_form_statistic
  - utter_ask_morehelp
* deny
  - utter_goodbye

## story-0002
* greet
  - utter_greet
* symptom_statistic {"time": "2018-04", "disease": "¸ßÑªÑ¹"}
  - slot {"time": "2018-03", "disease": "¸ßÑªÑ¹"}
  - action_form_statistic
  - utter_ask_morehelp
* symptom_statistic {"time": "2018-04", "disease": "ÐÄÔà²¡"}
  - slot {"time": "2018-03", "disease": "ÐÄÔà²¡"}
  - action_form_statistic
  - utter_ask_morehelp
* deny
  - utter_goodbye

## story-0003
* greet
  - utter_greet
* symptom_statistic {"time": "2018-04", "disease": "¸ßÑªÑ¹"}
  - slot {"time": "2018-03", "disease": "¸ßÑªÑ¹"}
  - action_form_statistic
  - utter_ask_morehelp
* symptom_statistic {"disease": "ÐÄÔà²¡"}
  - slot {"disease": "ÐÄÔà²¡"}
  - action_ask_time
* inform_time{"time": "2018-04"}
  - slot{"time": "2018-04"}
  - action_form_statistic
  - utter_ask_morehelp
* deny
  - utter_goodbye
