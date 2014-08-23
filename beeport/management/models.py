from django.db import models

# Create your models here.
class Categories(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url_name=models.CharField(max_length=255)
  
class Videos(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    resource = models.IntegerField(max_length=255,choices=[(1, 'Amazon AWS'), (2, 'Google Drive'),(3, 'Vimeo'), (4, 'Youtube')])
    path = models.URLField()
    tags = models.TextField()
 
class Users(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_name = models.CharField(max_length=255)
    image_url = models.URLField()
    social_id = models.TextField()
    social_type = models.IntegerField()

class Static_Pages(models.Model): 
    id = models.AutoField(primary_key=True)
    header = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    created_user = models.IntegerField()

class User_Events(models.Model):
	id=models.AutoField(primary_key=True)
	user_id=models.IntegerField()
	event_id=models.IntegerField()
	user_token=models.CharField(max_length=255)

class Events(models.Model):
	id=models.AutoField(primary_key=True)
	event_name=models.CharField(max_length=255)
	event_desc=models.TextField()
	event_price=models.FloatField()