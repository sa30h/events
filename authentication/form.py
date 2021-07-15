from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import authenticate,login


class RegistrationForm(UserCreationForm):
	class Meta:
		model=User
		fields=('username','email')


class UserLoginForm(forms.ModelForm):
	password=forms.CharField(label='Password',widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=('username','password')

	def clean(self):
		if self.is_valid():
			username=self.cleaned_data['username']
			password=self.cleaned_data['password']
			if not authenticate(username=username,password=password):
				raise forms.ValidationError("Invalid Creadentials")

class Taskform(forms.ModelForm):
	class Meta:
		model=EventTask
		fields='__all__'

class Taskupdatesform(forms.ModelForm):
	class Meta:
		model=TaskUpdates
		fields='__all__'

class Commentform(forms.ModelForm):
	class Meta:
		model=TaskComment
		fields='__all__'

