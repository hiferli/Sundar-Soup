from bs4 import BeautifulSoup
import re

with open("otherIndex.html" , 'r') as file:
    document = BeautifulSoup(file , 'html.parser');

tag = document.find(text = re.compile("\$.*"));
print(tag)