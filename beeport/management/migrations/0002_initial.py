# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Users'
        db.create_table(u'management_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('profile_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('social_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('social_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'management', ['Users'])

        # Adding model 'Categories'
        db.create_table(u'management_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'management', ['Categories'])

        # Adding model 'Videos'
        db.create_table(u'management_videos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Categories'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('resource', self.gf('django.db.models.fields.IntegerField')(max_length=255)),
            ('path', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Users'])),
            ('sharing_permissions', self.gf('django.db.models.fields.IntegerField')(max_length=255)),
            ('video_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'management', ['Videos'])

        # Adding model 'Video_Comments'
        db.create_table(u'management_video_comments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commenter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Users'])),
            ('video_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Videos'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('comment_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'management', ['Video_Comments'])

        # Adding model 'User_Liked_Videos'
        db.create_table(u'management_user_liked_videos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Videos'])),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Users'])),
            ('liked_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'management', ['User_Liked_Videos'])

        # Adding model 'Static_Pages'
        db.create_table(u'management_static_pages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(max_length=255)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Users'])),
        ))
        db.send_create_signal(u'management', ['Static_Pages'])

        # Adding model 'User_Events'
        db.create_table(u'management_user_events', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('event_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_token', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'management', ['User_Events'])

        # Adding model 'Events'
        db.create_table(u'management_events', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_desc', self.gf('django.db.models.fields.TextField')()),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('event_price', self.gf('django.db.models.fields.FloatField')()),
            ('event_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'management', ['Events'])

        # Adding model 'Messages'
        db.create_table(u'management_messages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reciever_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_recievers', to=orm['management.Users'])),
            ('sender_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_senders', to=orm['management.Users'])),
            ('sent_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'management', ['Messages'])

        # Adding model 'Password_Token_Cache'
        db.create_table(u'management_password_token_cache', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Users'])),
            ('pass_token', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal(u'management', ['Password_Token_Cache'])


    def backwards(self, orm):
        # Deleting model 'Users'
        db.delete_table(u'management_users')

        # Deleting model 'Categories'
        db.delete_table(u'management_categories')

        # Deleting model 'Videos'
        db.delete_table(u'management_videos')

        # Deleting model 'Video_Comments'
        db.delete_table(u'management_video_comments')

        # Deleting model 'User_Liked_Videos'
        db.delete_table(u'management_user_liked_videos')

        # Deleting model 'Static_Pages'
        db.delete_table(u'management_static_pages')

        # Deleting model 'User_Events'
        db.delete_table(u'management_user_events')

        # Deleting model 'Events'
        db.delete_table(u'management_events')

        # Deleting model 'Messages'
        db.delete_table(u'management_messages')

        # Deleting model 'Password_Token_Cache'
        db.delete_table(u'management_password_token_cache')


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
            'video_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['management']