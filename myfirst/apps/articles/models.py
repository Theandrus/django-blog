from django.db import models
from django.conf import settings
import datetime


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_title = models.CharField('name of the article', max_length=50)
    article_text = models.TextField('article text')
    pub_date = models.DateTimeField('date of publication')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blogpost_like')

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('name of author', max_length=50)
    comment_text = models.CharField('comment text', max_length=200)

    def __str__(self):
        return self.author_name
