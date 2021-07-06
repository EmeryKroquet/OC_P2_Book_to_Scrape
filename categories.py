import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# importation des fonction dans book.py
from books import book_url_info, get_page

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


def main():
    book_url = get_all_pages(
        f"https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
    # print(len(book_url))


book_info = [{
    "title":  title,
    "price": price,
    "universal_product_code": universal_product_code,
    "price_excluding_tax": price_excluding_tax,
    "price_including_tax": price_including_tax,
    "number_available": number_available,
    "review_rating": review_rating,
    "image_url": image_url,
    "product_description": product_description
}

    {
    "title":  title,
    "price": price,
    "universal_product_code": universal_product_code,
    "price_excluding_tax": price_excluding_tax,
    "price_including_tax": price_including_tax,
    "number_available": number_available,
    "review_rating": review_rating,
    "image_url": image_url,
    "product_description": product_description
}

{
    "title":  title,
    "price": price,
    "universal_product_code": universal_product_code,
    "price_excluding_tax": price_excluding_tax,
    "price_including_tax": price_including_tax,
    "number_available": number_available,
    "review_rating": review_rating,
    "image_url": image_url,
    "product_description": product_description
}
{
    "title":  title,
    "price": price,
    "universal_product_code": universal_product_code,
    "price_excluding_tax": price_excluding_tax,
    "price_including_tax": price_including_tax,
    "number_available": number_available,
    "review_rating": review_rating,
    "image_url": image_url,
    "product_description": product_description
}

]

save_tocsv(books_info_list)


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
