from django.shortcuts import render, redirect
from article.models import Article


def home(request):
    return redirect('/article/list')


def list(request):
    articles = Article.objects.order_by('-votes')
    return render(request, 'article/list.html', dict(articles=articles))


def add(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        author = request.POST.get("author", "")
        a = Article(title=title, content=content, author=author)
        a.save()
        return redirect('/article/list')
    else:
        return render(request, 'article/add.html')


def vote(request, id):
    a = Article.objects.get(id=id)
    a.votes += 1
    a.save()
    return redirect('/article/list')
