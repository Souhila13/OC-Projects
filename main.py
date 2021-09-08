import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv

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
        book["descrition"] = soup.find_all('p')[3].text
        return book

# test sur une url
#pprint(livre(http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html))

def clear(titre):
    """une petite fonction pour nettoyer les titres, enlever les espaces en trop"""
    propre = ""
    for lettre in titre:
        if lettre != " ":
            propre += lettre
    return propre

def liste_categories():
    """Retourne un dictionnaire avec toutes les catégories"""
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    page = requests.get(url)
    html = page.text
    soup = BeautifulSoup(html, "lxml")
    liens = soup.aside.find_all('a')
    categories = {}
    for lien in liens[1:]:
        url_cat = "http://books.toscrape.com/catalogue/category/" + lien['href'][3:]
        categories[clear(lien.text.replace("\n", ""))] = url_cat
    return categories

pprint(liste_categories())

# Maintenant que nous avons la liste des catégories et leur url, il faut réccupérer les livres de chaque catégorie

url = "https://books.toscrape.com/"

def get_all(url):
    """ cette fonction pas utilisée permet de réccupérer tous les livres
    attention, pour le moment elle ne prend que la première page"""
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

book = livre(url)

with open('librairie.csv', 'w') as file:
    code = list(book.keys())
    for link in write: 
        file.write(link + '\n')


url = "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"

response = requests.get(url)
if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        info = soup.find('ol', {'class': 'row'}) 
        print(info)


