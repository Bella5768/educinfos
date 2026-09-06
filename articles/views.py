from django.shortcuts import render
from .models import Article


def home(request):
    published_articles = Article.objects.filter(status='published')[:6]
    featured_articles = Article.objects.filter(status='published')[:3]
    context = {
        'articles': published_articles,
        'featured_articles': featured_articles,
    }
    return render(request, 'home.html', context)


def article_detail(request, slug):
    article = Article.objects.get(slug=slug, status='published')
    context = {
        'article': article,
    }
    return render(request, 'article_detail.html', context)


def articles_list(request):
    articles = Article.objects.filter(status='published')
    category_filter = request.GET.get('category')
    if category_filter:
        articles = articles.filter(category=category_filter)
    
    context = {
        'articles': articles,
        'category_filter': category_filter,
    }
    return render(request, 'articles_list.html', context)

