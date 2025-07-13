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
    print(first_news)
    return render(request,'index.html',{'categories':categories,'first_news':first_news})
# Create your views here.
