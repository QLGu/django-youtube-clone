# -*- coding: utf-8 -*-
from django.http import *
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.middleware import csrf
from management.models import *
from forms import RegisterForm
from django.http import HttpResponseRedirect

def loginUser():
    email = request.POST.get('email','')
    password = request.POST.get('password','')

def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token

def ana_sayfa(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    videos = Videos.objects.all()
    events = Events.objects.all()
    if request.POST:
        loginUser()
        return render_to_response('index.html',locals())
    else:
        return render_to_response('index.html',locals())

def kayit_sayfasi(request):
    kategoriler=Categories.objects.all()
    csrf_token = get_or_create_csrf_token(request)
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return render_to_response('register.html',locals()) 
    else:
        form = RegisterForm()
        return render_to_response('register.html',locals()) 
    
def kategori(request,kategori_adi):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler=Categories.objects.all()
    cat_info = Categories.objects.filter(url_name=kategori_adi)
    html = kategori_adi
    videos = Videos.objects.filter(category=1)
    if request.POST:
        return render_to_response('category.html',locals())
    else:
        return render_to_response('category.html',locals())

def ondemand_izleme_sayfasi(request,video_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler=Categories.objects.all()
    video_data = Videos.objects.filter(id=video_id)
    if request.POST:
        return render_to_response('watch.html',locals())
    else:
        return render_to_response('watch.html',locals())

def live_stream_sayfasi(request,event_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler=Categories.objects.all()
    video_data = Videos.objects.filter(id=2)
    event = Events.objects.filter(id=event_id)
    if request.POST:
        return render_to_response('event.html',locals())
    else:
        return render_to_response('event.html',locals())

def live_stream_izleme_sayfasi(request,event_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('live.html',locals())
    else:
        return render_to_response('live.html',locals())

def live_stream_satin_alma_sayfasi(request,event_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('buy.html',locals())
    else:
        return render_to_response('buy.html',locals())

def arama(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('search.html',locals())
    else:
        return render_to_response('search.html',locals())  

def video_yoneticisi(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('manager.html',locals())
    else:
        return render_to_response('manager.html',locals())

def listelerim(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('lists.html',locals())
    else:
        return render_to_response('lists.html',locals())

def bilgilerimi_guncelle(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('profile.html',locals())
    else:
        return render_to_response('profile.html',locals())

def mesajlarim(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('messages.html',locals())
    else:
        return render_to_response('messages.html',locals())

def abonelikler(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('subscriptions.html',locals())
    else:
        return render_to_response('subscriptions.html',locals())

def bildirim_ayarlari(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('settings.html',locals())
    else:
        return render_to_response('settings.html',locals())

def iletisim(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('contact.html',locals())
    else:
        return render_to_response('contact.html',locals())

def yardim(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('help.html',locals())
    else:
        return render_to_response('help.html',locals())

def rss(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('rss.html',locals())
    else:
        return render_to_response('rss.html',locals())

def gizlilik(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('gizlilik.html',locals())
    else:
        return render_to_response('gizlilik.html',locals())

def kosullar(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('kosullar.html',locals())
    else:
        return render_to_response('kosullar.html',locals())