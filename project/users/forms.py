from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.admin import widgets

class RegisterForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget())

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices = GENDER_CHOICES, widget=forms.Select())

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'gender',
            'birth_date',
        ]
        labels = {
            'email':'Email',
            'first_name':'First Name',
            'last_name':'Last Name',
            'gender':'Gender',
            'birth_date':'Birth Date'
        }
