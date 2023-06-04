from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):#переделаем базовую модель пользователя
    email = models.EmailField(verbose_name="email",max_length=60, unique=True)#сделаем почту уникальной
    username = models.CharField(max_length=30,unique=True)#уникальный адрес почты
    balance = models.IntegerField(default=0, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # нужен для того чтобы его аккаунт входил по email и чтобы его обозначение тоже было в виде email
    REQUIRED_FIELDS = ['username']  # список имен полей, которые будут запрашиваться при создании пользователя с помощью команды управления createsuperuser

    def __str__(self):
        return self.username

class CodeVerefication(models.Model):
    code = models.CharField(max_length=1000)
    user = models.OneToOneField('Account',on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now=True)

