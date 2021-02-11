from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<slug:pid>", views.blog_show, name="blog"),
    path("news", views.newss, name="news"),
    path("news/<slug:pid>", views.news_show, name="news_item"),
    path("gallery", views.gallery, name="gallery"),
    path("get_detail", views.get_detail, name="get_detail"),
]
