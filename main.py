import requests
from bs4 import BeautifulSoup 
from pprint import pprint

def livre(url):
    """ Fonction qui réccupère les informations d'un livre
     et les place dans un dictionnaire"""
   
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.find_all('div', {'class': 'product_main'})
        titre = header[0].find('h1').text
        table = soup.table.find_all('td')
        # book, le dictionnaire qui va contenir toutes les informations.
        book = {}
        book["name"] = titre
        book["image_url"] = "http://books.toscrape.com" + soup.img['src'][5:]
        book["price"] = table[3].text
        book["code"] = table[0].text 
        book["price_inclu"]= table[3].text
        book["price_exclu"] = table[2].text
        book["available"] = table[5].text
        book["review_rating"] = table[6].text
        """book["descrition"] = soup.find_all('p')[3].text"""

        return book

    # test sur une url
print(livre("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"))
        
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

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

 
if response.ok:
    category = []
    soup = BeautifulSoup(response.text, 'html.parser')
    links =soup.find_all('div', {'class': 'side_categories'})
    for li in links:
        categorie = li.find('ul')
        link = a['href']
        
        print(categorie)
        #category.append("https://books.toscrape.com/catalogue/category/books/travel_2/index.html" + link)   
"""
for book in links_r:
    print(livre(book))
"""
  