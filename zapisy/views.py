from django.shortcuts import render_to_response
from zapisy.models import Przedmiot,  Nauczyciel, Student
import operator

# Create your views here.

def sign_for_course(request):
  return render_to_response('sign_for_course.html')

def signing_process(request):
    if request.GET['nazwa_przedmiotu'] and request.GET['imie'] and request.GET['nazwisko']:
        if Przedmiot.objects.filter(name__exact=request.GET['nazwa_przedmiotu']):
            course = Przedmiot.objects.filter(name__exact=request.GET['nazwa_przedmiotu'])
            student = Student.objects.filter(name__exact=request.GET['imie'], surname__exact=request.GET['nazwisko'])
            if student:
                Przedmiot.students.add(student)
            else:
                
        else:
            return render_to_response('sign_for_course.html',
                                      {'no_course': True})
    else:
        return render_to_response('sign_for_course.html',
                                  {'error': True})

def show_courses(request):
  przedmioty = Przedmiot.objects.all()

  return render_to_response('all_courses.html',
                            {'przedmioty': przedmioty})

def show_lecturers(request):
  nauczyciele = Nauczyciel.objects.all()
  nauczyciele = sorted(nauczyciele, key=operator.attrgetter('surname'))

  return render_to_response('all_lecturers.html',
                            {'nauczyciele': nauczyciele})