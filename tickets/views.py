from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'tickets/pages/home.html', status=200, context={'nome': 'victor'})
