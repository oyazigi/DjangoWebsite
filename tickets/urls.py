from django.urls import path
from tickets.views import home

urlpatterns = [
    path('', home), # Home
]