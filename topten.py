from bs4 import BeautifulSoup
import urllib2
from datetime import date

site = 'http://www.pittnews.com'
response = urllib2.urlopen(site)
html_doc = response.read()
soup = BeautifulSoup(html_doc)

print "Top Articles At " + site + " on " + str(date.today()) + "\n"
# looks like class structure is .top-ten > .item > .top > .title > a href
for i,article in enumerate(soup.find('div',class_='top-ten').find_all('div',class_='item')):
	link = article.find('div',class_='top').find('h4',class_='title').find('a')
	print "#" + str(i+1)+": " + link.string
	print "Link: "+ site + link.get('href') + "\n"
