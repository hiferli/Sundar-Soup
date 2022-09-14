import requests
from bs4 import BeautifulSoup

# websiteURL = r'https://www.crummy.com/software/BeautifulSoup/bs4/doc/';
websiteURL = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

website_content = requests.get(websiteURL);

document = BeautifulSoup(website_content.text , 'html.parser')

# print(document.prettify())

prices = document.find_all(text = "$");
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)

for price in prices:
    print(price.parent.find("strong").string)