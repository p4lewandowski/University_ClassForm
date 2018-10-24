from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render_to_response
import datetime


def hello_template(request):
  today = datetime.datetime.today().strftime('%d, %b %Y')
  return render_to_response('hello.html',{ 'teraz': today})


def hello(request):
    return HttpResponse("Hello World!")


def hello2(request):
  today = datetime.datetime.today().strftime('%d, %b %Y')
  t = '<html><body>Witaj! Dziś mamy {{ teraz }} </body></html>'
  szablon = Template(t)
  html = szablon.render(Context({ 'teraz': today}))
  return HttpResponse(html)
