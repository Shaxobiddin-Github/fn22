from django.shortcuts import render,redirect
from django.core.handlers.wsgi import WSGIRequest 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import permission_required,login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings
from django.contrib.auth.models import User


from .models import Category, News,Comment
from .forms import RegisterForm,LoginForm

@login_required(login_url="login")
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

@login_required
@permission_required('app.view_news')
def detail(request, pk):
    news = News.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        "news":news,
        "categories":categories
    }
    return render(request, "app/detail.html",context)




def save_comments(request:WSGIRequest,news_id):
    news= News.objects.get(id=news_id)
    Comment.objects.create(
        user = request.user,
        news = news,  
        text = request.GET.get("text")
    )
    messages.success(request, "Komment qushildi")
    return redirect('detail', pk=news_id)

    



def register(request:WSGIRequest):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
            " Tabriklaymiz......  \n"
            "  Siz muvaffaqiyatli ruyxatdan utdingiz\n"
            "Login parolni terib saytimizga kiring!")
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
            messages.success(request, f"saytga xush kelibsiz {user.username}")
            return redirect('home')
        else:
            
            pass
    else:
        login_form = LoginForm()
    context={
        "login_form":login_form,
    }
    return render(request, "login.html",context)

@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, "Siz saytdan muvaffaqiyatli chiqdingiz!!")
    return redirect('login')


def save_comments(request:WSGIRequest,news_id):
    news= News.objects.get(id=news_id)
    Comment.objects.create(
        user = request.user,
        news = news,  
        text = request.GET.get("text")
    )
    messages.success(request, "Komment qushildi")
    return redirect('detail', pk=news_id)



@login_required
@permission_required("app.change_news","login")
def change_news(request):
    return  HttpResponse("o'zgartirish")


@login_required
def send_message_to_email(request:WSGIRequest):
    if request.user.is_staff:
        if request.method == "POST":
            title = request.POST.get("title")
            text = request.POST.get("text")
            
            users = User.objects.all()

            send_mail(
                title,
                text,
                settings.EMAIL_HOST_USER,
                [user.email for user in users],
                fail_silently=False,
            )
            messages.success(request, "xabar yuborildi📑")
        return render(request,"app/send_message.html")
    else:
        page = request.META.get("Http_REFERER", "home")
        return redirect(page)