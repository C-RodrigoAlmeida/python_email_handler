from django.contrib.auth.views import LogoutView

class UserLogout(LogoutView):
    def get_next_page(self):
        next_page = super().get_next_page()
        return next_page