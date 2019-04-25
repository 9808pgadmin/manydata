import scrapy

class datapaqu(scrapy.Spider):
    name = 'datatest'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self,response):

        data = response.css('div.quote')
        for a in data:

            text = a.css('.text::text').extract_first()
            author = a.css('.author::text').extract_first()
            tags = a.css('.tags .tag::text').extract()
            tags = ",".join(tags)

            fileName = '%s-语录.txt' %author

            with open(fileName,"a+",encoding="utf-8")as f:
                f.write(text)
                f.write('\n')
                f.write('标签:'+tags)
                f.write('\n------\n')
                f.close()
