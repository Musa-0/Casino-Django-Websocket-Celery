from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from Account.models import CodeVerefication
from Core.models import Stavka


# Register your models here.
class StavkaAdmin(ModelAdmin):
    #fields = ('email', 'username', 'password1', 'password2')
    list_display = ('id','owner_id','color', 'quantity')
    search_fields = ('owner_id', 'color')#строка поиска делается лишь по имэтлу и имени
    readonly_fields = ('id',)
    filter_horizontal = ()#
    list_filter = ()#
    fieldsets = ()#отключаем обязательную фильтрацию
admin.site.register(Stavka, StavkaAdmin)

class CodeVereficationAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'code', 'datetime')
admin.site.register(CodeVerefication, CodeVereficationAdmin)
