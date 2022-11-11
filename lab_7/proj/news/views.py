from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def rubrika(request):
    return render(request, 'rubrika.html', {})


def article(request):
    return render(request, 'article.html', {})
