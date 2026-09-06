from django.db import models
from django.utils import timezone


class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
    ]
    
    CATEGORY_CHOICES = [
        ('reforme', 'Réforme'),
        ('innovation', 'Innovation'),
        ('initiative', 'Initiative'),
        ('resultat', 'Résultat'),
        ('interview', 'Interview'),
        ('conseil', 'Conseil'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='reforme',
        verbose_name="Catégorie"
    )
    excerpt = models.TextField(max_length=300, verbose_name="Extrait")
    content = models.TextField(verbose_name="Contenu")
    author = models.CharField(max_length=100, verbose_name="Auteur")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='draft',
        verbose_name="Statut"
    )
    image_url = models.URLField(blank=True, verbose_name="URL de l'image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Mis à jour le")

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
