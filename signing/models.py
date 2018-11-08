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

    def __str__(self):
        return "Student " + self.name + " " + self.surname

    class Meta:
        verbose_name_plural = "Students"

class Course(models.Model):
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, blank=True)
    students = models.ManyToManyField(Student, blank=True)
    slug_name = slugify(name)
    examination = models.CharField(max_length=1, default='Z', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Courses"