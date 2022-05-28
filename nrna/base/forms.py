from tkinter import Widget
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from .models import NewUser

class UserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields=UserCreationForm.Meta.fields + ('email','username','first_name','country','address','year_in_school','about','avatar')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        # self.fields['email','user_name','first_name','country','address','year_in_school','about'].widget.attrs.update({'class': 'form-control'})
        # self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['year_in_school'].widget.attrs.update({'class': 'form-control'})
        self.fields['about'].widget.attrs.update({'class': 'form-control'})

        
        