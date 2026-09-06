from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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


def dashboard(request):
    articles = Article.objects.all().order_by('-published_date')
    context = {
        'articles': articles,
    }
    return render(request, 'dashboard.html', context)


def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        category = request.POST.get('category')
        excerpt = request.POST.get('excerpt')
        content = request.POST.get('content')
        author = request.POST.get('author', 'Admin')
        status = request.POST.get('status', 'draft')
        image_url = request.POST.get('image_url', '')
        
        article = Article.objects.create(
            title=title,
            slug=slug,
            category=category,
            excerpt=excerpt,
            content=content,
            author=author,
            status=status,
            image_url=image_url
        )
        return redirect('dashboard')
    
    return render(request, 'article_form.html')


def article_edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.slug = request.POST.get('slug')
        article.category = request.POST.get('category')
        article.excerpt = request.POST.get('excerpt')
        article.content = request.POST.get('content')
        article.author = request.POST.get('author', 'Admin')
        article.status = request.POST.get('status', 'draft')
        article.image_url = request.POST.get('image_url', '')
        article.save()
        return redirect('dashboard')
    
    context = {
        'article': article,
    }
    return render(request, 'article_form.html', context)


def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('dashboard')

