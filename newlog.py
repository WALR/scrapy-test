from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule

class UMG(InitSpider):
    name = 'umg'
    allowed_domains = ['apps.umg.edu.gt']
    login_page = 'https://apps.umg.edu.gt/signup/'
    start_urls = ['https://apps.umg.edu.gt/',
                  'https://apps.umg.edu.gt/notas']

    # rules = (
    #     Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
    #          callback='parse_item', follow=True),
    # )

    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'name': 'wlemusr', 'password': 'W@lr6074500'},
                    callback=self.check_login_response)

    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "logout" in response.body:
            print ">>>>>>>>>>>>>>>>>>>>>YEAHHHHH"
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            self.initialized()
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.

    # def parse_item(self, response):

    #     # Scrape data from page