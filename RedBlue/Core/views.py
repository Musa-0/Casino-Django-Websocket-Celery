from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from Account.email_worker.email_works import email_send_code_checker
from Account.forms import LoginUserForm, RegisterUserForm
from Account.models import Account
from Core.main_program import time_round
from Core.models import Stavka


# Create your views here.
def index(request):
    return render(request, "index.html")


def get_time(request):
    return JsonResponse({"time":time_round()})