from django.urls import path
from silveiraAdv.views import home, contato, sobre


urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),
    path('contato/', contato),
]
