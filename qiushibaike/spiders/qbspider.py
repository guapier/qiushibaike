# -*- coding: utf-8 -*-
import scrapy
from qiushibaike.items import QiushibaikeItem


class QbspiderSpider(scrapy.Spider):
    pages =100
    name = "qbspider"
    allowed_domains = ["qiushibaike.com"]
    start_urls=[]

    for page in range(1,36):
        start_urls.append('http://www.qiushibaike.com/8hr/page/'+str(page)+'?s=4938991')


    def parse(self, response):
        for item in response.xpath('//div[@id="content-left"]/div[@class="article block untagged mb15"]'):
            qiubai = QiushibaikeItem()

            icon = item.xpath('./div[@class="author clearfix"]/a[1]/img/@src').extract()
            if icon:
                icon = icon[0]
                qiubai['userIcon'] = icon
            userName = item.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            if userName:
                userName = userName[0]
                qiubai['userName'] = userName

            content = item.xpath('./a[@class="contentHerf"]/div[@class="content"]/span/descendant::text()').extract()
            if content:
                con = ''
                for str in content:
                    con += str
                qiubai['content'] = con

            like = item.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i/text()').extract()
            if like:
                like = like[0]
                qiubai['like'] = like

            comment = item.xpath('./div[@class="stats"]/span[@class="stats-comments"]/a/i/text()').extract()
            if comment:
                comment = comment[0]
                qiubai['comment'] = comment

            yield qiubai
