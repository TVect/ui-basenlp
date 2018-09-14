## Generated Story -7798302707235983698
* greet
    - utter_greet
* symptom_statistic
    - action_form_statistic
    - slot{"requested_slot": "disease"}
* inform_disease{"disease": "\u9ad8\u8840\u538b"}
    - slot{"disease": "\u9ad8\u8840\u538b"}
    - action_form_statistic
    - slot{"disease": "\u9ad8\u8840\u538b"}
    - slot{"requested_slot": "time"}
* inform_time{"time": "2018-04"}
    - slot{"time": "2018-04"}
    - action_form_statistic
    - export

## Generated Story 4691494301847031037
* greet
    - utter_greet
* request_weather{"city": "\u676d\u5dde"}
    - slot{"city": "\u676d\u5dde"}
    - action_weather
    - utter_ask_morehelp
* request_weather{"city": "\u676d\u5dde"}
    - slot{"city": "\u676d\u5dde"}
    - action_weather
* goodbye
    - utter_goodbye
    - export

## Generated Story -1480668120387350242
* greet
    - utter_greet
* symptom_statistic{"time": "2018-04", "disease": "\u9ad8\u8840\u538b"}
    - slot{"disease": "\u9ad8\u8840\u538b"}
    - slot{"time": "2018-04"}
    - action_form_statistic
    - utter_ask_morehelp
* request_weather{"city": "\u676d\u5dde"}
    - slot{"city": "\u676d\u5dde"}
    - action_weather
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export