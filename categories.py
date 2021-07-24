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
def get_url_page(soup):
    categories = []
    
    # scrape data for every book URL: this may take some time

    categories = soup.find_all("ul", class_= "nav nav-list")
    for categorie in categories:
        categories_lk = urljoin(url, categorie.find("li").a.get("href"))
        book = categorie.find("li").a. text.strip()
        book_list = {"categories_lk": categories_lk, "book": book}
        book_lists.append(book_list)
        print(book_lists)
    return book_lists
    

def main():
    book_url = get_all_pages(
        f"https://books.toscrape.com/index.html")
    # print(len(book_url))

    save_tocsv(book_url)


def save_tocsv(books_info_list, book_lists):
    header = [{
        "categories_lk": categories_lk,
        "book": book,
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

    with open('books.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in books_info_list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
