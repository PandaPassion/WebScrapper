import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
#opening the client, grabbing the page 
my_url = "https://www.emag.ro/laptopuri/c?ref=hp_menu_quick-nav_1_1&type=category"
client = ureq(my_url)

#offloading the page into a variabale 
page = client.read()

#closing the client
client.close()

#html parsing 
page_soup= soup(page, 'html.parser')

#grabs each products
containere = page_soup.findAll('div', attrs = {'class':'card'})

for container in containere:
    title = container.find('h2', attrs = {'class':'card-body product-title-zone'})
    price_new = container.find('p', attrs = {'class':'product-new-price'})
    price_old = container.find('p', attrs = {'class':'product-old-price'})
    deal = container.find('span', attrs = {'class':'product-this-deal'})
    in_stock = container.find('p', attrs = {'class':'product-stock-status text-availability-in_stock'}) 
    print(title.a['title'], "price", price_old.text)
print(len(containere))
