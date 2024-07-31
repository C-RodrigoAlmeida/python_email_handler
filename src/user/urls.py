from django.urls import path
from src.user.views.registration import RegistrationView
from src.user.views.login import LoginView
from src.user.views.panel import PanelView

app_name = "user"

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('panel/', PanelView.as_view(), name='panel'),
]
