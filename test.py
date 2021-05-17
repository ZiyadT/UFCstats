import tkinter as tk
from urllib.request import urlopen
import io
import base64
from bs4 import BeautifulSoup

name_components = ["Israel", "Adesanya"]
url = "http://ufcstats.com/statistics/fighters/search?query=" + name_components[0]
request = urlopen(url)
request_in_html = request.read()
request.close()
html_parsed = BeautifulSoup(request_in_html, 'html.parser')
testing = html_parsed.find_all('a', class_='b-link b-link_style_black')

for x in range(len(testing)):
    if testing[x].text == name_components[0] and testing[x+1].text == name_components[1]:
        fighter_url = testing[x]['href']
print(fighter_url)
name = "Rafael DOs Anjos"

print(name.split(' ', 1))