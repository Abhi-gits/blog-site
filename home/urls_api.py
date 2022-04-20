
from django.urls import path

from home.views_api import LoginView, SignupView
from .views import *

urlpatterns = [
    path('login/', LoginView),
    path('signup/', SignupView)
]