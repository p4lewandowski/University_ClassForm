from django import forms

class SigningForm(forms.Form):
    student_name = forms.CharField(label="Imię studenta:", max_length=50, required=True)
    student_surname = forms.CharField(label="Nazwisko studenta:", max_length=50, required=True)
    student_index = forms.IntegerField(label="Indeks studenta:", required=True)