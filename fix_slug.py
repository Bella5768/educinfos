from articles.models import Article

article = Article.objects.filter(slug='www.educinfos.com').first()
if article:
    article.slug = 'educinfos-com'
    article.save()
    print('Slug corrigé')
else:
    print('Article non trouvé')
