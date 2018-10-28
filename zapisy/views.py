from django.shortcuts import render_to_response, render
from zapisy.models import Przedmiot,  Nauczyciel, Student
from .forms.signing import SigningForm
import operator

# Create your views here.


def signing_process(request):
    przedmioty = Przedmiot.objects.all()
    form = SigningForm()

    if request.method == "POST":

        form = SigningForm(request.POST)
        if form.is_valid():

            course_name = form.data['subject']
            if Przedmiot.objects.filter(name__exact=course_name):

                course = Przedmiot.objects.get(name=course_name)
                temp, created = course.students.get_or_create(name=form.data['student_name'],
                                                              surname=form.data['student_surname'])

                if not created:
                    return render(request, 'sign_with_list.html',
                                              {'form': form, 'przedmioty': przedmioty, 'existed': True})

                return render(request,'sign_with_list.html',
                                          {'form': form,'przedmioty': przedmioty,  'signed': True})
            else:
                return render(request,'sign_with_list.html',
                                          {'form': form,'przedmioty': przedmioty,  'no_course': True})
        else:
             return render(request,'sign_with_list.html',
                                      {'form': form,'przedmioty': przedmioty,  'error': True})


    return render(request, 'sign_with_list.html', {'przedmioty': przedmioty, 'form': form})



def sign_for_course(request):
  return render_to_response('sign_for_course.html')

def show_courses(request):
  przedmioty = Przedmiot.objects.all()

  return render_to_response('all_courses.html',
                            {'przedmioty': przedmioty})

def show_lecturers(request):
  nauczyciele = Nauczyciel.objects.all()
  nauczyciele = sorted(nauczyciele, key=operator.attrgetter('surname'))

  return render_to_response('all_lecturers.html',
                            {'nauczyciele': nauczyciele})