from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
import time
from django.contrib import messages


class CreateUserForm(UserCreationForm):
  username = forms.CharField(required=True, max_length=30, ) 
  email = forms.EmailField(required=True)
  first_name = forms.CharField(required=True, max_length=50)
  last_name = forms.CharField(required=True, max_length=50)
  

  
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2',]
  #function to display errors
  def clean(self):
          cleaned_data=super().clean()
          password1 = self.cleaned_data.get('password1')
          password2 = self.cleaned_data.get('password2')

          if User.objects.filter(username=cleaned_data["username"]).exists():
            raise ValidationError("This username is taken, please try another one")

          elif password1 != password2:
            raise forms.ValidationError("2 password fields do not match")

          elif len(password1) < 8 or len(password2) < 8:
            raise forms.ValidationError("Passwords must be at least 8 characters long")

          








          
