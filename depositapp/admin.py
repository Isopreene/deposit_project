from django.contrib import admin

from depositapp.models import DepositModel

# Register your models here.

@admin.register(DepositModel)
class DepositModelAdmin(admin.ModelAdmin):
    pass