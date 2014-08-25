# -*- coding: utf-8 -*-
from django.http import *
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.middleware import csrf
from management.models import *

def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token

def ana_sayfa(request):
    kategoriler = Categories.objects.all()
    videos = Videos.objects.all()
    events = Events.objects.all()
    return render_to_response('index.html',locals())

def kayit_sayfasi(request):
    csrf_token = get_or_create_csrf_token(request)
    if request.method=="post":
        name = request.POST['name']
        surname = request.POST['surname']
        mail = request.POST['mail']
        password = request.POST['password']
        passagain = request.POST['passagain']
        return render_to_response('register.html',locals()) 
    else:
        mert= "test"
        return render_to_response('register.html',locals()) 
    
def kategori(request,kategori_adi):
	html = kategori_adi
        kategoriler = Categories.objects.all()

        videos = Videos.objects.filter(id=video_id)
        return render_to_response('category.html',locals()) 

def ondemand_izleme_sayfasi(request,video_id):
    kategoriler=Categories.objects.all()
    video_data = Videos.objects.filter(id=video_id)
    return render_to_response('watch.html',locals()) 

def live_stream_sayfasi(request,event_id):
	kategoriler=Categories.objects.all()
        video_data = Videos.objects.filter(id=2)
        event = Events.objects.filter(id=event_id)
    	return render_to_response('event.html',locals()) 

def live_stream_izleme_sayfasi(request,event_id):
    return render_to_response('live.html') 

def live_stream_satin_alma_sayfasi(request,event_id):
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