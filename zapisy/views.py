from django.shortcuts import render_to_response
from zapisy.models import Przedmiot, Student, Nauczyciel

# Create your views here.

def search_form(request):
  return render_to_response('search_form.html')

def search(request):
  if 'nazwa_przedmiotu' in request.GET and request.GET['nazwa_przedmiotu']:
    query = request.GET['nazwa_przedmiotu']
    przedmioty = Przedmiot.objects.filter(name__icontains=query)
    return render_to_response('results_form.html',
      {'przedmioty': przedmioty, 'query': query})
  else:
    return render_to_response('noresults_form.html',
      {'error': True})

def show_courses(request):
  przedmioty = Przedmiot.objects.all()

  return render_to_response('all_courses.html',
                            {'przedmioty': przedmioty})