from importlib.resources import contents
import requests
from bs4 import BeautifulSoup

# Getting the website 
websiteURL = r'https://www.codewithharry.com';

# Getting the HTML
website_content = requests.get(websiteURL);
webHTML = website_content.content
# print(webHTML)


