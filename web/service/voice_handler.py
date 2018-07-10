# -*- coding: utf-8 -*-

'''
Created on 2017年9月27日

@author: xiaoliang.qian@wowjoy.cn
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../")

import time
import pickle
import json
import logging
import subprocess

import tornado.web
from app.aidvoice.IflyVoiceDictation import IflyVoiceDictation

voice_dictation = IflyVoiceDictation()    

class VoiceHandler(tornado.web.RequestHandler):

    def get(self):
        self.finish({"msg": "voice handler"})


    def post(self):
        ret = {'status': True}
        upload_path = os.path.join(os.path.dirname(__file__), 'files')
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        file_metas = self.request.files.get('voicefile', None)

        if not file_metas:
            ret['status'] = False
        else:
            for meta in file_metas:
                filename = meta['filename']
                file_path = os.path.join(upload_path, filename.split(".")[0]+".silk")

                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
                flag, msg = voice_dictation.process_silk(file_path)
                logging.info("msg: %s, time: %s" % (str(msg), str(int(time.time()))))

                # TODO 文件删除
                cmd = "rm -rf %s %s" % (file_path, file_path.split(".")[0]+".pcm")
                subprocess.getstatusoutput(cmd)
                
                if flag:
                    ret['status'] = flag
                    if msg["data"] and ("result" in msg["data"]):
                        ret['result'] = msg["data"]["result"]
                    else:
                        ret['status'] = False
                        ret['result'] = str(msg.get("desc", "Unknown Error"))
                else:
                    ret['status'] = flag
                    ret['result'] = str(msg)
        
        self.finish(ret)

