from django.contrib import admin
from management.models import *
from django import forms
 
class VideoClass(admin.ModelAdmin):
	formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

  	class Media:
    		js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

list_display = ('resource', 'category', 'name')

class KullaniciClass(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')

class EtkinlikClass(admin.ModelAdmin):
	formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

  	class Media:
    		js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

list_display = ('event_image', 'event_name', 'event_price','event_date')

class StaticClass(admin.ModelAdmin):
	formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

list_display = ('header', 'created_date','created_user')
def save_model():
    if getattr(obj, 'created_user', None) is None:
      obj.created_user = request.user
    obj.save()

class Media:
    		js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    	


admin.site.register(Categories)
admin.site.register(Videos,VideoClass)
admin.site.register(Users,KullaniciClass)
admin.site.register(Static_Pages,StaticClass)
admin.site.register(Events,EtkinlikClass)