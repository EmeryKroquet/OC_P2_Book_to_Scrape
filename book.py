# importation des modules
import requests
from bs4 import BeautifulSoup
# urllib pour concatener les urls
from urllib.parse import urljoin


# debut des fonctions de récuperation des infos d'une page

def get_page(url):
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, "html.parser")
    return soup

# fonction de reccuperation d' upc


def get_universal_product_code(soup):
    return soup.select_one(".table.table-striped td").text

# fonction de reccuperation prix avant tax


def get_price_excluding(soup):
    return soup.select("table.table-striped td")[2].text

# fonction de reccuperation prix après tax

def get_price_including(soup):
    return soup.select(".table.table-striped td")[3].text

# fonction de reccuperation de titre


def get_title(soup):
    return soup.select_one(".col-sm-6.product_main h1").text

# fonction de reccuperation de prix


def get_price(soup):
    return soup.select_one("p.price_color").text

# fonction de reccuperation de nombre des livres en stock


def get_number_available(soup):
    return soup.select(".table.table-striped td")[5].text

# fonction de reccuperation les nobres des étoiles


def get_review_rating(soup):
    stars = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return stars[soup.select_one(".star-rating")['class'][1]]

# fonction de reccuperation de descriptions


def get_product_description(soup):
    if soup.select_one(".product_page > p"):
        return soup.select_one(".product_page > p").text
    else:
        return ""

# fonction de reccuperation l'url de l'images


def get_image_url(soup, url):
    return urljoin(url, soup.select_one(".item.active img")['src'])

# appelle des fonctions


def book_url_info(soup, book_url):
    title = get_title(soup)
    price = get_price(soup)
    universal_product_code = get_universal_product_code(soup)
    price_excluding_tax = get_price_excluding(soup)
    price_including_tax = get_price_including(soup)
    number_available = get_number_available(soup)
    review_rating = get_review_rating(soup)
    image_url = get_image_url(soup, book_url)
    product_description = get_product_description(soup)
# demande de retour des info afin de les recuper dans un dictionnaire
    return {
        "title": title,
        "price": price,
        "universal_product_code": universal_product_code,
        "price_excluding_tax": price_excluding_tax,
        "price_including_tax": price_including_tax,
        "number_available": number_available,
        "review_rating": review_rating,
        "image_url": image_url,
        "product_description": product_description
    }


""" fonction main pour recuper 
et afficher les infos afin le code
ne puisse ne pas ne pas être excuter
en continuer ou sécuriser
"""


def main():
    url = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
    soup = get_page(url)
    info = book_url_info(soup, url)
    print(info)


if __name__ == "__main__":
    main()
