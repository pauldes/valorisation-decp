#valorisation-decp

Prérequis :
* pipenv
* Python 3.8

Installer les dépendances  :
```python
pipenv install
```

Télécharger le jeu de donnnées DECP :
```python
pipenv run download
```

Télécharger les 100 premières lignes du jeu de donnnées DECP :
```python
pipenv run download --rows 100
```

Afficher un échantillon du jeu de donnnées et sa taille :
```python
pipenv run load
```