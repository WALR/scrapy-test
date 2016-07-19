import scrapy
from scrapy.http import FormRequest


class UMGSpider(scrapy.Spider):
    name = 'umg'
    # start_urls = ['https://apps.umg.edu.gt/signup/']
    allowed_domains = ["https://apps.umg.edu.gt"]

    
    def start_requests(self):
        return [ FormRequest("https://apps.umg.edu.gt/signup/",
                     formdata={'username': 'wlemusr', 'password': 'W@alr6074500'},
                     callback=self.parse) ]


    def parse(self, response):

        if "logout" in response.body:
            print '->>>>>>>>>>>>> YEAHHHHHHHHHHHHHHHHHHHHHHHH'

        print '->>>>>>>>>>>>> %s' %response.body
        yield response

    # def parse_question(self, response):
    #     yield {
    #         'title': response.css('h1 a::text').extract_first(),
    #         'votes': response.css('.question .vote-count-post::text').extract_first(),
    #         'body': response.css('.question .post-text').extract_first(),
    #         'tags': response.css('.question .post-tag::text').extract(),
    #         'link': response.url,
    #     }