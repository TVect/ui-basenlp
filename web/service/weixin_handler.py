'''
Created on 2018-07-15

@author: chin340823@163.com
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

import json
import hashlib
import tornado.web

import app.wx.receive
import app.wx.reply

from app.chatbot.ChatbotManager import ChatbotManager

class WeixinHandler(tornado.web.RequestHandler):

    chatbot = ChatbotManager()

    def get(self):
        '''
        @summary: 初始的token认证提交 
        '''
        try:
            signature = self.get_argument("signature")
            timestamp = self.get_argument("timestamp")
            nonce = self.get_argument("nonce")
            echostr = self.get_argument("echostr")
            token = "VectorMachine"

            items = [token.encode("utf-8"), timestamp.encode("utf-8"), nonce.encode("utf-8")]
            items.sort()
            sha1 = hashlib.sha1()
            for item in items:
                sha1.update(item)
            hashcode = sha1.hexdigest()
            # print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                self.write(echostr)
            else:
                self.write("")
        except Exception as Argument:
            self.write(str(Argument))


    def post(self):
        '''
        @summary:
        '''
        try:
            webData = self.request.body
            # print("Handle Post webdata is ", webData)
            recMsg = app.wx.receive.parse_xml(webData)
            if isinstance(recMsg, app.wx.receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                # print("user content: ", recMsg.Content)
                content = self.chatbot.response(recMsg.Content.decode("utf-8"))
                replyMsg = app.wx.reply.TextMsg(toUser, fromUser, content)
                self.write(replyMsg.send())
            else:
                print("暂且不处理")
                self.write("success")
        except Exception as Argment:
            self.write(str(Argment))


    def put(self):
        '''
        @summary:
        '''
        pass
