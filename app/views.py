from django.shortcuts import render
from .models import Category, News


def index(request):
    newsers = News.objects.filter(is_active = True)
    news_banner = newsers.filter(is_banner=True).last()
    news_top_story = newsers.order_by("-views").first()
    latest_news = newsers.order_by("-created")[:8]
    context = {
        "news_banner":news_banner,
        "news_top_story":news_top_story,
        "latest_news":latest_news,
    }
    return render(request, "app/index.html",context) 