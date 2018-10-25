from zapisy import views
from django.urls import path

urlpatterns = [
    path('szukaj/', views.search_form),
    path('wyniki/', views.search),
]