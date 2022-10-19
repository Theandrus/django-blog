from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('<int:article_id>/like/', views.post_like, name="post_like"),
    path('create_post', views.create_post, name="create_post"),
    path('post_add', views.post_add, name="post_add"),

]