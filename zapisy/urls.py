from zapisy import views
from django.urls import path

urlpatterns = [
    path('', views.signing_process),
]