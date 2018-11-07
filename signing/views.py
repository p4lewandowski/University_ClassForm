from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from signing.models import Course,  Lecturer, Student
from .forms.signing_form import SigningForm
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json
import operator
import requests

# Create your views here.


def sign_for_courses(request):
    courses = Course.objects.all()
    return render_to_response('sign_for_courses.html',
                              {'courses': courses})

def signing_process(request, course_name=None):

    form = SigningForm()
    if request.method == "POST":

        form = SigningForm(request.POST)
        if form.is_valid():

            course = Course.objects.get(name=course_name)
            temp, created = course.students.get_or_create(name=form.data['student_name'],
                                                          surname=form.data['student_surname'])
            if not created:
                return render(request, 'sign_for_course.html',
                              {'form': form, 'existed': True, 'name': course_name})

            return render(request, 'sign_for_course.html',
                                          {'form': form, 'signed': True, 'name': course_name})

    return render(request, 'sign_for_course.html', {'form': form, 'name': course_name})


def show_courses(request):
  courses = Course.objects.all()

  return render_to_response('show_courses.html',
                            {'courses': courses})

def show_lecturers(request):
  lecturers = Lecturer.objects.all()
  lecturers = sorted(lecturers, key=operator.attrgetter('surname'))

  return render_to_response('show_lecturers.html',
                            {'lecturers': lecturers})


def database_management(request):

    if request.method == "POST":
        data = {
            'students': serializers.serialize('json', Student.objects.all(), use_natural_foreign_keys=True),
            'lecturers': serializers.serialize('json', Lecturer.objects.all(), use_natural_foreign_keys=True),
            'courses': serializers.serialize('json', Course.objects.all(), use_natural_foreign_keys=True),
        }

        with open('db_backup', 'w') as file:
            file.write(data)

    return render_to_response('import_export.html')

def export_data(request):

    data = {
        'students': serializers.serialize('json', Student.objects.all(), use_natural_foreign_keys=True),
        'lecturers': serializers.serialize('json', Lecturer.objects.all(), use_natural_foreign_keys=True),
        'courses': serializers.serialize('json', Course.objects.all(), use_natural_foreign_keys=True),
    }
    return JsonResponse(data)


# @csrf_exempt
# def import_data(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#
#         for key, value in data.items():
#             deserialized = serializers.deserialize('json', value, ignorenonexistent=True)
#             [obj.save() for obj in deserialized]
#
#     return HttpResponse('Success')
#
#
# def delete_all(request):
#     Student.objects.all().delete()
#     Lecturer.objects.all().delete()
#     Course.objects.all().delete()
#
#     return HttpResponse('Success')