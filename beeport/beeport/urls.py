from django.conf.urls import patterns, include, url
import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beeport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^management/', include(admin.site.urls)),
    url(r'^$', views.ana_sayfa),
    url(r'^register/', views.kayit_sayfasi),
    url(r'^watch/(.+)/', views.ondemand_izleme_sayfasi),
    url(r'^event/(.+)/', views.live_stream_sayfasi),
    url(r'^live/(.+)/', views.live_stream_izleme_sayfasi),
    url(r'^buy/(.+)/', views.live_stream_satin_alma_sayfasi),
    url(r'^search/$', views.arama),
    url(r'^manager/', views.video_yoneticisi),
    url(r'^lists/', views.listelerim),
    url(r'^profile/', views.bilgilerimi_guncelle),
    url(r'^messages/', views.mesajlarim),
    url(r'^subscriptions/', views.abonelikler),
    url(r'^settings/', views.bildirim_ayarlari),
    url(r'^contact/', views.iletisim),
    url(r'^help/', views.yardim),
    url(r'^rss/', views.rss),
    url(r'^sign_out/', views.oturum_kapat),
    url(r'^oneall/', include('django_oneall.urls')),
    url(r'^terms/',views.kosullar),
    url(r'^forgot_pass/',views.sifremi_unuttum),
    url(r'^reset_pass/',views.sifre_sifirla),
    url(r'^privacy/',views.gizlilik),
    url(r'^category/(.+)/', views.kategori),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
