# views.py

from django.shortcuts import render

def index(request):
    # Your logic for rendering the index page goes here
    return render(request, 'index.html')
