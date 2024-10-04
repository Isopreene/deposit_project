from django.contrib import admin
from django.urls import path
from depositapp.views import DepositView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("deposit/", DepositView.as_view(), name="deposit")
]