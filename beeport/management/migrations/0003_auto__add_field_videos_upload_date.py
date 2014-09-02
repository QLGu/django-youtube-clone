# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Videos.upload_date'
        db.add_column(u'management_videos', 'upload_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 1, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Videos.upload_date'
        db.delete_column(u'management_videos', 'upload_date')


    models = {
        u'management.categories': {
            'Meta': {'object_name': 'Categories'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'management.events': {
            'Meta': {'object_name': 'Events'},
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            'event_desc': ('django.db.models.fields.TextField', [], {}),
            'event_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'event_price': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'management.messages': {
            'Meta': {'object_name': 'Messages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'reciever_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_recievers'", 'to': u"orm['management.Users']"}),
            'sender_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_senders'", 'to': u"orm['management.Users']"}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'management.password_token_cache': {
            'Meta': {'object_name': 'Password_Token_Cache'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pass_token': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Users']"})
        },
        u'management.static_pages': {
            'Meta': {'object_name': 'Static_Pages'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Users']"}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'max_length': '255'})
        },
        u'management.user_events': {
            'Meta': {'object_name': 'User_Events'},
            'event_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'user_token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'management.user_liked_videos': {
            'Meta': {'object_name': 'User_Liked_Videos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liked_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Users']"}),
            'video_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Videos']"})
        },
        u'management.users': {
            'Meta': {'object_name': 'Users'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'social_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'social_type': ('django.db.models.fields.IntegerField', [], {}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'management.video_comments': {
            'Meta': {'object_name': 'Video_Comments'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'comment_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'commenter_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Users']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Videos']"})
        },
        u'management.videos': {
            'Meta': {'object_name': 'Videos'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Categories']"}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Users']"}),
            'resource': ('django.db.models.fields.IntegerField', [], {'max_length': '255'}),
            'sharing_permissions': ('django.db.models.fields.IntegerField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'video_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['management']