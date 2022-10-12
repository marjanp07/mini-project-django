from django import forms
from core.models import *
from django.forms.widgets import SelectMultiple,FileInput, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,TimeInput

# <input type="email" class="form-control" id="inputEmailAddress" placeholder="example@user.com">
# <select class="form-select" id="inputSelectCountry" aria-label="Default select example">
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'email': TextInput(attrs={'class': 'form-control','type':'email', 'placeholder': 'example@user.com','id':'email','name':'email'}),
            'password': TextInput(attrs={'class': 'form-control','type':'password', 'placeholder': '****************','id':'password','name':'password'})
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = peoples
        fields = '__all__'
        widgets = {
            'person_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'person_name','name':'person_name'}),
            'place': TextInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'place','name':'place'}),
            'state': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'district': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'district','name':'district'}),
            'police_station_range': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'district','name':'district'}),
            'post': TextInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'post','name':'post'}),
            'adhar_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'adhar_number','name':'adhar_number'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'phone_number','name':'phone_number'}),
            'photo': FileInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'photo','name':'photo'})
        }



class complaintForm(forms.ModelForm):
    class Meta:
        model = complaints
        fields = '__all__'
        widgets = {
            'user': Select(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'person_name','name':'person_name'}),
            'police_station': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'complaint_discription': Textarea(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'post','name':'post'}),
            'document_feild': FileInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'photo','name':'photo'})
        }