# Guide de déploiement sur PythonAnywhere

## Étape 1 : Préparer le code

1. **Initialiser Git (si pas déjà fait)**
```bash
cd c:\wamp64\www\educinfos
git init
git add .
git commit -m "Initial commit"
```

2. **Pousser sur GitHub/GitLab**
```bash
git remote add origin https://github.com/votre-username/educinfos.git
git push -u origin main
```

## Étape 2 : Configuration PythonAnywhere

1. **Créer un compte** sur https://www.pythonanywhere.com/

2. **Créer un nouveau Web App**
   - Allez dans "Web" → "Add a new web app"
   - Choisissez "Manual configuration"
   - Sélectionnez Python 3.10 ou supérieur

3. **Configurer le virtualenv**
   - Dans la section "Virtualenv", cliquez sur "Create a new virtualenv"
   - Choisissez la même version de Python que votre web app
   - Notez le chemin du virtualenv

4. **Installer les dépendances**
```bash
workon <votre-virtualenv>
pip install -r requirements.txt
```

## Étape 3 : Cloner le projet

```bash
cd ~/<votre-username>.pythonanywhere.com/
git clone https://github.com/votre-username/educinfos.git
```

## Étape 4 : Configurer les variables d'environnement

Dans le tableau de bord PythonAnywhere → Web → Variables

Ajoutez les variables suivantes :
- `DJANGO_SECRET_KEY` : une clé secrète aléatoire (générez-en une avec `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG` : `False`
- `ALLOWED_HOSTS` : `votre-domaine.pythonanywhere.com`

## Étape 5 : Configurer la base de données

```bash
cd ~/<votre-username>.pythonanywhere.com/educinfos
workon <votre-virtualenv>
python manage.py migrate
python manage.py collectstatic --noinput
```

## Étape 6 : Configurer le fichier WSGI

Dans PythonAnywhere → Web → Code → Edit WSGI configuration file

Remplacez le contenu par :
```python
import os
import sys

path = '/home/<votre-username>/<votre-username>.pythonanywhere.com/educinfos'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'educinfos.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Étape 7 : Configurer Static Files

Dans PythonAnywhere → Web → Static files

Ajoutez :
- URL directory : `/static/`
- Directory path : `/home/<votre-username>/<votre-username>.pythonanywhere.com/educinfos/staticfiles`

## Étape 8 : Redémarrer le serveur

Cliquez sur le bouton "Reload" dans la section Web

## Étape 9 : Créer le superutilisateur (optionnel)

```bash
cd ~/<votre-username>/<votre-username>.pythonanywhere.com/educinfos
workon <votre-virtualenv>
python manage.py createsuperuser
```

## Étape 10 : Tester

Accédez à votre site : `https://votre-domaine.pythonanywhere.com/`

## Notes importantes

- Le fichier `db.sqlite3` n'est pas dans Git (voir .gitignore)
- Vous devrez soit :
  - Copier manuellement votre base de données locale
  - Recréer les articles via l'admin Django
  - Utiliser PostgreSQL sur PythonAnywhere (recommandé pour la production)

## Pour utiliser PostgreSQL (recommandé)

1. Créer une base de données dans PythonAnywhere → Databases
2. Installer psycopg2-binary dans requirements.txt :
```
psycopg2-binary
```
3. Modifier settings.py pour PostgreSQL :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<votre-db-name>',
        'USER': '<votre-db-user>',
        'PASSWORD': '<votre-db-password>',
        'HOST': '<votre-db-host>',
        'PORT': '5432',
    }
}
```
