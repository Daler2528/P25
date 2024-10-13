from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, TextChoices, ForeignKey, CASCADE


class User(AbstractUser):
    class JobChoicesField(TextChoices):
        FULL_STACK_DEVELOPEE = "full stack developer" , "Full Stack Developer"
        DESIGNER = "designer" , "Designer"
        FLATER = "flater" , "Flater"
    phone = CharField(max_length=12)
    mobile = CharField(max_length=12)
    address = CharField(max_length=255)
    job = CharField(max_length=255 , choices=JobChoicesField , default=JobChoicesField.FULL_STACK_DEVELOPEE)


    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


class Internet(models.Model):
    instagram_name = CharField(max_length=255 , default="-" , blank=True, null=True)
    website_name = CharField(max_length=255 , default="-" ,blank=True, null=True)
    twiiter_name = CharField(max_length=255 ,default="-" , blank=True, null=True)
    github_name = CharField(max_length=255 , default="-" , blank=True, null=True)
    facebook_name = CharField(max_length=255 , default="-" , blank=True, null=True)
    user_id = models.ForeignKey("apps.User", on_delete=models.CASCADE , related_name="internet_profiles")





