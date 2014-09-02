from django import forms
from management.models import *

class RegisterForm(forms.ModelForm):
	name = forms.CharField(label='Adiniz')
	surname = forms.CharField(label='Soyadiniz')
	email = forms.CharField(label='E-Mail',widget=forms.EmailInput())
	password = forms.CharField(label='Sifreniz',widget=forms.PasswordInput())
	passagain = forms.CharField(label='Sifrenizi Tekrar Giriniz',widget=forms.PasswordInput())
	
	class Meta:
		model=Users
		exclude=('image_url','about_me','birthdate','image_url','profile_name','social_id','social_type')

	'''
	def __init__(self, user, *args, **kwargs):
	    super(RegisterForm, self).__init__(*args, **kwargs)
	    self.fields['profile_name'].widget = forms.HiddenInput()
	    self.fields['image_url'].widget = forms.HiddenInput()
	    self.fields['social_id'].widget = forms.HiddenInput()
		social_type = forms.IntegerField(label='Sosyal Medya Tipi',required=False,widget=forms.HiddenInput())
	'''
