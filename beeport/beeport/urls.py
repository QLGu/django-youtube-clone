from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beeport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^management/', include(admin.site.urls)),
    url(r'^$', views.ana_sayfa),
    url(r'^(.+)/', views.kategori),
    url(r'^register/', views.kayit_sayfasi),
    url(r'^watch/', views.ondemand_izleme_sayfasi),
    url(r'^event/', views.live_stream_sayfasi),
    url(r'^live/', views.live_stream_izleme_sayfasi),
    url(r'^buy/', views.live_stream_satin_alma_sayfasi),
    url(r'^search/', views.arama),
    url(r'^manager/', views.video_yoneticisi),
    url(r'^lists/', views.listelerim),
    url(r'^profile/', views.bilgilerimi_guncelle),
    url(r'^messages/', views.mesajlarim),
    url(r'^subscriptions/', views.abonelikler),
    url(r'^settings/', views.bildirim_ayarlari),
    url(r'^contact/', views.iletisim),
    url(r'^help/', views.yardim),
    url(r'^rss/', views.rss)
)
