from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path
from signing.models import Student, Lecturer, Course
from signing import views
# Register your models here.

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Course)