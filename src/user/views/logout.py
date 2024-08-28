from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserLogout(LogoutView, LoginRequiredMixin):
    def get_next_page(self):
        next_page = super().get_next_page()
        return next_page