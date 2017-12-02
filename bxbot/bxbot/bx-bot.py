import urllib2
import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://bx.in.th')
soup = BeautifulSoup(page.content, 'html.parser')

listToScrape = ["OMG", "ETH", "XRP", "GNO", "DAS", "EVX", "REP", "XZC"]
others = ["BTC", "BTH", "DOG"]


for coin in listToScrape:
    href = "./THB/%s/" % coin
    print href
    start = soup.find_all("a", {"href": href})
    start = start[len(start) - 1].parent.parent
    x = start.find_next_siblings("td")
    r = "[-]?[0-9]+.[0-9]+"
    print re.findall(r, str(x[3]))[0]
    