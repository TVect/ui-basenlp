import logging
import requests
import user_agent
import urllib
import hashlib
from lxml import html

def to_uuid(in_str):
    hl = hashlib.md5()
    hl.update(in_str.encode(encoding="utf-8"))
    return hl.hexdigest()


class CrawlerPart(object):

    def __init__(self):
        self.base_url = "http://jbk.39.net/bw/"
        self.load()


    def load(self):
        self.user_agent = user_agent.UserAgent()
        # self.random_proxy = random_proxy.RandomProxyMiddleware()


    def crawler_bodyparts(self):
        headers = {"User-Agent": self.user_agent.random_user_agent}
        page = requests.get(self.base_url, headers=headers)
        if page.status_code != requests.codes.ok:
            logging.info("url: %s, code: %s" % (page.url, page.status_code))
        tree = html.fromstring(page.text)
        
        # bodypart
        body_items = tree.xpath('//*[@id="cond_box1"]/dl')
        if body_items:
            for item in body_items:
                dt_name = item.xpath("dt/a")[0].text
                dt_url = urllib.parse.urljoin(page.url, item.xpath("dt/a/@href")[0].strip())
                for dd in item.xpath("dd/a"):
                    dd_name = dd.text
                    dd_url = urllib.parse.urljoin(page.url, dd.xpath('@href')[0].strip())
                    yield dt_name, dt_url, dd_name, dd_url


    def crawler_departments(self):
        headers = {"User-Agent": self.user_agent.random_user_agent}
        page = requests.get(self.base_url, headers=headers)
        if page.status_code != requests.codes.ok:
            logging.info("url: %s, code: %s" % (cur_url, page.status_code))
        tree = html.fromstring(page.text)
        
        # departments
        departs = tree.xpath('//*[@id="cond_box2"]/dl')
        if departs:
            for depart in departs:
                dt_name = depart.xpath("dt/a")[0].text
                dt_url = urllib.parse.urljoin(page.url, depart.xpath("dt/a/@href")[0].strip())
                for dd in depart.xpath("dd/a"):
                    dd_name = dd.text
                    dd_url = urllib.parse.urljoin(page.url, dd.xpath('@href')[0].strip())
                    yield dt_name, dt_url, dd_name, dd_url


def dump_parts():
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../../")
    from med_base.storage.neo4j.models import Bodypart, Department
    from conf.settings import NEO4J_URI
    from py2neo import Graph
    graph = Graph(NEO4J_URI)

    cp = CrawlerPart()
    for dt_name, dt_url, dd_name, dd_url in cp.crawler_bodyparts():
        print(dt_name, dt_url, dd_name, dd_url)
        body_dt = Bodypart()
        body_dt.name = dt_name
        body_dt.id = to_uuid(dt_url)
         
        body_dd = Bodypart()
        body_dd.name = dd_name
        body_dd.id = to_uuid(dd_url)
         
        body_dd.partof.add(body_dt)
        graph.push(body_dd)

    for dt_name, dt_url, dd_name, dd_url in cp.crawler_departments():
        print(dt_name, dt_url, dd_name, dd_url)
        depart_dt = Department()
        depart_dt.name = dt_name
        depart_dt.id = to_uuid(dt_url)
         
        depart_dd = Department()
        depart_dd.name = dd_name
        depart_dd.id = to_uuid(dd_url)
         
        depart_dd.partof.add(depart_dt)
        graph.push(depart_dd)


if __name__ == "__main__":
    dump_parts()
