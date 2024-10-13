from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from apps.forms import RegisterForm, LoginForm, ProfilEditForm, InternetForm
from apps.models import User


class HomeTemplateView(TemplateView):
    template_name = "apps/home.html"



class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = "apps/register.html"
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def form_invalid(self, form):
        return super().form_invalid(form)


# class LoginFormView(FormView):
#     form_class = LoginForm
#     template_name = "apps/login.html"
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         if form.is_valid():
#             user = form.find_user
#             login(self.request, user)
#             return super().form_invalid(form)

class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'apps/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            user = form.find_user
            login(self.request , user)
            return super().form_valid(form)


class LogoutView(View):
    def post(self , request):
        logout(request)
        return redirect('login')


class ProfileTemplateView(TemplateView):
    template_name = "apps/profile.html"


class ProfileEditFormView(FormView):
    form_class = ProfilEditForm
    template_name = "apps/profil-edit.html"
    success_url = reverse_lazy("profile")


    def form_valid(self, form):
        user = self.request.user
        form_data = form.cleaned_data
        form_data['first_name'] = form_data.get("fullname").split()[0]
        form_data['last_name'] = form_data.get("fullname").split()[1]
        del form_data['fullname']
        user = User.objects.filter(pk=user.pk)
        user.update(**form.cleaned_data)
        return super().form_valid(form)


# class InternetFormView(FormView):
#     form_class = InternetForm
#     template_name = "apps/internet.html"
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         if form.is_valid():
#             return super().form_valid(form)


class InternetFormView(FormView):
    form_class = InternetForm
    template_name = "apps/internet.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Internet ob'ektini saqlashdan oldin user_id ni qo'shamiz
        internet = form.save(commit=False)  # Modelni hozircha saqlamaymiz
        internet.user_id = self.request.user  # Foydalanuvchi bilan bog'laymiz
        internet.save()  # Modelni saqlaymiz
        return super().form_valid(form)





