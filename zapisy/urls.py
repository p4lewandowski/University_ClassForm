from zapisy import views
from django.urls import path

urlpatterns = [
    path('', views.sign_for_course),
    path('status', views.signing_process)
]