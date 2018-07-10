# -*- coding: utf-8 -*-

'''
Created on 2018年07月10日

@author: chin340823@163.com
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

import json
import tornado.web

from app.chatbot.ChatbotManager import ChatbotManager

class ChatbotHandler(tornado.web.RequestHandler):

    chatbot = ChatbotManager()

    def get(self):
        '''
        @summary: 对话接口
        '''
        in_str = self.get_argument("in_str", None)
        if in_str != None:
            self.finish({"flag": True, "response": self.chatbot.response(in_str)})
        else:
            self.finish({"flag": False, "response": "Error: 输入为空......"})


    def post(self):
        '''
        @summary:
        '''
        pass
    

    def put(self):
        '''
        @summary:
        '''
        pass
