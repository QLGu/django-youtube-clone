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
	class Meta:
		model = UserProfile
		exclude=('user',)

class AddVideoForm(forms.ModelForm):
	class Meta:
		model = Videos
		exclude = ['path_720p', 'path_480p', 'path_360p', 'path_240p', 'publisher', \
		'upload_date', 'like_count', 'comment_count', 'watch_count', 'video_duration']

	def __init__(self, *args, **kwargs):
		super(AddVideoForm, self).__init__(*args, **kwargs)
		self.fields['category'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}
		)

		self.fields['name'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}
		)

		self.fields['resource'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}
		)

		self.fields['sharing_permissions'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}
		)

		self.fields['path'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}
			)
		self.fields['video_image'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}
			)
		self.fields['desc'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}
			)
		self.fields['tags'].widget.attrs.update(
			{
			'class': "form-control",
			'style': "margin:10px;",
			}

		)


	"""
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
	"""