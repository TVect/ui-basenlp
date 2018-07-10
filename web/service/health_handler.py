# -*- coding: utf-8 -*-

'''
Created on 2018年02月28日

@author: xiaoliang.qian@wowjoy.cn
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

import tornado.web


class HealthHandler(tornado.web.RequestHandler):
    '''
    @summary: health check
    '''
    def get(self):
        '''
        @summary: health check
        @return: {"status": "UP"}
        '''
        self.finish({"status": "UP"})


