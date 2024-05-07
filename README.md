## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis
test git

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement
Premièrement, je ne peux que vous conseiller de vous rendre sur la documentation technique, section deployment ici via le lien ci-dessous

```
https://p13-oc-lettings.readthedocs.io/en/latest/deployment.html
```

Pour voir les étapes de déploiement dans le code vous pouvez vous référer au fichier django.yml présent dans le Git

```
.github/workflows/django.yml
```

Dans le job **django-test-and-quality** vous verrez des {{ secrets.variables }} dans le code.

Ces dernières doivent être ajoutées dans votre repository GitHub
Pour se faire, suivez les instructions ci-dessous :
1. Rendez-vous sur votre compte GitHub
2. Ouvrez les paramètres de ce dernier
3. Cliquez sur "Secrets and variables"
4. Cliquez sur "Actions"
5. Descendez jusqu'à "Repository secrets"

Vous devez ensuite ajouter les valeurs ci-dessous :
* DOCKER_USERNAME : Le nom d'utilisateur de votre compte DockerHub
* DOCKER_PASSWORD : Le mot de passe de votre compte DockerHub
* DOCKER_REPO_NAME : Le nom de votre répertoire sur lequel est votre projet *Voir la partie **build-and-push-docker** plus bas* 
Par exemple ici : r0b1ndock/p13_oc, le nom est **p13_oc**
* LINK_RENDER : *Voir la partie Render plus bas* 
* SECRET_KEY : La clé secrète présente dans votre fichier .env
* SENTRY_KEY_URL : L'URL vers votre project sentry *aussi présent dans votre .env*

Pour terminer ce job, GitHub Action va installer python, puis les dépendances de votre projet avant d'éxécuter toutes les commandes nécessaires aux tests et contrôle qualité.
Par exemple flake8, ou encore coverage. 

Pour le job **build-and-push-docker**

Vous aurez besoin de créer un repository sur votre compte DockerHub
Le nom choisi doit donc aller dans la variable GitHub Action **DOCKER_REPO_NAME**
Le job build simplement votre image Docker avant de l'envoyer sur votre repository en ligne

Enfin le job **deploy-render**

Merci de suivre les instructions ci-dessous :
1. Créer un compte sur render.com
2. Rendez-vous sur le *dashboard*
3. Cliquez sur "New"
4. Choisissez "Web Service"
5. Choisissez "Deploy an existing image from a registry" puis cliquez sur "Next"
6. Entrer les informations demandées
7. Séléctionner le tier souhaité (fonctionne avec le tier gratuit)

Rendez-vous maintenant sur votre Tableau de bord où vous devriez voir apparaître votre Web Service
Suivez les instructions ci-dessous :
1. Allez dans les détails de votre web service
2. Puis dans les paramètres de ce dernier
3. Descendez jusqu'à trouver *Deploy Hook*
4. Copiez le lien and enregistrez-le dans votre variable secrètre GitHub Actions **LINK_RENDER**

Le job enverra une requête au webhook afin de lui permettre de récupérer la dernière version de Docker sur votre repository 

Après toute cette configuration, il ne vous reste plus qu'à push sur votre branche *master* afin d'entrer dans le workflow Github executant tous les jobs listés ci-dessus 
 
### Explication projet

Choix changement model d'applications : https://realpython.com/move-django-model/#the-short-way-reference-the-new-django-model-to-the-old-table
