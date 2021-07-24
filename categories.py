import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# importation des fonction dans book.py
from book import book_url_info, get_page
import csv
import re


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

    next = soup.select_one(".next a")
    if next is not None:
        url_next = urljoin(url, next['href'])
        books_info_list += get_all_pages(url_next)
    return books_info_list

# creat a new function in categories
def get_page_categories(soup):
    
    categories = []

    # scrape data for every book URL: this may take some time

    links = soup.find_all("ul", class_= "nav nav-list")
    for link in links:
        categories_lk = urljoin(url, link.find("li").a.get("href"))
        name = link.find("li").a. text.strip()
        book_list = {
                    "categories_lk": categories_lk, 
                    "name": name
                    }
        categories.append(book_list)
        #print(book_lists)
    return categories

def main():
    book_url = get_all_pages(
        f"https://books.toscrape.com/index.html")
    # print(len(book_url))

    save_tocsv(book_url)


def save_tocsv(books_info_list, book_list):
    header = [{
        "categories_lk": categories_lk,
        "name": name,
        "title": title,
        "price": price,
        "review_rating": review_rating,
        "number_available": number_available,
        "product_description": product_descriptio,
        "universal_product_code": universal_product_code,
        "price_excluding_tax": price_excluding_tax,
        "price_including_tax": price_including_ta,
        "image_url":image_url
        }
    ]

    with open('files.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in books_info_list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
