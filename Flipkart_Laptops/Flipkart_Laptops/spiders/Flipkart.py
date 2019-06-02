# -*- coding: utf-8 -*-
import scrapy


from ..items import FlipkartLaptopsItem

class FlipkartSpider(scrapy.Spider):
    name = 'Flipkart'
    page=2
    n=1
    x=int(input())

    start_urls = ['https://www.flipkart.com/search?q=laptops&page=2']

    def parse(self, response):
        items=FlipkartLaptopsItem()
        allt=response.css('div._1UoZlX')

        for all in allt:
            if FlipkartSpider.n <= FlipkartSpider.x:
                print(FlipkartSpider.n)
                items['laptop_title']=all.css('._3wU53n::text').extract()
                items['current_selling_price']=all.css('._2rQ-NK::text').extract()
                items['ratings']=all.css('.hGSR34::text').extract()
                print(items)
                FlipkartSpider.n+=1





        next='https://www.flipkart.com/search?q=laptops&page='+str(FlipkartSpider.page)
        if FlipkartSpider.n <= FlipkartSpider.x:
            print(FlipkartSpider.page)
            FlipkartSpider.page+=1
            yield response.follow(next,callback=self.parse)

