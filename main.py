import requests
from bs4 import BeautifulSoup 

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    header = soup.find_all('div', {'class': 'product_main'})
    print(header[0])

    titre = header[0].find('h1').text
    print(titre)

    page = soup.find_all('article', {'class': 'product_page'})
    print(page[0].text)

    book = {}
    book["name"] = "A Light in the Attic" """mettre le titre"""
    book["price"] = "51.77" """mettre le prix""" 


    table = soup.table.find_all('td') 
    code = table[0].text
    prix = table[3].text

    description = soup.find_all('p')[3].text 
    
    print(book)



    """for valeur in book.values(): 
        print(valeur)"""

   """for cle in book.keys(): 
        print (cle)"""

    
    
    




        

        











  




