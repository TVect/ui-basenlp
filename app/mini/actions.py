import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

from rasa_core.actions import Action
from rasa_core.actions.forms import FormAction, EntityFormField
import datetime
from utils.weather import AliWeather

ali_weather = AliWeather()


class ActionWeather(Action):
    
    def name(self):
        return "action_weather"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("city")
        if city is None:
            dispatcher.utter_message("Please input a city")
            return []

        weather_info = ali_weather.query(city=city)
        if weather_info:
            dispatcher.utter_message("city:{}, 天气: {}, 最高温度: {}, 最低温度: {}, 风向: {}, 风力: {}"\
                                     .format(weather_info["result"]["city"], weather_info["result"]["weather"], 
                                             weather_info["result"]["temphigh"], weather_info["result"]["templow"], 
                                             weather_info["result"]["winddirect"], weather_info["result"]["windpower"]))
        else:
            dispatcher.utter_message("现在信号有些不稳定，稍等一下再和我说呢")

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
        return_slots = []
        slot_names = [field.slot_name for field in self.required_fields()]
        for slot in tracker.slots:
            return_slots.append(SlotSet(slot, None))
        return return_slots
