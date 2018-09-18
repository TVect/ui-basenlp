# -*- coding: utf-8 -*-

import os
import re
import random
import base64
import traceback
import requests
from lxml import etree
import logging


class RandomProxyMiddleware(object):

    def __init__(self, settings=None):
        self.proxies = {} # key: http://ip:port  value: user_pass
        self._load_proxy()


    def _load_proxy(self):
        self.download_proxy_xdaili()

    @property
    def random_proxy(self):
        return random.choice(list(self.proxies.keys()))


    def download_proxy_kuai(self):
        kuaidaili = "http://www.kuaidaili.com/free/inha/1/"
        ret_text = requests.get(kuaidaili).text
        ret_html = etree.HTML(ret_text)
        selectors = ret_html.xpath('//*[@id="list"]/table/tbody/tr')
        print("download proxy ......")
        for selector in selectors:
            _ip = selector.xpath('td[@data-title="IP"]')[0].text
            _port = selector.xpath('td[@data-title="PORT"]')[0].text
            _type = selector.xpath('td[@data-title="类型"]')[0].text
            print("%s://%s:%s" % (_type, _ip, _port))
            self.proxies["%s://%s:%s" % (_type, _ip, _port)] = None
        print(self.proxies)


    def download_proxy_xdaili(self):
        xdaili = "http://www.xdaili.cn/ipagent//freeip/getFreeIps"
        xdaili_json = requests.get(xdaili).json()
        for xdaili_item in xdaili_json["rows"]:
            self.proxies["http://%s:%s" % (xdaili_item['ip'], xdaili_item['port'])] = None
        print(self.proxies)



    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)


    def process_request(self, request, spider):
        # Don't overwrite with a random one (server-side state for IP)
        # if 'proxy' in request.meta:
        #     return
        if len(self.proxies) == 0:
            self._load_proxy()
        try:
            proxy_address = random.choice(list(self.proxies.keys()))
            proxy_user_pass = self.proxies[proxy_address]
            request.meta['proxy'] = proxy_address
            if proxy_user_pass:
                basic_auth = 'Basic ' + base64.encodestring(proxy_user_pass)
                request.headers['Proxy-Authorization'] = basic_auth
        except Exception:
            log.msg(traceback.format_exc())


    def process_exception(self, request, exception, spider):
        log.msg(exception)
        proxy_address = request.meta['proxy']
        log.msg('Removing failed proxy_address <%s>, %d proxies left' % (proxy_address, len(self.proxies)))
        try:
            del self.proxies[proxy_address]
        except Exception:
            log.msg(traceback.format_exc())


if __name__ == "__main__":
    random_proxy = RandomProxyMiddleware()
    print(random_proxy.proxies)

