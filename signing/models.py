from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Lecturer(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return "Lecturer "+ self.name+ " " + self.surname

    class Meta:
        verbose_name_plural = "Lecturers"

class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    index = models.IntegerField(unique=True, blank=True, null=True, default=None)

    def __str__(self):
        return "Student " + self.name + " " + self.surname + ' ' + str(self.index)


    class Meta:
        verbose_name_plural = "Students"

class Course(models.Model):
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, blank=True)
    students = models.ManyToManyField(Student, blank=True)
    slug_name = slugify(name)
    examination = models.CharField(max_length=1)

    def __str__(self):
        if self.examination == 'E':
            return self.name + " - egzamin"
        elif self.examination == 'Z':
            return self.name + " - zaliczenie"
        else:
            return self.name

    class Meta:
        verbose_name_plural = "Courses"