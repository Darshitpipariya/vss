from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blogs', views.blogs,name='blogs'),
    path('blogs/<slug:pid>',views.blog_show,name='blog'),
    path('news', views.newss,name='news'),
    path('news/<slug:pid>',views.news_show,name='news_item'),
    path('contact',views.contact_us,name='contact_us'),
    path('about',views.about_us,name='about_us'),
    path('incubation_program',views.incubation_program,name='incubation_program'),
    path('Launchpad_program',views.Launchpad_program,name='Launchpad_program'),
    path('Acclerator_program',views.Acclerator_program,name='Acclerator_program'),
    path('gallery',views.gallery,name='gallery'),
    path('get_detail',views.get_detail,name='get_detail'),
]