# -*- coding: utf-8 -*-
from django.http import *
 
def ana_sayfa(request):
    return HttpResponse(u'Merhaba Django') 

def kayit_sayfasi(request):
    return HttpResponse(u'Merhaba Django') 

def kategori(request,kategori_adi):
	html = kategori_adi
    	return HttpResponse(html) 

def ondemand_izleme_sayfasi(request):
    return HttpResponse(u'Merhaba Django') 

def live_stream_sayfasi(request):
    return HttpResponse(u'Merhaba Django')

def live_stream_izleme_sayfasi(request):
    return HttpResponse(u'Merhaba Django')

def live_stream_satin_alma_sayfasi(request):
    return HttpResponse(u'Merhaba Django') 

def arama(request):
    return HttpResponse(u'Merhaba Django')  

def video_yoneticisi(request):
    return HttpResponse(u'Merhaba Django') 

def listelerim(request):
    return HttpResponse(u'Merhaba Django') 

def bilgilerimi_guncelle(request):
    return HttpResponse(u'Merhaba Django') 

def mesajlarim(request):
    return HttpResponse(u'Merhaba Django') 

def abonelikler(request):
    return HttpResponse(u'Merhaba Django') 

def bildirim_ayarlari(request):
    return HttpResponse(u'Merhaba Django') 

def iletisim(request):
    return HttpResponse(u'Merhaba Django') 

def yardim(request):
    return HttpResponse(u'Merhaba Django') 

def rss(request):
    return HttpResponse(u'Merhaba Django') 