import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# importation des fonction dans book.py
from book import book_url_info, get_page
import csv
from collections import OrderedDict
import os

#url = "https://books.toscrape.com/index.html"
# créations des fonctions de categorie
def get_all_pages(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
# boucle pour recuperer les urls d'une categorie et les images
    book_urls = soup.select("h3 a")
    books_info_list = []
    for book_url in book_urls:
        book_url = urljoin(url, book_url['href'])

        info = book_url_info(get_page(book_url), book_url)
        books_info_list.append(info)

    # next = soup.select_one(".next a")
    # if next is not None:
    #     url_next = urljoin(url, next['href'])
    #     books_info_list += get_all_pages(url_next)
        
    return books_info_list

def main():
    url = "https://books.toscrape.com/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser") 

    categories_list = soup.select(".nav.nav-list li a")
    
    for category in categories_list:
        if category['href'] is not None:
            category_name = category.text.strip()
            category_url = urljoin(url, category['href'])
            books_list = get_all_pages(category_url)
            
            save_tocsv(books_list, category_name)
        
def save_tocsv(books_info_list, category_name):
    header = OrderedDict([      
        ("title",None),
        ("price", None),
        ("review_rating", None),
        ("number_available", None),
        ("product_description", None),
        ("universal_product_code", None),
        ("price_excluding_tax", None),
        ("price_including_tax", None),
        ( "image_url", None)
    
    ])

    with open(category_name +".csv", 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in books_info_list:
            writer.writerow(row)
            

def imagedownload(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    images = soup.select('img')

    for image in images:
        name = image['alt']
        link = urljoin(url, image['src'])
        
        with open(name + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)
    #return imagedownload
        
# url = imagedownload("https://books.toscrape.com")
# imageUrl = get_all_pages(url)
# print(imageUrl)
    
    urlImage(imagedownload)
    
if __name__ == "__main__":
    
    main()
    