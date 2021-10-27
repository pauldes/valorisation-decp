# valorisation-decp

Prérequis :
* pipenv
* Python 3.8

Installer les dépendances  :
```shell
pipenv install
```

Télécharger le jeu de donnnées DECP augmmenté :
```shell
pipenv run python script.py download --augmented
```

Télécharger uniquement les 100 premières lignes du jeu de donnnées DECP augmenté :
```shell
pipenv run python script.py download --augmented --rows 100
```

Télécharger le jeu de données DECP consolidé (pré-requis à l'analyse de données):
```shell
pipenv run python script.py download --consolidated
```

Mener l'analyse de qualité (pré-requis à l'application Web) :
```shell
pipenv run python script.py audit
```

Lancer l'application Web d'analyse de qualité :
```shell
pipenv run python script.py web
```

Obtenir de l'aide :
```shell
pipenv run python script.py --help
```