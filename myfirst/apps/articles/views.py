from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Article
from django.urls import reverse
from django.utils import timezone


def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'latest_articles': latest_articles})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("The article has not found(")

    latest_comments = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments': latest_comments})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("The article has not found(")

    a.comment_set.create(author_name=request.user, comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def post_like(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("The article has not found(")
    if a.likes.filter( username=request.user.username).exists():
        a.likes.remove(request.user)
    else:
        a.likes.add(request.user)
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'latest_articles': latest_articles})


def create_post(request):
    return render(request, 'articles/create_post.html')


def post_add(request):
    a = Article(author_id=request.user.id, article_title=request.POST['title'], article_text=request.POST['text'], pub_date=timezone.now())
    a.save()
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'latest_articles': latest_articles})
