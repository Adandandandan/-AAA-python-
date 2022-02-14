# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from mmkk.settings import IMAGES_STORE as images_store
import os


class MmkkPipeline(ImagesPipeline):
##    def process_item(self, item, spider):
##        with open('0.txt','a') as f:
##            f.write(f'{item}\n')
##            return item
    def get_media_requests(self,item,info):

        yield scrapy.Request(url = item['image_url'],meta = {'folder_name':item['folder_name'],'name':item['image_name']})

    def file_path(self,request,response = None,info =None):
        
        folder_name = request.meta['folder_name']
        folder_path = './' + folder_name
##        if not os.path.exists(fild_path):
##            os.mkdir(fild_path)
        
        
        image_path = os.path.join(folder_name,request.meta['name'])
        
        return image_path

    def item_completed(self,results,item,info):
        
        image_paths = [x['path'] for ok, x in results if ok]
        print('11111111111111111111111111111111111')
        
        if not image_paths:
            raise DropItem("Item contains no image")
        
        return item
     
