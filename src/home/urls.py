from django.urls import path
from src.home.views.home import Home
from src.home.views.about import About

app_name = "home"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
]