# projet 2 dans le cadre de formation Développeur d'Application Python chez Openclassrooms le plus grand platforme de formation 💯 en ligne en Europe

# Thème:
## Utilisez les bases de Python pour l'analyse de marché

# Scenario: 
Vous êtes analyste marketing chez Books Online, une importante librairie en ligne spécialisée dans les livres d'occasion. Dans le cadre de vos fonctions, vous essayez de suivre manuellement les prix des livres d'occasion sur les sites web de vos concurrents, mais cela représente trop de travail et vous n'arrivez pas à y faire face : il y a trop de livres et trop de librairies en ligne ! Vous et votre équipe avez décidé d'automatiser cette tâche laborieuse via un programme (un scraper) développé en Python, capable d'extraire les informations tarifaires d'autres librairies en ligne.

## Les étapes pour cloner le ripositorie sur votre machine local

Creation de l'environnement de python : 

    . python -m venv env 


 Ativation de l'environnement : 

Ativation de l'environnement : 

    . source env/bin/activate

Desactivation de l'environnement : 

    . deactivate

Installation des librairies : 

    . pip install requests 

    . pip install BeautifulSoup4



1- Fonctionnalité de cette application : 
cette application  permet de récuperer des informations sur un site comerciale de vente de livre.

- La première fonction P2_01_codesource.py qui me permet de récuperer les informations sur un livre 
    . sa description 
    . son titre 
    . son prix hors tax et avec tax 
    . son code universal (upc)
    . recupére le nombre des étoiles 
    . récupère l'url de l'image

Ainsi dans la deuxième fonction P2_02_codesource.py qui me permet de récuperer les categories des livre et de les convertir dans un fichier csv. 
Dans le cas des catégories qui ont une pagination, j'ai utiliser la boucle IF avec la next qui permet de récuperer tous les livres d'une categopries avec pagionation, les images, les urls et toutes les autres informations de celle-ci en faisant appelle à la fonction book, get_page et le dictionaire book_url_info dans le quel sont stoquer les données et les sauvergarder dans un fichier csv.  

Excution de l'application :
 . python -m book
 . python -m categories


L'excution de l'application :
     . python -m book
     . python -m categories
