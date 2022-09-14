import requests
from bs4 import BeautifulSoup

url = r'https://coinmarketcap.com/';
document = BeautifulSoup(requests.get(url).text , 'html.parser');

tableBody = document.tbody;
tableRows = tableBody.contents

# print(tableRows[0].next_sibling);

prices = {};

for rows in tableRows[:10]:
    name , price = rows.contents[2:4];
    # print(name.p.string + " - " + price.a.string)
    prices[name.p.string] = price.a.string;

print(prices)