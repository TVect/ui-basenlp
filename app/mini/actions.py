import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

from rasa_core.actions import Action
from rasa_core.actions.forms import FormAction, EntityFormField
import datetime
from utils.weather import AliWeather

ali_weather = AliWeather()

class ActionStatistic(Action):

    def name(self):
        return 'action_statistic'

    def run(self, dispatcher, tracker, domain):
        disease = tracker.get_slot("disease")
        if disease is None:
            dispatcher.utter_message("Please input a disease")
            return []

        start_time = tracker.get_slot("start_time")
        end_time = tracker.get_slot("end_time")
        if (start_time is None) or (end_time is None):
            dispatcher.utter_message("Please input a time that you want to see ")
            return []
        dispatcher.utter_message("wait a minute ......")
        dispatcher.utter_message("disease: {}".format(disease))
        return []


class ActionWeather(Action):
    
    def name(self):
        return "action_weather"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("city")
        if city is None:
            dispatcher.utter_message("Please input a city")
            return []

        weather_info = ali_weather.query(city=city)
        dispatcher.utter_message("city:{}, 天气: {}, 最高温度: {}, 最低温度: {}, 风向: {}, 风力: {}"\
                                 .format(weather_info["result"]["city"], weather_info["result"]["weather"], 
                                         weather_info["result"]["temphigh"], weather_info["result"]["templow"], 
                                         weather_info["result"]["winddirect"], weather_info["result"]["windpower"]))
        return []


class StatisticFormAction(FormAction):
    
    RANDOMIZE = False
    
    @staticmethod
    def required_fields():
        return [
            EntityFormField("disease", "disease"),
            EntityFormField("time", "time"),
        ]


    def name(self):
        return 'action_form_statistic'


    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message("...... 疾病统计信息完成 ......")
        return []
