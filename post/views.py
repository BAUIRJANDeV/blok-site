from django.shortcuts import render
from .models import *


def index(request):
    categories=Categorya.objects.all()
    first_news=[]
    for category in categories:
        category_first_post=News.objects.filter(category=category).first()
        if category_first_post is not None:
            first_news.append(category_first_post)
    if len(first_news)<4:
        news=News.objects.all()
        first_news.extend(news[len(news)-4:len(news)-len(first_news)])
    news=News.objects.all().order_by('-created_at')
    news1 = News.objects.filter(category__name='Jahon').order_by('-created_at')
    news2 =  News.objects.filter(category__name='O‘zbekiston').order_by('-created_at')
    return render(request,'index.html',{'categories':categories,'first_news':first_news,'news':news,'news1':news1,'news2':news2})
# Create your views here.
