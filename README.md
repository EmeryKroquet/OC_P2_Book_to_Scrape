# projet2
Creation de l'environnement de python : 

    . python -m venv env 

 Ativation de l'environnement : 

    . source env/bin/activate

Desactivation de l'environnement : 

    . deactivate

Installation des librairies : 

    . pip install requests 

    . pip install BeautifulSoup4



1- Fonctionnalité de cette application : 
cette application  permet de récuperer des informations sur un site comerciale de vente de livre.

- La première fonction book.py qui permet de récuperer les informations sur un livre 
    . sa description 
    . son titre 
    . son prix hors tax et avec tax 
    . son code universal (upc)
    . recupére le nombre des étoiles 
    . récupère l'url de l'image

Ainsi dans la deuxième fonction categories.py qui me permet de récuperer les categories des livre et de les convertir dans un fichier csv. 
Dans le cas des catégories qui ont une pagination, j'ai utiliser la boucle IF avec la next qui permet de récuperer tous les livres d'une categopries avec pagionation, les images, les urls et toutes les autres informations de celle-ci en faisant appelle à la fonction book, get_page et le dictionaire book_url_info dans le quel sont stoquer les données et les sauvergarder dans un fichier csv.  

Excution de l'application :
 . python -m book
 . python -m categories