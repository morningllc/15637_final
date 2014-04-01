from django import forms

from django.contrib.auth.models import User
from models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 50,
    						   label='username',
                               widget=forms.TextInput(
                                attrs={'label':'username',
                                       'class':'form-control',
                                       'placeholder':'Username',
                                       'required':True,
                                       'autofocus':True}))
    firstname = forms.CharField(max_length = 50,
                               label='firstname',
                               widget=forms.TextInput(
                                attrs={'label':'email',
                                       'class':'form-control',
                                       'placeholder':'First Name',
                                       'required':True}))
    lastname = forms.CharField(max_length = 50,
                               label='lastname',
                               widget=forms.TextInput(
                                attrs={'label':'email',
                                       'class':'form-control',
                                       'placeholder':'Last Name',
                                       'required':True}))
    email=forms.CharField(max_length=70,
    					  label='email',
                           widget=forms.EmailInput(
                            attrs={'label':'email',
                                   'class':'form-control',
                                   'placeholder':'E-mail',
                                   'required':True}))
    password1 = forms.CharField(max_length = 200, 
                                label='Password', 
                                widget = forms.PasswordInput(
                                attrs={'label':'password1',
                                   'class':'form-control',
                                   'placeholder':'Password',
                                   'required':True}))
    password2 = forms.CharField(max_length = 200, 
                                label='Confirm password',  
                                widget = forms.PasswordInput(
                                attrs={'label':'password2',
                                   'class':'form-control',
                                   'placeholder':'Confirm Password',
                                   'required':True}))

    def clean(self):
    	cleaned_data = super(RegistrationForm,self).clean()

    	# if not '@' in cleaned_data.get('email'):
    	# 	raise forms.ValidationError("Email address in invailid.")
    	password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        return cleaned_data

    def clean_username(self):
	    username = self.cleaned_data.get('username')
	    if User.objects.filter(username__exact=username):
	        raise forms.ValidationError("Username is already taken.")

	    return username