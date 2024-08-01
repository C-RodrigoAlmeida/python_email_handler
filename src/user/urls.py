from django.urls import path
from src.user.views.registration import RegistrationView
from src.user.views.login import LoginView
from src.user.views.panel import PanelView
from src.user.views.profile import ProfileView
from src.user.views.logout import UserLogout

app_name = "user"

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('panel/', PanelView.as_view(), name='panel'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
