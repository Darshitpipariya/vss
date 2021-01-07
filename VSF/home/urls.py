from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blogs', views.blogs,name='blogs'),
    path('blogs/<slug:pid>',views.blog_show,name='blog'),
    path('news', views.newss,name='news'),
    path('news/<slug:pid>',views.news_show,name='news_item'),
    path('basic',views.basic1),
]