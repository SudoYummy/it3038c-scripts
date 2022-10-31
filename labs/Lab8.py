#This will pull all players that are in the NFL that went to college that started with an 'O'

from urllib import request
from bs4 import BeautifulSoup
import requests, re

data = requests.get('http://www.espn.com/nfl/college/_/letter/o').content
output = []
soup = BeautifulSoup(data, 'html.parser')

table = soup.findAll("tr", {"class":re.compile('(evenrow player-\d\d-\d\d\d\d\d\d\d|oddrow player-\d\d-\d\d\d\d\d\d\d)')})

for player in table:
    name = player.findAll("a", {"href":re.compile('(http:\/\/www\.espn\.com\/nfl\/player\/_\/id\/\d\d\d\d\d\d\d\/.+)')})
    
    for n in name:
        output.append((re.compile('>(.+)<').findall(str(n))))
        
for entry in output:
    print(entry)