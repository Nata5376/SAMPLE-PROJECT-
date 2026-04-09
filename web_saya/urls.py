from django.contrib import admin
from django.urls import path
from web_saya import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.halaman_utama),
]