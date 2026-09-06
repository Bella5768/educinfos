# Educ.Infos224 - Landing Page

Plateforme d'information spécialisée dans l'actualité de l'éducation en Guinée.

## Installation

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Initialiser la base de données :
```bash
python manage.py migrate
```

3. Créer un superutilisateur (admin) :
```bash
python manage.py createsuperuser
```

4. Lancer le serveur de développement :
```bash
python manage.py runserver
```

Le site sera accessible sur http://127.0.0.1:8000/

## Structure du projet

- `educinfos/` : Configuration principale du projet Django
- `articles/` : Application Django pour la gestion des articles
- `templates/` : Templates HTML
- `static/` : Fichiers statiques (CSS, JS)

## Fonctionnalités

- Page d'accueil avec sections héro, fonctionnalités, articles, à propos et contact
- Système de gestion d'articles via l'admin Django
- Catégorisation des articles (Réformes, Innovations, Initiatives, Résultats, Interviews, Conseils)
- Page de détail d'article
- Liste des articles avec filtrage par catégorie
- Formulaire de contact
- Design responsive

## Admin Django

Accédez au panel d'administration sur http://127.0.0.1:8000/admin/

Connectez-vous avec le superutilisateur créé pour créer et gérer les articles.

## Personnalisation

- Modifier les couleurs dans `static/css/style.css` (variables CSS)
- Adapter le contenu dans les templates HTML
- Configurer les paramètres dans `educinfos/settings.py`
