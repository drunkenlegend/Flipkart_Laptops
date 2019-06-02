# -*- coding: utf-8 -*-
import scrapy

import pickle





class FlipkartSpider(scrapy.Spider):
    name = 'Flipkart'
    page=2
    n=1
    x=int(input())
    list=[]

    start_urls = ['https://www.flipkart.com/search?q=laptops&page=2']

    def parse(self, response):
        allt=response.css('div._1UoZlX')

        for all in allt:
            if FlipkartSpider.n <= FlipkartSpider.x:
                print(FlipkartSpider.n)
                items={'Laptop_No.:':FlipkartSpider.n}
                items['laptop_title']=all.css('._3wU53n::text').extract()
                items['current_selling_price']=all.css('._2rQ-NK::text').extract()
                items['ratings']=all.css('.hGSR34::text').extract()
                FlipkartSpider.list.append(items)
                print(items)
                if FlipkartSpider.n == FlipkartSpider.x:
                    print('dictionaries for all laptop data is stored in a list as follows:   and the same is pickled')

                    print(FlipkartSpider.list)

                FlipkartSpider.n+=1
                pic = open('Laptop.pickle', 'wb')
                pickle.dump(FlipkartSpider.list, pic)
                pic.close()





        next='https://www.flipkart.com/search?q=laptops&page='+str(FlipkartSpider.page)
        if FlipkartSpider.n <= FlipkartSpider.x:
            print(FlipkartSpider.page)
            FlipkartSpider.page+=1
            yield response.follow(next,callback=self.parse)






