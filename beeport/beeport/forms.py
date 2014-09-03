# -*- coding: utf-8 -*-
from django import forms
from management.models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender', 'birthdate')

class ProfileForm(forms.ModelForm):
	CHOICES = ((1,'Erkek'),(2,'Kadın'),)
	name=forms.CharField(label='Adiniz')
	surname=forms.CharField(label='Soyadiniz')
	birthdate=forms.DateField(label='Doğum Tarihiniz')
	gender=forms.IntegerField(label='Cinsiyet',widget=forms.Select(choices=CHOICES))
	about_me=forms.CharField(label='Hakkimda',widget=forms.Textarea())

	class Meta:
		model = User
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