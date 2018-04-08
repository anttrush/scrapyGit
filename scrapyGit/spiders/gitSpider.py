import random
from scrapy import Spider
from scrapyGit.items import GitRepItem
from scrapy.selector import Selector
from scrapyGit import urlSetting

class GitSpider(Spider):

    name = urlSetting.SPIDER_NAME
    allowed_domains = urlSetting.DOMAIN
    url_list = []
    loop = urlSetting.LIST_URL_RULER_LOOP
    for i in range(loop):
        starNum = random.randint(500,1000)
        print(starNum)
        url = urlSetting.LIST_URL_RULER_PREFIX + str(starNum) + urlSetting.LIST_URL_RULER_SUFFIX
        url_list.append(url)
        start_urls = url_list

    def parse(self, response):
        item = GitRepItem()
        sel = Selector(response)
        print("get string and score: ")
        node = sel.xpath(urlSetting.NODE_XPATH)[0]
        [author, name] = node.xpath('@href').extract()[0].split('/')[1:3]
        star = node.xpath('text()')[1].extract().strip()
        item["author"] = author
        item["name"] = name
        item["score"] = star
        print(item["author"], item["name"], item["score"])
        yield item

