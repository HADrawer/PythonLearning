import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
noStrachSoup = bs4.BeautifulSoup(res.text , 'html.parser')

element = noStrachSoup.select('#mp-tfa ')
print(element)
print(element[0].getText())