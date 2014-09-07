# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model): 
    user = models.OneToOneField(User)
    image_url = models.URLField()
    gender = models.IntegerField(max_length=255,choices=[(1,'Erkek'),(2,'Kadın')])
    about_me=models.TextField(blank=True,null=True,default="")
    birthdate=models.DateField(blank=True,null=True,default=datetime.now())
    social_id = models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    social_type = models.IntegerField(default=0,choices=[(0,'No Social Media'),(1,'Facebook'),(2,'Twitter'),(3,'Google')])
    
    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural="Kullanıcılar"

class Categories(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url_name=models.SlugField(editable=False)
  
    def __unicode__(self):
    	return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_name = slugify(self.name)

        super(Categories, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural="Kategoriler"

class Videos(models.Model): 
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories)
    name = models.CharField(max_length=255)
    resource = models.IntegerField(max_length=255,choices=[(1, 'Amazon AWS'), (2, 'Google Drive'),(3, 'Vimeo'), (4, 'Youtube')])
    path=models.URLField()
    path_240p = models.URLField(blank=True,null=True)
    path_360p = models.URLField(blank=True,null=True)
    path_480p = models.URLField(blank=True,null=True)
    path_720p = models.URLField(blank=True,null=True)
    publisher=models.ForeignKey(User)
    sharing_permissions=models.IntegerField(max_length=255,choices=[(1,'Herkese Açık'),(2,'Video Linkine Sahip Olan Herkese Açık'),(3,'Sadece Bana Açık')])
    video_image=models.ImageField(upload_to="image/%Y/%m/%d")
    desc=models.TextField(null=True, blank=True)
    upload_date=models.DateTimeField(auto_now=True,default=datetime.now())
    tags = models.CharField(max_length=255)
    like_count=models.IntegerField(default=0)
    comment_count=models.IntegerField(default=0)
    watch_count=models.IntegerField(default=0)
    video_duration=models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="Videolar"

class Video_Comments(models.Model):
    id=models.AutoField(primary_key=True)
    commenter_id=models.ForeignKey(User)
    video_id=models.ForeignKey(Videos)
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="Yorumlar"

class User_Liked_Videos(models.Model):
    id=models.AutoField(primary_key=True)
    video_id=models.ForeignKey(Videos)
    user_id=models.ForeignKey(User)
    liked_date=models.DateTimeField(auto_now=True)

class Static_Pages(models.Model): 
    id = models.AutoField(primary_key=True)
    type = models.IntegerField(max_length=255,choices=[(1, 'Help'), (2, 'Contact')])
    header = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    created_user = models.ForeignKey(User)

    def __unicode__(self):
        return self.header

    class Meta:
        verbose_name_plural="Statik Sayfalar"

class User_Events(models.Model):
	id=models.AutoField(primary_key=True)
	user_id=models.IntegerField()
	event_id=models.IntegerField()
	user_token=models.CharField(max_length=255)

class Events(models.Model):
	id=models.AutoField(primary_key=True)
	event_name=models.CharField(max_length=255)
	event_desc=models.TextField()
        event_date=models.DateTimeField()
	event_price=models.FloatField()
	event_image=models.ImageField(upload_to="image/%Y/%m/%d")

class Meta:
        verbose_name_plural="Etkinlikler"

	def __unicode__(self): 
	    return self.event_name 

class Messages(models.Model):
     id=models.AutoField(primary_key=True)
     reciever_id=models.ForeignKey(User, related_name='message_recievers')
     sender_id=models.ForeignKey(User, related_name='message_senders')
     sent_date=models.DateTimeField(auto_now=True)
     message=models.TextField()
     status=models.IntegerField(choices=[(1,'Okundu'),(2,'İletildi')])

class Password_Token_Cache(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User)
    pass_token=models.TextField(max_length=255)

class User_Playlist(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User)
    playlist_name=models.CharField(max_length=255)

class Playlist_Videos(models.Model):
    id=models.AutoField(primary_key=True)
    video_id=models.ForeignKey(Videos)
    playlist_id=models.ForeignKey(User_Playlist)

class User_Subscriptions(models.Model):
    id=models.AutoField(primary_key=True)
    liker_id=models.ForeignKey(User, related_name='user_liker')
    liked_id=models.ForeignKey(User, related_name='user_liked')

class Event_Stream_Informations(models.Model):
    id=models.AutoField(primary_key=True)
    event_id=models.ForeignKey(Events)
    resource = models.IntegerField(max_length=255,choices=[(1, 'Livestream'), (2, 'Server Link'),(3, 'Youtube')])
    stream_link = models.URLField()

#class Site_Editable_Settings(models.Model):


