# -*- coding: utf-8 -*-
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

class ProfileForm(forms.ModelForm):
	CHOICES = ((1,'Erkek'),(2,'Kadın'),)
	name=forms.CharField(label='Adiniz')
	surname=forms.CharField(label='Soyadiniz')
	birthdate=forms.DateField(label='Doğum Tarihiniz')
	gender=forms.IntegerField(label='Cinsiyet',widget=forms.Select(choices=CHOICES))
	about_me=forms.CharField(label='Hakkimda',widget=forms.Textarea())

	class Meta:
		model = Users
		exclude=('image_url','profile_name','social_id','social_type','email','password')

class AddVideoForm(forms.ModelForm):
	CHOICES= (
	(1, 'Herkese Açık'),
	(2, 'Video Linkine Sahip Olan Herkese Açık'),
	(3, 'Sadece Bana Açık'),
	)
	video_image=forms.ImageField(label='Video Görseli')
	name = forms.CharField(label='Video Adi')
	category = forms.ModelChoiceField(label='Kategori Seçiniz',queryset=Categories.objects.all())
	desc=forms.CharField(label='Açıklama',widget=forms.Textarea())
	tags = forms.CharField(label='Anahtar Kelimeler')
	sharing_permissions=forms.IntegerField(label='Gizlilik',widget=forms.Select(choices=CHOICES))
    
	class Meta:
		model=Videos
		exclude=('resource','path','path_240p','path_360p','path_480p','path_720p','publisher','upload_date')

	def save(self, force_insert=False, force_update=False, commit=True):
	    m = super(AddVideoForm, self).save(commit=False)
	    # do custom stuff
	    if commit:
	        m.save()
	    return m