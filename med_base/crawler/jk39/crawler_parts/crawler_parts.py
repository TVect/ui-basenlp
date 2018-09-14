import logging
import requests
import user_agent
from lxml import html

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
            logging.info("url: %s, code: %s" % (cur_url, page.status_code))
        tree = html.fromstring(page.text)
        
        # bodypart
        body_items = tree.xpath('//*[@id="cond_box1"]/dl')
        if body_items:
            for item in body_items:
                dt = item.xpath("dt/a")[0].text
                for dd in item.xpath("dd/a"):
                    yield dt, dd.text


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
                dt = depart.xpath("dt/a")[0].text
                for dd in depart.xpath("dd/a"):
                    yield dt, dd.text


def dump_parts():
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../../")
    from med_base.storage.neo4j.models import Bodypart, Department

    from py2neo import Graph
    graph = Graph("bolt://neo4j:123456@192.168.10.132:7687")

    cp = CrawlerPart()
    for dt, dd in cp.crawler_bodyparts():
        print(dt, dd)
        body_dt = Bodypart()
        body_dt.name = dt
        body_dd = Bodypart()
        body_dd.name = dd
        body_dd.partof.add(body_dt)
        graph.push(body_dd)

    for dt, dd in cp.crawler_departments():
        print(dt, dd)
        depart_dt = Department()
        depart_dt.name = dt
        depart_dd = Department()
        depart_dd.name = dd
        depart_dd.partof.add(body_dt)
        graph.push(depart_dd)


if __name__ == "__main__":
    dump_parts()
