from django.urls import path
from tickets.views import home, contato, sobre

urlpatterns = [
    path('', home), # Home
    path('contato/', contato), # Contato
    path('sobre/', sobre) # Sobre
]