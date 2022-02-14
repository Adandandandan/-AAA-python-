import scrapy
from jiandan.items import JiandanItem


class JianSpider(scrapy.Spider):
    name = 'jian'
    allowed_domains = []
    start_urls = ['http://i.jandan.net/girl/MjAyMTA4MTgtOTI=#comments']

    def parse(self, response):

        item = JiandanItem()
        item['image_urls'] = response.xpath('//*/div[1]/p/img/@src').extract()
        
##        for image in images:
##            
##            item['image_urls'] = image.xpath('//@src').extract()
            
        yield item

        new_url = response.xpath('//*[@id="comments"]/p[2]/a[@title ="Older Comments"]/@href').extract_first()
        if new_url:
            yield response.follow(url = new_url,callback = self.parse)

    







    

      
