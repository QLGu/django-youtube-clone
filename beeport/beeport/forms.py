from django import forms
from management.models import Users

class RegisterForm(forms.ModelForm):
	name = forms.CharField(label='Adiniz')
	surname = forms.CharField(label='Soyadiniz')
	email = forms.CharField(label='E-Mail')
	password = forms.CharField(label='Sifreniz')
	passagain = forms.CharField(label='Sifrenizi Tekrar Giriniz')
	profile_name = forms.CharField(label='Profil Adi',required=False)
	image_url = forms.URLField(label='Profil Resmi',required=False)
	social_id = forms.CharField(label='Sosyal Medya URL\'i',required=False)
	social_type = forms.IntegerField(label='Sosyal Medya Tipi')
	
	class Meta:
		model=Users

	'''
	def __init__(self, user, *args, **kwargs):
	    super(RegisterForm, self).__init__(*args, **kwargs)
	    self.fields['profile_name'].widget = forms.HiddenInput()
	    self.fields['image_url'].widget = forms.HiddenInput()
	    self.fields['social_id'].widget = forms.HiddenInput()
		social_type = forms.IntegerField(label='Sosyal Medya Tipi',required=False,widget=forms.HiddenInput())
	'''