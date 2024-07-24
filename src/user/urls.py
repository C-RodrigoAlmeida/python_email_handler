from django.urls import path
from src.user.views.registration import RegistrationView
from src.user.views.login import LoginView

app_name = "user"

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login')
]
