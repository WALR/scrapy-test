from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from loginform import fill_login_form
 
class LoginSpider(BaseSpider):
 
    start_urls = ["http://github.com/login"]
    login_user = "walr"
    login_pass = "1714412193wa"
 
    def parse(self, response):
        args, url, method = fill_login_form(response.url, response.body, self.login_user, self.login_pass)
        return FormRequest(url, method=method, formdata=args, callback=self.after_login)
 
    def after_login(self, response):
        if "logout" in response.body:
            print '->>>>>>>>>>>>> YEAHHHHHHHHHHHHHHHHHHHHHHHH'
        # you are logged in here