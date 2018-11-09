from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from signing.models import Course,  Lecturer, Student
from .forms.signing_form import SigningForm
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json
import operator
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


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

            # If question was asked what to do with index
            if form.data['confirmation']=='1':
                # If update
                if form.data['assign']=='1':
                    student = course.students.get(name=form.data['student_name'],
                                                  surname=form.data['student_surname'])
                    setattr(student, 'index', form.data['student_index'])
                    student.save()
                    return render(request, 'sign_for_course.html',
                                  {'form': form, 'signed': True, 'name': course_name, 'old':True})

                # if create new
                else:
                    course.students.create(name=form.data['student_name'],
                                           surname=form.data['student_surname'],
                                           index=form.data['student_index'])
                    return render(request, 'sign_for_course.html',
                                  {'form': form, 'signed': True, 'name': course_name, 'new':True})


            # If index is used
            try:
                # Check if person with such a index exists
                course.students.get(index=form.data['student_index'])
                return render(request, 'sign_for_course.html',
                              {'form': form, 'existed_index': True, 'name': course_name})

            except ObjectDoesNotExist:

                # If name and surname is used - and no index is present - ask what to do
                try:
                    student = course.students.get(name=form.data['student_name'],
                                                            surname=form.data['student_surname'])
                    # Does it have index
                    if getattr(student, 'index'):
                        raise ObjectDoesNotExist

                    # If not ask if rewrite required or new
                    return render(request, 'sign_for_course.html',
                                  {'form': form, 'found_identity':
                                      True, 'name': course_name,
                                  'student_name': form.data['student_name'],
                                   'student_surname': form.data['student_surname'],
                                   'student_index': form.data['student_index']})


                # If no index or identity present
                except ObjectDoesNotExist:

                    course.students.create(name=form.data['student_name'],
                                            surname=form.data['student_surname'],
                                            index=form.data['student_index'])

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

@csrf_exempt
def database_management(request):

    # Import
    if request.method == 'POST' and request.FILES['myfile']:

        ## Save a file and open it
        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # fs.save(myfile.name, myfile)
        #
        # with open('media/'+myfile.name, "r") as fin:
        #     data = json.loads(fin.read())

        # Only opening and reading in the file
        data = json.loads(request.FILES['myfile'].read())

        # Deleting previous database
        Student.objects.all().delete()
        Lecturer.objects.all().delete()
        Course.objects.all().delete()

        for key, value in data.items():
            deserialized = serializers.deserialize('json', value, ignorenonexistent=True)
            [obj.save() for obj in deserialized]

    return render_to_response('database_import_export.html')

def database_export_old(request):

    data = {
        'students': serializers.serialize('json', Student.objects.all(), use_natural_foreign_keys=True,
                                          fields=('name', 'surname')),
        'lecturers': serializers.serialize('json', Lecturer.objects.all(), use_natural_foreign_keys=True),
        'courses': serializers.serialize('json', Course.objects.all(), use_natural_foreign_keys=True),
    }
    data_string = json.dumps(data)

    response = HttpResponse(data_string, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=export.json'

    return response

def database_export_new(request):

    data = {
        'students': serializers.serialize('json', Student.objects.all(), use_natural_foreign_keys=True),
        'lecturers': serializers.serialize('json', Lecturer.objects.all(), use_natural_foreign_keys=True),
        'courses': serializers.serialize('json', Course.objects.all(), use_natural_foreign_keys=True),
    }
    data_string = json.dumps(data)

    response = HttpResponse(data_string, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=export.json'

    return response

def export_data(request):

    data = {
        'students': serializers.serialize('json', Student.objects.all(), use_natural_foreign_keys=True),
        'lecturers': serializers.serialize('json', Lecturer.objects.all(), use_natural_foreign_keys=True),
        'courses': serializers.serialize('json', Course.objects.all(), use_natural_foreign_keys=True),
    }
    return JsonResponse(data)
