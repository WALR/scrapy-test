from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.http.request import Request
from loginform import fill_login_form
from scrapy import log
from scrapy.item import Item

from scrapy.item import Item, Field

class ArticleItem(Item):
    title = Field()
    url = Field()



class GitHubLogin(BaseSpider):

    name = 'GitHubLogin'
    allowed_domains = ['umg.edu.gt']
    # allowed_domains = ['github.com']
    start_urls = ['https://apps.umg.edu.gt/signup/']
    # start_urls = ['http://github.com/login']
    login_user = 'wlemusr'
    # login_user = 'wilfred.lean.15@gmail.com'
    login_pass = 'W@lr6074500'
    # login_pass = '1714412193wa'

    def parse(self, response):
        (args, url, method) = fill_login_form(response.url,
                response.body, self.login_user, self.login_pass)
        return FormRequest(url, method=method, formdata=args,
                           callback=self.after_login)

    def after_login(self, response):
        if "Sign out" in response.body:
            print '->>>>>>>>>>>>> YEAHHHHHHHHHHHHHHHHHHHHHHHH'
        else:
            print '->>>>>>>>>>>>> NOOOOOOOOOOOOOOOOOOOOOOOOOOO :('
        # for link in response.xpath("//*[@id='site-container']/div[2]/div[4]/p/a/@href").extract():

        # item = ArticleItem()
        # item['title'] = 'walr'
        # log.msg('***************    :   '
        #         + str(response.xpath("//form[@class='subnav-search left']/input/@value"
        #         ).extract()))
        # item['url'] = \
        #     response.xpath("//*[@id='site-container']/div[1]/div/div/span/span/text()"
        #                    ).extract()
        # yield item
