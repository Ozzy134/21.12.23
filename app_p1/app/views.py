from django.shortcuts import render
from .models import Eat

def index(request):
    dann = Eat(request.POST)
    return render(request, 'index.html', context={'dann': dann})
