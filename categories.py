import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# importation des fonction dans book.py
from book import book_url_info, get_page
import csv


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
        print(info)
        books_info_list.append(info)

    next = soup.select_one(".next a")
    if next is not None:
        url_next = urljoin(url, next['href'])
        books_info_list += get_all_pages(url_next)
    return books_info_list


def main():
    book_url = get_all_pages(
        f"https://books.toscrape.com/catalogue/category/books_1/index.html")
    # print(len(book_url))

    save_tocsv(book_url)


def save_tocsv(books_info_list):
    header = [
        "title",
        "price",
        "review_rating",
        "number_available",
        "product_description",
        "universal_product_code",
        "price_excluding_tax",
        "price_including_tax",
        "image_url"
    ]

    with open('categorie.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in books_info_list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
