from django.db import models

# Create your models here.

class Nauczyciel(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return "Nauczyciel "+ self.name+ " " + self.surname

    class Meta:
        verbose_name_plural = "nauczyciele"

class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return "Student "+ self.name+ " " + self.surname

    class Meta:
        verbose_name_plural = "studenci"

class Przedmiot(models.Model):
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Nauczyciel, on_delete=models.CASCADE, blank=True)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "przedmioty"