from django.urls import path, include

from Account.views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name="login"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('logout/', logout_user, name="logout"),
    path('verification_email/<str:code>', email_verification, name="email_verification" )
]