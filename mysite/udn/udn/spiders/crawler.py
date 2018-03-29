from datetime import datetime, timedelta
from scrapy.spider import CrawlSpider
from scrapy.http import FormRequest
from scrapy.http import Request
from udn.items import UdnItem
import re
import requests

class UdnSpider(CrawlSpider):
    name='udn'

    def start_requests(self):
        url='https://nba.udn.com/nba/cate/6754/-1/newest/1'
        yield Request(url,callback=self.parse)



    def parse(self, response):
        urls=response.css('div#mainbar div.box_body dl dt a::attr(href)').extract()
        for url in urls[2:]:
            url='https://nba.udn.com'+url
            yield Request(url, callback=self.parse_page)


    def parse_page(self,response):
        content=response.css('div#story_body_content span p ::text').extract()
        str=''
        content=str.join(content[4:])
        pre_content=content[:20]+'...'
        title=response.css('h1.story_art_title ::text').extract_first()
        post_time=response.css('div.shareBar__info--author span ::text').extract_first()
        author=response.css('div.shareBar__info--author ::text').extract()[1]
        res=requests.get(response.url)
        img=re.findall('\"thumbnailUrl\": \"(.*)\",',res.text)
        img=img[0]

        print(pre_content)
        item=UdnItem()
        item['url']=response.url
        item['title']=title
        item['content']=content
        item['post_time']=post_time
        item['author']=author
        item['img_url']=img
        item['pre_content']=pre_content
        yield item











