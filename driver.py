# -*- coding: utf-8 -*-

'''
Created on 2018年02月28日

@author: xiaoliang.qian@wowjoy.cn
'''

import os
import logging

import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options

from urls import url_patterns

define("port", default=10081, help="Run server on a specific port", type=int)


def make_app():
    return tornado.web.Application(handlers=url_patterns,
                                   template_path=os.path.join(os.path.dirname(__file__), "web/fronts/templates"),
                                   static_path=os.path.join(os.path.dirname(__file__), "web/fronts/static"),
                                   )


if __name__ == "__main__":
    app = make_app()
    tornado.options.parse_command_line()
    app.listen(options.port)
    logging.info("start server ......")
    tornado.ioloop.IOLoop.current().start()
