import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('') # just pass the web link here
page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())
