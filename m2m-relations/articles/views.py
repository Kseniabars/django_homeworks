from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.prefetch_related('tags').order_by(ordering).all()
    context = {
        'articles': articles
    }
    return render(request, template, context)
