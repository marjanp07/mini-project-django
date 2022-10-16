from django import forms
from core.models import *
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,TimeInput,DateInput

# <input type="email" class="form-control" id="inputEmailAddress" placeholder="example@user.com">
# <select class="form-select" id="inputSelectCountry" aria-label="Default select example">
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': TextInput(attrs={'class': 'form-control','type':'email', 'placeholder': 'example@user.com','id':'username','name':'username'}),
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
        fields = ('police_station','document_feild','complaint_discription')
        widgets = {
            # 'user': Select(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'person_name','name':'person_name'}),
            'police_station': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'complaint_discription': Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe complaint','id':'post','name':'post'}),
            'document_feild': FileInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'photo','name':'photo'})
        }


class complaintupdateForm(forms.ModelForm):
    class Meta:
        model = complaint_updates
        fields = ('comment',)
        widgets = {
            # 'user': Select(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'person_name','name':'person_name'}),
            # 'status': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'post','name':'post'}),
        }

class policecomplaintupdateForm(forms.ModelForm):
    class Meta:
        model = complaint_updates
        fields = ('comment','status')
        widgets = {
            # 'user': Select(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'person_name','name':'person_name'}),
            'status': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'post','name':'post'}),
        }



  

class firstatusForm(forms.ModelForm):
    class Meta:
        model = fir_status_report
        fields = ('fir','current_status')
        widgets = {
            # 'user': Select(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'person_name','name':'person_name'}),
            'status': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'post','name':'post'}),
        }  
        

class FirCreateForm(forms.ModelForm):
    class Meta:
        model = fir_details
        fields = ('document_feild','fir','case_type','hearing_date','decision_date','court_no_and_judge','status')
        widgets = {
            'document_feild': FileInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'photo','name':'photo'}),
            'fir': Textarea(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'post','name':'post'}),
            'case_type': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'status': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'hearing_date': DateInput(attrs={'class': 'form-control', 'type':'date','placeholder': 'example@user.com','id':'state','name':'state'}),
            'decision_date': DateInput(attrs={'class': 'form-control','type':'date', 'placeholder': 'example@user.com','id':'state','name':'state'}),
            'court_no_and_judge': TextInput(attrs={'class': 'form-control', 'placeholder': 'example@user.com','id':'place','name':'place'}),

        }

class FirrejectForm(forms.ModelForm):
    class Meta:
        model = fir_details
        fields = ('status',)
        widgets = {
            'status': Select(attrs={'class': 'form-select', 'placeholder': 'example@user.com','id':'state','name':'state'}),
        }