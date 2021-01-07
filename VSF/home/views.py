from django.shortcuts import render
from .models import blog,news

# Create your views here.
def home(request):
    return render(request,'home.html')

def blogs(request):
    blog_list=blog.objects.all().order_by('-date_created')
    print(blog_list)
    context={"blog_list":blog_list}
    return render(request,'blog.html',context)

def blog_show(request,pid):
    blog_data=blog.objects.get(id=pid)
    print(blog_data)
    blog_list=blog.objects.all().order_by('-date_created')
    print(blog_list)
    context={"blog_list":blog_list,'blog_data':blog_data,"blog_show":True}
    return render(request,'blog.html',context)

def newss(request):
    news_list=news.objects.all().order_by('-date_created')
    print(news_list)
    context={"news_list":news_list}
    return render(request,'news.html',context)

def news_show(request,pid):
    news_data=news.objects.get(id=pid)
    print(news_data)
    news_list=news.objects.all().order_by('-date_created')
    print(news_list)
    context={"news_list":news_list,'news_data':news_data,"news_show":True}
    return render(request,'news.html',context)

def basic1(request):
    return render(request,'basic1.html')