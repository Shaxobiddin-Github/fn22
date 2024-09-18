from django.shortcuts import render,redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import login, logout





from .models import Category, News
from .forms import RegisterForm,LoginForm


def index(request):
    newsers = News.objects.filter(is_active = True)
    news_banner = newsers.filter(is_banner=True).last()
    news_top_story = newsers.order_by("-views").first()
    latest_news = newsers.order_by("-created")[:8]
    latest_news_jahon = newsers.filter(tag=1).last()
    categories = Category.objects.all()
    
    context = {
        "news_banner":news_banner,
        "news_top_story":news_top_story,
        "latest_news":latest_news,
        "categories":categories,
        "latest_news_jahon":latest_news_jahon,
            }
    return render(request, "app/index.html",context) 

def detail(request, pk):
    news = News.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        "news":news,
        "categories":categories
    }
    return render(request, "app/detail.html",context)



def register(request:WSGIRequest):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.error_messages, "**********************************")

    else:
        form = RegisterForm()

    context={
        "form":form,
    }
    return render(request, "register.html", context)


def user_login(request:WSGIRequest):
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user=login_form.get_user()
            login(request,user)
            return redirect('home')
    login_form = LoginForm()
    context={
        "login_form":login_form,
    }
    return render(request, "login.html",context)


def user_logout(request):
    logout(request)
    return redirect('login')