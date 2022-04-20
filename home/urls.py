
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home, name="home"),
    path('login/', login_view , name="login_view"),
    path('signup/', signup_view , name="signup_view"),
    path('add_blog/', add_blog_view , name="add_blog_view"),
    path('blog_detail/<slug>' , blog_detail , name="blog_detail"),
    path('see_blog/' , see_blog , name="see_blog"),
    path('blog_delete/<id>' , blog_delete , name="blog_delete"),
    path('blog_update/<slug>/',  blog_update , name="blog_update"),
    path('logout_view/', logout_view , name="logout_view"),
    path('verify/<token>/' , verify , name="verify")
]