from django.contrib import admin

# Register your models here.
from .models import Student, Nauczyciel, Przedmiot

admin.site.register(Student)
admin.site.register(Nauczyciel)
admin.site.register(Przedmiot)
