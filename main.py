import requests
from bs4 import BeautifulSoup 


def livre(url):
    
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.find_all('div', {'class': 'product_main'})
        print(header[0])

        titre = header[0].find('h1').text
        print(titre)

        page = soup.find_all('article', {'class': 'product_page'})
        print(page[0].text)

        table = soup.table.find_all('td')
        
        book = {}
        
        code = table[0].text
        prix = table[3].text
        inclu = table[3].text
        exclu = table[2].text
        stock = table[5].text
        vue = table[6].text

        image_url = "http://books.toscrape.com" + soup.img['src'][5:]
        
        book["image_url"] = image_url
        print(image_url)

        book["name"] = titre
        book["price"] = prix
        book["code"] = code 

        book["price_inclu"]= inclu
        book["price_exclu"] = exclu
        book["available"] = stock
        book["review_rating"] = vue
        return book
    """description = soup.find_all('p')[3].text """
    
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    
print(livre(url))



url = "https://books.toscrape.com/"

response = requests.get(url)

if response.ok: 
    links_r = []
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('div', {'class': 'image_container'})
    for div in links: 
        a = div.find('a')
        link = a['href']
        links_r.append("https://books.toscrape.com/" + link)
        
    
print(links_r)

for book in links_r: 
    print(livre(book))





url = "https://books.toscrape.com/catalogue/category/"

response = requests.get(url)


if response.ok:
    link_r = []
    soup = BeautifulSoup(response.text, 'html.parser')
    links =soup.find_all('div', {'class': 'page_inner'})
    print(

    )
"""for category in url: 
     = div.find('li')
    links_r.append("https://books.toscrape.com/catalogue/category/" + link.replace)

    print(category)
"""
