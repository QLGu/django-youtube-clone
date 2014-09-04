#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from management.models import *
from django import forms
 
class VideoClass(admin.ModelAdmin):
  formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

  class Media:
    		js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

  list_display = ('resource', 'category', 'name')


class MesajClass(admin.ModelAdmin):
    verbose_name_plural = 'Mesajlar'
    can_delete = False
    list_display = ('status','reciever_id', 'sender_id', 'sent_date')

class Comments(admin.ModelAdmin):
  verbose_name_plural = 'Video Yorumları'
  list_display=('commenter_id','video_id','comment','comment_date')

class EtkinlikClass(admin.ModelAdmin):
  verbose_name_plural = 'Etkinlikler'
formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
 
class Media:
    	js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

list_display = ('event_image', 'event_name', 'event_price','event_date')

class StaticClass(admin.ModelAdmin):
  verbose_name_plural = 'Statik Sayfalar'
formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

list_display = ('header', 'created_date','created_user')
def save_model():
    if getattr(obj, 'created_user', None) is None:
      obj.created_user = request.user
    obj.save()

class Media:
    		js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    	

admin.site.register(Categories)
admin.site.register(User_Liked_Videos)
admin.site.register(User_Events)
admin.site.register(Event_Stream_Informations)
admin.site.register(User_Playlist)
admin.site.register(User_Subscriptions)
admin.site.register(Playlist_Videos)
admin.site.register(Messages,MesajClass)
admin.site.register(Videos,VideoClass)
admin.site.register(UserProfile)
admin.site.register(Video_Comments,Comments)
admin.site.register(Static_Pages,StaticClass)
admin.site.register(Events,EtkinlikClass)