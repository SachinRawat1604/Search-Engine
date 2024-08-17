from django.shortcuts import render
from django.db.models import Q
from .models import Page

# Create your views here.

def search(request):
    return render(request, 'search/search.html')

def results(request):
    query = request.GET.get('q')
    pages = Page.objects.filter(
        Q(title__icontains=query) | 
        Q(content__icontains=query)
    )
    return render(request, 'search/results.html', {'pages': pages})

#create the smaple data using the Django shell.

# cmd ---> python manage.py shell

# Then add website using this cmd
'''from search.models import Page
Page.objects.create(title="Django Documentation", content="Comprehensive documentation for Django.", url="https://www.djangoproject.com/")'''