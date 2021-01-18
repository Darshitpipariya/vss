from django.shortcuts import render,redirect
from .models import blog,news,contact_details
from .forms import contact_form
from django.http import HttpResponse


# Create your views here.
def home(request):
    form=contact_form()
    context={'form':form}
    return render(request,'home.html',context)

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

def contact_us(request):
    return render(request,'main_contact.html')

def about_us(request):
    return render(request, 'main_about.html')

def incubation_program(request):
    return render(request,'incubation_program.html')

def Launchpad_program(request):
    return render(request,'Launchpad_program.html')

def Acclerator_program(request):
    return render(request,'Acclerator_program.html')

def gallery(request):
    return render(request,'gallery.html')

def get_detail(request):
    if request.method=='POST':
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('')
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)

