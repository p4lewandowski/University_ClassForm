from django.shortcuts import render_to_response, render
from signing.models import Course,  Lecturer, Student
from .forms.signing_form import SigningForm
import operator
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