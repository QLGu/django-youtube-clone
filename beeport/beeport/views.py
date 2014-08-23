# -*- coding: utf-8 -*-
from django.http import *
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from management.models import *

def ana_sayfa(request):
    kategoriler = Categories.objects.all()
    return render_to_response('index.html',locals())

def kayit_sayfasi(request):
    return render_to_response('register.html') 

def kategori(request,kategori_adi):
	html = kategori_adi
    	return render_to_response('category.html') 

def ondemand_izleme_sayfasi(request):
    return render_to_response('watch.html') 

def live_stream_sayfasi(request):
    return render_to_response('event.html') 

def live_stream_izleme_sayfasi(request):
    return render_to_response('live.html') 

def live_stream_satin_alma_sayfasi(request):
    return render_to_response('buy.html') 

def arama(request):
    return render_to_response('search.html')   

def video_yoneticisi(request):
    return render_to_response('manager.html')  

def listelerim(request):
    return render_to_response('lists.html') 

def bilgilerimi_guncelle(request):
    return render_to_response('profile.html') 

def mesajlarim(request):
    return Hrender_to_response('messages.html')  

def abonelikler(request):
    return render_to_response('subscriptions.html')  

def bildirim_ayarlari(request):
    return render_to_response('settings.html') 

def iletisim(request):
    return render_to_response('contact.html')

def yardim(request):
    return render_to_response('help.html') 

def rss(request):
    return render_to_response('rss.html') 