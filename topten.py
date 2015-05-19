from bs4 import BeautifulSoup
#get html document from pittnews.com -> call it html_doc
soup = BeautifulSoup(html_doc)

# looks like class structure is .top-ten > .item > .top > .title > a href
# where href="x" x is article link and <a>y</a> is the article title

# also look up email libraries and send weekly email with top ten titles and links
