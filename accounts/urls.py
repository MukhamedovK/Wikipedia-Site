from django.urls import path

from accounts.views import *
from encyclopedia.views import home_page


urlpatterns = [
    path('', home_page, name='home'),
    path("logout/", logout_page, name="logout"),
    path('login/', log_in, name='login'),
    path('register/', register, name='register'),
]