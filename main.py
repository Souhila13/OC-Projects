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

    table = soup.table.find_all('td')
    
    book = {}
    
    code = table[0].text
    prix = table[3].text
    inclu = table[3].text
    exclu = table[2].text
    stock = table[5].text
    vue = table[6].text
    
    image = soup.find('div', {'id': 'product_gallery'}).text
    book["image_url"] = image
    print(image)

    book["name"] = titre
    book["price"] = prix
    book["code"] = code 

    book["price_inclu"]= inclu
    book["price_exclu"] = exclu
    book["available"] = stock
    book["review_rating"] = vue
    
     


    """description = soup.find_all('p')[3].text """
    
    print(book)



    """for valeur in book.values(): 
        print(valeur) """ 
    """for cle in book.keys(): 
        print (cle) """

    
    
    




        

        











  




