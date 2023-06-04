import random

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Account.email_worker.email_works import email_send_code_checker, randomword
from Account.forms import LoginUserForm, RegisterUserForm
from Account.models import CodeVerefication


# Create your views here.
class LoginUser(LoginView):#класс входа пользователя
    form_class = LoginUserForm
    template_name = 'account/login.html'

    def get_success_url(self):#переправляет нас на главную страницу в случае успешного входа в систему
        return reverse_lazy('index')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        user = form.save()

        code = randomword(15)
        email_send_code_checker(user.email, code)
        CodeVerefication.objects.create(user=user, code=code)

        return render(self.request, "account/email_confirm.html")


def logout_user(request):
    logout(request)
    return redirect('login')

def email_verification(request, code):
    code_accounts = CodeVerefication.objects.all()
    for account in code_accounts:
        if account.code==code:
            user = account.user
            user.is_active=True
            user.save()
            account.delete()
            login(request, user)
            break
    return render(request, "index.html")

