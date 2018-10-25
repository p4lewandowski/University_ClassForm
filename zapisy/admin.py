from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path
from .models import Student, Nauczyciel, Przedmiot
from zapisy import views
# Register your models here.

admin.site.register(Student)
admin.site.register(Nauczyciel)
admin.site.register(Przedmiot)
