import requests
import inspect
import sys

class AliWeather:
    
    def __init__(self):
        self.weather_url = 'https://jisutqybmf.market.alicloudapi.com/weather/query'
        self.method = 'GET'
        self.appcode = '397328e6ac4e4e1bbfa44afd2f37ee0d'


    def query(self, **kwargs):
        '''
        @param city: STRING,可选    城市（city,cityid,citycode三者任选其一）
        @param citycode: STRING,可选    城市天气代号（city,cityid,citycode三者任选其一）
        @param cityid: STRING,可选    城市ID（city,cityid,citycode三者任选其一）
        @param ip: STRING,可选    IP
        @param location: STRING,可选    经纬度 纬度在前,分割 如：39.983424,116.322987
        '''
        params = kwargs
        headers = {'Authorization': 'APPCODE ' + self.appcode}
        req = requests.get(self.weather_url, params, headers=headers)
        if req.ok:
            return req.json()
        return None


if __name__ == "__main__":
    weather = AliWeather()
    res = weather.query(city="杭州")
    print("city:{}, 天气: {}, 最高温度: {}, 最低温度: {}, 风向: {}, 风力: {}"\
          .format(res["result"]["city"], res["result"]["weather"], res["result"]["temphigh"], 
                  res["result"]["templow"], res["result"]["winddirect"], res["result"]["windpower"]))
    print(res)