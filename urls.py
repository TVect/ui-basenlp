# -*- coding: utf-8 -*-

'''
Created on 2018年07月10日

@author: chin340823@163.com
'''

from web.service.main_handler import MainHandler
from web.service.health_handler import HealthHandler
from web.service.chatbot_handler import ChatbotHandler
from web.service.weixin_handler import WeixinHandler
from web.service.wx_mp_handler import WxMpHandler

url_patterns=[(r"/", MainHandler), 
              (r"/health", HealthHandler), 
              (r"/chat", ChatbotHandler),
              (r"/wx", WeixinHandler),
              (r"/wx_mp", WxMpHandler),
#               (r'/aidvoice', VoiceHandler),
             ]

