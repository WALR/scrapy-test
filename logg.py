from loginform import fill_login_form
import requests

url = "https://github.com/login"
r = requests.get(url)
fill_login_form(url, r.text, "john", "secret")