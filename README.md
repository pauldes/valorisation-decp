# valorisation-decp

Prérequis :
* pipenv
* Python 3.8

Installer les dépendances  :
```shell
pipenv install
```

Télécharger le jeu de donnnées DECP (pré-requis aux autres commandes) :
```shell
pipenv run python script.py download
```

Télécharger uniquement les 100 premières lignes du jeu de donnnées DECP :
```shell
pipenv run python script.py download --rows 100
```

Afficher un échantillon du jeu de donnnées et sa taille :
```shell
pipenv run python script.py load
```

Lancer l'application Web d'analyse de qualité :
```shell
pipenv run python script.py web
```

Obtenir de l'aide :
```shell
pipenv run python script.py --help
```