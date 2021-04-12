from django.shortcuts import render
from newsapi import NewsApiClient
from newsApp.models import Post,Saved
from django.http import HttpResponse
# from django.template import context
# Create your views here.

def index(request): 
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')
    headLines = newsApi.get_top_headlines(sources = 'bbc-news')
    articles = headLines['articles']
    
    desc = []
    news = []
    img = []
    idd = []

    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)


    return render(request, "main/index.html", context = {"mylist": mylist})

    # return render(request, 'blog/index.html',
    #          context={'all_articles': all_articles, 'message': 'Write something!'})

def readmore(request):
    return render(request, "main/readmore.html", {'aa':a})

def save(request):
    tmp = request.GET["ib"]
    me = Post.objects.get(idd = tmp)
    print(tmp)
    Saved.objects.create(idd = me.idd, desc = me.desc, news = me.news, img = me.img)
    return HttpResponse("")