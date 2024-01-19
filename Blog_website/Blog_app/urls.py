from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name="home"),
    path("login/",login,name="login"),
    path("logindata/",logindata,name="logindata"),
    path("signup/",signup,name="signup"),
    path("signupdata/",signupdata,name="signupdata"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("services/",services,name="services"),
    path("logout/",logout,name="logout"),
]
