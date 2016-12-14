# qiushibaike
scrapy抓取糗事百科热门，
#首先安装scrapy环境
pip install scrapy
#然后分析页面
xpath的使用，具体参考源代码，很容易学会
#运行
scrapy crawl qbspider
#注意事项
settings.py 里面得加入cookie，Host，If-None-match,否则会出现503错误。
