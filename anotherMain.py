from bs4 import BeautifulSoup
import re

with open("otherIndex.html" , 'r') as file:
    document = BeautifulSoup(file , 'html.parser');

tags = document.find_all("input" , type="text")

for tag in tags:
    tag['placeholder'] = 'Changed';

with open("changedFile.html" , 'w') as file:
    file.write(str(document));