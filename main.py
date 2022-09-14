from importlib.resources import contents
import requests
from bs4 import BeautifulSoup

# Getting the website 
websiteURL = r'https://www.codewithharry.com';

# Getting the HTML
website_content = requests.get(websiteURL);
webHTML = website_content.content
# print(webHTML)

# Parsing the HTML
soup = BeautifulSoup(webHTML , 'html.parser')
# print(soup.prettify())

# HTML Tree Traversal

# Getting the Title
webTitle = soup.find("title")
# print(webTitle)

# Getting any specific tags
webParas = soup.find_all('a');
# print(webParasClass)

# Getting tags with specific class
webClassElements = soup.find_all('li' , class_ = "mx-2")
# print(webClassElements);

# Getting text from tags
# print(soup.find('p').get_text());

# Getting all links in the page
anchor = soup.find_all('a')

all_links = set();
for links in anchor:
    link = links.get('href')
    # print(link)
    if(link != '#'):
        if(link[0] == '/'):
            all_links.add(websiteURL + link);
        elif(link[0] == 'h'):
            all_links.add(link);
            
print(all_links)