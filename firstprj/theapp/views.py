from django.shortcuts import render
from .models import Article

# Create your views here.
def intro(requests):
    article = Article.objects
    return render(requests, 'intro.html', {'article':article})

def base(requests):
    return render(requests, 'base.html')