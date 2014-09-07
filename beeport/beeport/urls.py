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
    url(r'^$', views.ana_sayfa, name="home"),
    url(r'^register/', views.kayit_sayfasi, name="register"),
    url(r'^watch/(.+)/', views.ondemand_izleme_sayfasi, name="watch1"),
    url(r'^watch/$', views.ondemand_izleme_sayfasi, name="watch2"),
    url(r'^event/(.+)/', views.live_stream_sayfasi, name="event"),
    url(r'^live/(.+)/', views.live_stream_izleme_sayfasi, name="live"),
    url(r'^buy/(.+)/', views.live_stream_satin_alma_sayfasi, name="buy"),
    url(r'^search/$', views.arama, name="search"),
    url(r'^manager/', views.video_yoneticisi, name="manager"),
    url(r'^lists/', views.listelerim, name="lists"),
    url(r'^del-list/(.+)/',views.liste_sil, name="del_list"),
    url(r'^del_video/(.+)/',views.video_sil, name="del_video"),
    url(r'^profile/', views.bilgilerimi_guncelle, name="profile"),
    url(r'^messages/', views.mesajlarim, name="messages"),
    url(r'^subscriptions/', views.abonelikler, name="subscriptions"),
    url(r'^settings/', views.bildirim_ayarlari, name="settings"),
    url(r'^contact/', views.iletisim, name="contact"),
    url(r'^help/', views.yardim, name="help"),
    url(r'^rss/', views.rss, name="rss"),
    url(r'^sign_out/', views.oturum_kapat, name="sign_out"),
    url(r'^oneall/', include('django_oneall.urls')),
    url(r'^terms/',views.kosullar, name="terms"),
    url(r'^forgot_pass/',views.sifremi_unuttum, name="forgot_pass"),
    url(r'^reset_pass/',views.sifre_sifirla, name="reset_pass"),
    url(r'^privacy/',views.gizlilik, name="privacy"),
    url(r'^category/(.+)/', views.kategori, name="category"),
    url(r'^delete_user/',views.kullanici_sil, name="delete_user"),
    url(r'^change_pass/',views.sifre_degistir, name="change_pass"),
    url(r'^update_email/', views.mail_degistir, name="update_email"),
    url(r'^add_video/',views.video_ekle, name="add_video"),
    url(r'^coklu_kategori_degistir/',views.coklu_kategori_degistir, name="coklu_kategori_degistir"),
    url(r'^coklu_sil/',views.coklu_sil, name="coklu_sil"),
    url(r'^edit_video/(.+)/',views.video_duzenle, name="edit_video"),
    url(r'^edit_list/(.+)/',views.liste_duzenle, name="edit_list"),
    url(r'^del_video/(.+)/',views.video_sil, name="del_video"),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    #Services
    url(r'^like/$', views.like, name="like"),
    url(r'^comment/$', views.comment, name="comment"),
    url(r'^follow/$', views.follow, name="follow"),
    url(r'^nplaylist/$', views.new_list, name='newlist'),
    url(r'^/add-multi-list/$',views.coklu_listeye_ekle, name="add-multi-list"),
    url(r'^/add-multi-tag/$',views.coklu_tag_ekle, name="add-multi-tag"),
    url(r'^/change-multi-cat/$',views.coklu_kategori_degistir, name="change-multi-cat"),
    url(r'^/delete-multi/$',views.coklu_sil, name="delete-multi"),
    url(r'^/make-multi-public/$',views.coklu_public, name="make-multi-public"),
    url(r'^/make-multi-owner-public/$',views.coklu_url_public, name="make-multi-owner-public"),
    url(r'^/make-multi-private/$',views.coklu_private, name="make-multi-private"),

    
)

