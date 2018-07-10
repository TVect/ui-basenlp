# -*- coding: utf-8 -*-

'''
Created on 2018年02月28日

@author: xiaoliang.qian@wowjoy.cn
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

import tornado.web


class MainHandler(tornado.web.RequestHandler):

#     def get(self):
#         self.finish({"version" : "0.0.1", 
#                     "tagline" : " === Wowjoy EagleEyes === "})

    def get(self):
        self.render("index.html")

