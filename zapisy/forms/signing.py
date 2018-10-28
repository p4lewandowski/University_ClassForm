from django import forms

class SigningForm(forms.Form):
    subject = forms.CharField(label="Nazwa przedmiotu:", max_length=100, required=True)
    student_name = forms.CharField(label="Imię studenta:", max_length=50, required=True)
    student_surname = forms.CharField(label="Nazwisko studenta:", max_length=50, required=True)