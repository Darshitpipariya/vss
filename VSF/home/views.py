from django.shortcuts import render,redirect
from .models import blog,news,contact_details,OurStartUp,PressReleases,StartupSessions,Events,incubation,launchpad,accelaration
from .forms import contact_form
from django.http import HttpResponse,JsonResponse


# Create your views here.
def home(request):
    OurStartUpimg = OurStartUp.objects.all()
    form=contact_form()
    context={'form':form,"OurStartUpimg":OurStartUpimg}
    return render(request,'home.html',context)

def blogs(request):
    blog_list=blog.objects.all().order_by('-date_created')
    context={"blog_list":blog_list}
    return render(request,'blog.html',context)

def blog_show(request,pid):
    blog_data=blog.objects.get(id=pid)
    blog_list=blog.objects.all().order_by('-date_created')
    context={"blog_list":blog_list,'blog_data':blog_data,"blog_show":True}
    return render(request,'blog.html',context)

def newss(request):
    news_list=news.objects.all().order_by('-date_created')
    context={"news_list":news_list}
    return render(request,'news.html',context)

def news_show(request,pid):
    news_data=news.objects.get(id=pid)
    news_list=news.objects.all().order_by('-date_created')
    context={"news_list":news_list,'news_data':news_data,"news_show":True}
    return render(request,'news.html',context)

def gallery(request):
    imgPressReleases = PressReleases.objects.all()
    imgStartupSessions = StartupSessions.objects.all()
    imgEvents = Events.objects.all()
    context = {"imgPressReleases":imgPressReleases,"imgStartupSessions":imgStartupSessions,"imgEvents":imgEvents}
    return render(request,'gallery.html',context)

def get_detail(request):
    if request.method=='POST':
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('')
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)

def Startups(request):
    OurStartUpimg = OurStartUp.objects.all()
    context={"OurStartUpimg":OurStartUpimg}
    return render(request,"startups.html",context)

def Incubation(request):
    page_data=incubation.objects.all().first()
    context={'page_data':page_data}
    return render(request,'rander_page.html',context)

def Launchpad(request):
    page_data=launchpad.objects.all().first()
    context={'page_data':page_data}
    return render(request,'rander_page.html',context)

def Accelaration(request):
    page_data=accelaration.objects.all().first()
    context={'page_data':page_data}
    return render(request,'rander_page.html',context)