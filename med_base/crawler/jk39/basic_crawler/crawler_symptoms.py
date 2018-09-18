import logging
import requests
import user_agent
from lxml import html

class CrawlerSymptoms(object):

    def __init__(self):
        self.base_url = "http://jbk.39.net/bw_t2_p{}/"
        self.load()


    def load(self):
        self.user_agent = user_agent.UserAgent()
        # self.random_proxy = random_proxy.RandomProxyMiddleware()


    def process(self):
        headers = {"User-Agent": self.user_agent.random_user_agent}

        page_id = 194
        while True:
            logging.info("====== page_id = {}".format(page_id))
            page = requests.get(self.base_url.format(page_id), headers=headers)
            if page.status_code != requests.codes.ok:
                logging.warning("url: %s, code: %s" % (page.url, page.status_code))
                continue
            tree = html.fromstring(page.text)

            body_items = tree.xpath('//*[@id="res_subtab_1"]/div/dl/dt/h3/a')
            if body_items:
                for item in body_items:
                    url = item.xpath('@href')[0]
                    name = item.xpath('@title')[0]
                    
                    detail_page = requests.get(url, headers=headers)
                    if detail_page.status_code != requests.codes.ok:
                        logging.warning("url: %s, code: %s" % (detail_page.url, detail_page.status_code))
                        continue
                    detail_page.encoding = detail_page.apparent_encoding
                    detail_tree = html.fromstring(detail_page.text)
                    describe_items = detail_tree.xpath('//*[@id="intro"]/p')
                    if describe_items:
                        describe = describe_items[0].text
                    yield name, describe, detail_page.url
            page_id += 1


def dump_symptoms():
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../../")
    from med_base.storage.neo4j.models import Symptom
    from med_base.storage.es.models import EntitySymptom
    from elasticsearch_dsl.connections import connections

    from py2neo import Graph
    from conf.settings import NEO4J_URI, ES_HOST
    graph = Graph(NEO4J_URI)
    connections.create_connection(hosts=[ES_HOST])

    cp = CrawlerSymptoms()
    for name, describe, source_url in cp.process():
        logging.debug("name={}, describe={}".format(name, describe))
        entity_symptom = EntitySymptom(name=name, describe=describe, source_url=source_url)
        entity_symptom.save()

        symptom_node = Symptom.match(graph).where(name=name).first()
        if symptom_node:
            pass
        else:
            symptom = Symptom()
            symptom.name = name
            symptom.id = str(entity_symptom._id)
            graph.push(symptom)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dump_symptoms()
