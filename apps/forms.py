from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, Form, forms

from apps.models import User, Internet


# class RegisterForm(ModelForm):
#     confirm_password = CharField(max_length=30)
#
#     class Meta:
#         model = User
#         fields = ["first_name" , "last_name" , "email" , "username" , "phone" , "mobile" , "address" , "password" , "confirm_password"]
#
#     def clean_email(self):
#         email = self.clean().get('email')
#         if not email.endswith('@gamil.com'):
#             raise ValidationError("Invalid Your Email")
#         return email
#
#     def clean_password(self):
#         password = self.clean().get('password')
#         if len(password) < 4:
#             raise ValidationError("Your Password is short")
#         clean_data = super().clean()
#         confirm_password = self.data.get("confirm_password")
#         if confirm_password != password:
#             raise ValidationError("Confirm password and Password is not match")
#         return make_password(clean_data.get("password"))



class RegisterForm(ModelForm):
    confirm_password = CharField(max_length=30)

    class Meta:
        model = User
        fields = "first_name", "last_name", "email", "username", "phone", "mobile", "address", "password", "confirm_password"

    def clean_email(self):
        email = self.clean().get("email")
        if not email.endswith('@gmail.com'):
            raise ValidationError("Your Password is short")
        return email
    def clean_password(self):
        password = self.clean().get("password")
        if len(password) < 4:
            raise ValidationError("Your Password is short")
        clean_data = super().clean()
        confirm_password = self.data.get("confirm_password")
        if confirm_password != password:
            raise ValidationError("Password and Confirm password not match")
        return make_password(clean_data.get("password"))


# class LoginForm(Form):
#     username = CharField(max_length=255)
#     password = CharField(max_length=255)
#
#
#     def cleand(self):
#         data = super().clean()
#         username = data.get('username')
#         password = data.get('password')
#         self.find_user = User.objects.filter(username=username).first()
#         if not self.find_user:
#             raise ValidationError("Not found User")
#         if check_password(password , self.find_user.password):
#             raise ValidationError("Your password wrong")
#         return data


class LoginForm(Form):
    username = CharField(max_length=50)
    password = CharField(max_length=50)


    def clean(self):
        data = super().clean()
        username = data.get('username')
        password = data.get('password')
        self.find_user = User.objects.filter(username=username).first()
        if not self.find_user:
            raise ValidationError("Not Found account")
        if not check_password(password,self.find_user.password):
            raise ValidationError("Your wrong password")
        return data


class ProfilEditForm(Form):
    fullname=CharField(max_length=255)
    email=CharField(max_length=255)
    phone=CharField(max_length=12)
    mobile=CharField(max_length=12)
    address=CharField(max_length=255)



class InternetForm(ModelForm):
    class Meta:
        model = Internet
        fields = ['instagram_name', 'website_name', 'twiiter_name', 'github_name', 'facebook_name']

    def clean_instagram_name(self):
        return self.cleaned_data.get("instagram_name")





