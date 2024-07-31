from django.urls import path
from src.home.views.home import Home

app_name = "home"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', Home.as_view(), name='about'),
]