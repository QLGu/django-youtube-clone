from django.db import models

# Create your models here.
class Users(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_name = models.CharField(max_length=255)
    image_url = models.URLField()
    social_id = models.CharField(max_length=255)
    social_type = models.IntegerField()

    def __unicode__(self):
        return self.profile_name

class Categories(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url_name=models.CharField(max_length=255)
  
    def __unicode__(self):
    	return self.name

class Videos(models.Model): 
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories)
    name = models.CharField(max_length=255)
    resource = models.IntegerField(max_length=255,choices=[(1, 'Amazon AWS'), (2, 'Google Drive'),(3, 'Vimeo'), (4, 'Youtube')])
    path = models.URLField()
    publisher=models.ForeignKey(Users)
    video_image=models.ImageField(upload_to="image/uploads/%Y/%m/%d")
    desc=models.TextField()
    tags = models.CharField(max_length=255)
    #likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Video_Comments(models.Model):
    id=models.AutoField(primary_key=True)
    commenter_id=models.ForeignKey(Users)
    video_id=models.ForeignKey(Videos)
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now=True)

class Static_Pages(models.Model): 
    id = models.AutoField(primary_key=True)
    type = models.IntegerField(max_length=255,choices=[(1, 'Help'), (2, 'Contact')])
    header = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    created_user = models.ForeignKey(Users)

    def __unicode__(self):
        return self.header

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
	event_image=models.ImageField(upload_to="image/uploads/%Y/%m/%d")

	def __unicode__(self): 
	    return self.event_name 