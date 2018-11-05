from signing import views
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('courses/', views.show_courses, name='courses_list'),
    path('lecturers/', views.show_lecturers, name='lecturers_list'),
    path('sign/', views.sign_for_courses, name='signing_list'),
    url(r'^sign/(?P<course_name>[\w-]+)/$', views.signing_process, name='course'),
    path('nav/', TemplateView.as_view(template_name='base.html'))
]