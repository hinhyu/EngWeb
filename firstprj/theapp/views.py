from django.shortcuts import render

# Create your views here.
def intro(requests):
    return render(requests,'intro.html')