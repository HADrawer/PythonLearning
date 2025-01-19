import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

elements = exampleSoup.select('#author')
print(elements)
print(elements[0].getText())
print(elements[0].attrs)