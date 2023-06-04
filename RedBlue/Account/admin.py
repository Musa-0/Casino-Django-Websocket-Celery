from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Account.models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    #fields = ('email', 'username', 'password1', 'password2')
    list_display = ('id','username','email', 'date_joined','last_login', 'is_admin','is_staff')
    search_fields = ('email', 'username')#строка поиска делается лишь по имэтлу и имени
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()#
    list_filter = ()#
    fieldsets = ()#отключаем обязательную фильтрацию
admin.site.register(Account, AccountAdmin)
