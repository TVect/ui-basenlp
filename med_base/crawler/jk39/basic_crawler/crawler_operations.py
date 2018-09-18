import logging
import requests
import user_agent
from lxml import html

class CrawlerOperations(object):
    
    '''
    @summary: 做法有问题，base_url 每一页的数据是一样的
    '''
    def __init__(self):
        self.base_url = "http://jbk.39.net/shoushu/search_p{}/"
        self.load()


    def load(self):
        self.user_agent = user_agent.UserAgent()
        # self.random_proxy = random_proxy.RandomProxyMiddleware()


    def process(self):
        headers = {"User-Agent": self.user_agent.random_user_agent}

        page_id = 0
        while True:
            logging.info("====== page_id = {}".format(page_id))
            page = requests.get(self.base_url.format(page_id), headers=headers)
            if page.status_code != requests.codes.ok:
                logging.warning("url: %s, code: %s" % (page.url, page.status_code))
                continue
            tree = html.fromstring(page.text)

            body_items = tree.xpath('//*[@id="res_tab_1"]/div/dl/dt/h3/a')
            if body_items:
                for item in body_items:
                    url = item.xpath('@href')[0]
                    name = item.xpath('@title')[0]
                    operation_item = {"name": name}

                    detail_page = requests.get(url, headers=headers)
                    if detail_page.status_code != requests.codes.ok:
                        logging.warning("url: %s, code: %s" % (detail_page.url, detail_page.status_code))
                        continue
                    operation_item["source_url"] = detail_page.url
                    detail_page.encoding = detail_page.apparent_encoding
                    detail_tree = html.fromstring(detail_page.text)

                    describe_items = detail_tree.xpath('//*[@id="intro"]/span')
                    if describe_items:
                        operation_item["describe"] = describe_items[0].text_content().strip()

                    # info_items = detail_tree.xpath('//*[@class="infolist"]/li/span')
                    info_items = detail_tree.xpath('//*[@class="info clearfix"]//*/li/span')
                    for info_item in info_items:
                        info_key = info_item.xpath("b/text()")
                        if info_key:
                            if "手术部位" in info_key[0]:
                                operation_item["related_bodypart"] = info_item.xpath("a/text()")[0].strip()
                            elif "科室" in info_key[0]:
                                operation_item["related_departs"] = info_item.xpath("a/text()")[0].strip()

                    yield operation_item
            page_id += 1


def dump_operations():
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../../")
    from med_base.storage.neo4j.models import Operation, Bodypart, Department
    from med_base.storage.es.EntityOperation import EntityOperation
    from elasticsearch_dsl.connections import connections

    from py2neo import Graph
    from conf.settings import NEO4J_URI, ES_HOST
    graph = Graph(NEO4J_URI)
    connections.create_connection(hosts=[ES_HOST])

    cp = CrawlerOperations()
    for item in cp.process():
        logging.info(item)

        entity_operation = EntityOperation(name=item["name"], describe=item["describe"], source_url=item["source_url"])
        entity_operation.save()

        operation = Operation()
        operation.name = item["name"]
        operation.id = str(entity_operation._id)
        
        if item.get("related_bodypart", None):
            operation.related_bodypart.add(Bodypart.match(graph, item["related_bodypart"]).first())
        if item.get("related_departs", None):
            operation.related_departs.add(Department.match(graph, item["related_departs"]).first())

        graph.push(operation)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dump_operations()
