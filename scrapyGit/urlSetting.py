# 爬取域名
DOMAIN = 'github.com'

# 爬虫名
""" URL爬虫模块名，不可变 """
SPIDER_NAME = 'GitSpider'

GROUP_ID = '33'

MODULE = '999'

# 文章列表页起始爬取URL
START_LIST_URL = ''

# 文章列表循环规则
LIST_URL_RULER_PREFIX = r'https://github.com/search?l=Java&q=stars%3A<'
LIST_URL_RULER_SUFFIX = r'&type=Repositories'
LIST_URL_RULER_LOOP = 50

# 文章URL爬取规则XPATH
NODE_XPATH = r'//a[@class="muted-link"]'