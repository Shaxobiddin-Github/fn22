from django.shortcuts import render
from .models import Category, News


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