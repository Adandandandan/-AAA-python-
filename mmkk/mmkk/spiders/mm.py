import scrapy
from mmkk.items import MmkkItem

class MmSpider(scrapy.Spider):
    name = 'mm'
    allowed_domains = ['www.mmkk.me']
    start_urls = ['https://www.mmkk.me/category/xinggan/']

    def parse(self, response):
        
##        fild_name = response.xpath('//*[@id="masonry"]/div/div/a/div/text()').extract()
        ##获取一级页面
        html_urls =response.xpath('//*/div/div/a[@class="item-link"]/@href').extract()
        for html_url in html_urls:
            print(html_url)
            yield scrapy.Request(url = html_url,callback = self.parse0)

        new_url = response.xpath('/html/body/div[1]/ol/li[@class = "next"]/a/@href').extract_first()
        if new_url:
            yield response.follow(url = new_url,callback = self.parse)


    def parse0(self,response):
        item = MmkkItem()
##        mulu_name = response.xpath('//*/head/meta[7]/@content').extract_first()

        
##        image_urls = response.xpath('//*[@id="masonry"]/div/img/@data-original').extract()
##        name = response.xpath('//*[@id="masonry"]/div/img/@alt').extract()
        item['folder_name'] = response.xpath('/html/head/meta[7]/@content').extract_first()
        urls = response.xpath('//*/div/img').extract()
        for url in urls:
            image_url = url.split('data-original="')[-1].split('"',1)[0]
            name = url.split('alt="')[-1].split('"',1)[0]
            item['image_url'] = image_url
            item['image_name'] = name + '.jpg'
            yield item






##        for image_url in image_urls:
##            item['image_url'] = image_url
##            item['mulu'] = mulu_name + '.jpg'
##            yield item

        
        
