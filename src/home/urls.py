from django.urls import path
from src.home.views.home import Home
from src.home.views.guide import Guide
app_name = "home"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('guide/', Guide.as_view(), name='guide'),
]