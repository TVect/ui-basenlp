# -*- coding: utf-8 -*-
import scrapy
import re
from w3lib.html import remove_tags
from jk39.items import DiseaseItem, ExamItem, DrugItem, OperationItem


class DiseaseSpider(scrapy.Spider):
    name = 'disease'
    allowed_domains = ['jbk.39.net', 'ypk.39.net']
    start_urls = ['http://jbk.39.net/bw_t1/']


    def parse(self, response):
        body_items = response.xpath('//*[@id="res_tab_2"]/div/dl/dt/h3/a')
        if body_items:
            for body_item in body_items:
                url = body_item.xpath('@href').extract_first() + "jbzs"
                name = body_item.xpath('@title').extract_first()

                yield scrapy.Request(url, 
                                     callback=self.parse_jbzs, 
                                     meta={"disease_info": {"name": name}})
        
        page_item = response.xpath('//div[@class="site-pages"]/a[contains(text(), "下页")]/@href').extract_first()
        if page_item:
            next_page_url = response.urljoin(page_item)
            yield scrapy.Request(next_page_url, callback=self.parse)


    def parse_jbzs(self, response):
        describe = response.xpath('//dl[@class="intro"]/dd/text()').extract_first().strip()
        meta_dict = {"describe": describe, "source_url": response.url}
        meta_dict.update(response.meta["disease_info"])

        info_items = response.xpath('//dl[@class="info"]/dd')
        for info_item in info_items:
            key = info_item.xpath('i/text()').extract_first()
            if not key:
                continue
            if "传染性" in key:
                meta_dict["is_infect"] = info_item.xpath('text()').extract_first()
            elif "人群" in key:
                meta_dict["highrisk_group"] = info_item.xpath('text()').extract_first()
            elif "治疗周期" in key:
                meta_dict["treatment_cycle"] = info_item.xpath('text()').extract_first()
            elif "治疗费用" in key:
                meta_dict["treatment_cost"] = info_item.xpath('text()').extract_first()
            elif "相关症状" in key:
                # meta_dict["related_symptom"] = info_item.xpath('a/@title').extract()
                meta_dict["related_symptom"] = [response.urljoin(url_path) 
                                                for url_path in info_item.xpath('a[not(contains(text(), "详细"))]/@href').extract()]
            elif "并发疾病" in key:
                # meta_dict["related_disease"] = info_item.xpath('a/@title').extract()
                meta_dict["related_disease"] = [response.urljoin(url_path) 
                                                for url_path in info_item.xpath('a[not(contains(text(), "详细"))]/@href').extract()]
            elif "部位" in key:
                # meta_dict["related_bodypart"] = info_item.xpath('a/text()').extract()
                meta_dict["related_bodypart"] = [response.urljoin(url_path) 
                                                for url_path in info_item.xpath('a[not(contains(text(), "详细"))]/@href').extract()]
            elif "科室" in key:
                # meta_dict["related_depart"] = info_item.xpath('a/text()').extract()
                meta_dict["related_depart"] = [response.urljoin(url_path) 
                                                for url_path in info_item.xpath('a[not(contains(text(), "详细"))]/@href').extract()]
            elif "检查" in key:
                # meta_dict["related_exam"] = info_item.xpath('a/@title').extract()
                meta_dict["related_exam"] = [response.urljoin(url_path) 
                                             for url_path in info_item.xpath('a[not(contains(text(), "详细"))]/@href').extract()]
                for exam_url in meta_dict['related_exam']:
                    yield scrapy.Request(exam_url, 
                                         callback=self.parse_exams, 
                                         meta={"disease_name": meta_dict["name"]})
            elif "药品" in key:
                # meta_dict["related_drug"] = info_item.xpath('a/@title').extract()
                meta_dict["related_drug"] = [response.urljoin(url_path) 
                                             for url_path in info_item.xpath('a[not(contains(text(), "详细"))]/@href').extract()]
                for drug_url in meta_dict["related_drug"]:
                    if "ypk.39.net" in drug_url:
                        yield scrapy.Request(drug_url, 
                                             callback=self.parse_drugs, 
                                             meta={"disease_name": meta_dict["name"]})                
            elif "手术" in key:
                # meta_dict["related_operation"] = info_item.xpath('a/@title').extract()
                meta_dict["related_operation"] = [response.urljoin(url_path) 
                                                  for url_path in info_item.xpath('a[not(contains(text(), "详细"))]/@href').extract()]
                for operation_url in meta_dict["related_operation"]:
                    yield scrapy.Request(operation_url, 
                                         callback=self.parse_operations, 
                                         meta={"disease_name": meta_dict["name"]})

        yield DiseaseItem(**meta_dict)


    def parse_exams(self, response):
        describe = response.xpath('//*[@id="intro"]/span/p').get()
        if describe:
            describe = remove_tags(describe)
        name = response.xpath('/html/body/section/div[2]/article/div[1]/div[1]/h1/b/text()').extract_first()
        source_url = response.url
        meta_dict = {"describe": describe, "name": name, "source_url": source_url}

        info_items = response.xpath('//*[@class="info clearfix"]//*/li/span')
        for info_item in info_items:
            info_key = info_item.xpath("b/text()").extract_first()
            if info_key:
                if "检查部位" in info_key:
                    # meta_dict["related_bodypart"] = info_item.xpath("a/text()").extract()
                    meta_dict["related_bodypart"] = [response.urljoin(url_path) 
                                                     for url_path in info_item.xpath("a/@href").extract()]
                    break
        
        meta_dict["related_disease"] = [response.urljoin(url_path) for url_path in 
                                        response.xpath('//*[@id="refdisease"]/div[@class="listBox"]/div/div/ul/li/a/@href').extract()]

        yield ExamItem(**meta_dict)

    
    def parse_drugs(self, response):
        name = response.xpath('//div[@class="yps_top"]/div[1]/h1/a/text()').extract_first()
        meta_dict = {"source_url": response.url, "name": name}
    
#         for info_item in response.xpath('//div[@class="ps"]/p'):
#             key = info_item.xpath('strong/text()').extract_first()
#             if "分" in key:
#                 meta_dict["composition"] = remove_tags(re.sub(r'<strong>[\s\S]+</strong>', "", info_item.get())).strip()
#                 break
#             elif ("适应症" in key) or ("主治" in key):
#                 meta_dict["indication"] = remove_tags(info_item.get()).strip()
#             elif "用法" in key:
#                 meta_dict["usage"] = remove_tags(info_item.get()).strip()

        yield DrugItem(**meta_dict)

    
    def parse_operations(self, response):
        describe = response.xpath('//*[@id="intro"]/span/p').get()
        if describe:
            describe = remove_tags(describe)
        name = response.xpath('/html/body/section/div[2]/article/div[1]/div[1]/h1/b/text()').extract_first()
        meta_dict = {"source_url": response.url, "describe": describe, "name": name}

        info_items = response.xpath('//*[@class="info clearfix"]//*/li/span')
        for info_item in info_items:
            info_key = info_item.xpath("b/text()").extract_first()
            if info_key:
                if "手术部位" in info_key:
                    meta_dict["related_bodypart"] = [response.urljoin(url_path) 
                                                     for url_path in info_item.xpath("a/@href").extract()]
                elif "科室" in info_key:
                    meta_dict["related_depart"] = [response.urljoin(url_path) 
                                                   for url_path in info_item.xpath("a/@href").extract()]

        yield OperationItem(**meta_dict)
