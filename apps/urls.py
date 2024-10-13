from django.urls import path

from apps.views import HomeTemplateView, RegisterFormView, LoginFormView, LogoutView, ProfileTemplateView, \
    ProfileEditFormView, InternetFormView

urlpatterns = [
    path("" , HomeTemplateView.as_view() , name = "home"),
    path("register" , RegisterFormView.as_view() , name = "register"),
    path("login" , LoginFormView.as_view() , name = "login"),
    path("logout" , LogoutView.as_view() , name = "logout"),
    path("profile" , ProfileTemplateView.as_view() , name = "profile"),
    path("profile-edit" , ProfileEditFormView.as_view() , name = "profile-edit"),
    path("internet" , InternetFormView.as_view() , name = "internet"),
]