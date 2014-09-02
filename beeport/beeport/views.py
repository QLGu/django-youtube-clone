# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.middleware import csrf
from management.models import *
from forms import *
from django.http import HttpResponse
from django.utils import simplejson
import uuid
from payment import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pafy

def makePayment(request):
    token = uuid.uuid4().hex
    p = Payment()
    test_obj = p.postToService()
    obj = User_Events(user_id=1,event_id=2,user_token=token)
    obj.save()

def sendMessage(request):
    kime = request.POST.get("kime", "")
    mesaj = request.POST.get("mesaj", "")
    user= Users.objects.get(profile_name=kime)
    sender= Users.objects.get(pk=1)
    obj = Messages(sender_id=sender, reciever_id=user, message=mesaj,status=2)
    obj.save()

def loginUser(request):
    u_email = request.POST.get("email", "")
    u_password = request.POST.get("password", "")
    user_data = Users.objects.filter(email=u_email, password=u_password)
    if user_data.count() > 0:
        request.session.set_test_cookie()
        request.session['user_id'] =user_data[0].id
        request.session['user_name'] =user_data[0].profile_name
        status="ok"
    else:
        status = "Kullanici adi ya da sifre yanlıs"
        
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
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
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
    cat_id=cat_info[0].id
    videos = Videos.objects.filter(category=cat_id)
    paginator = Paginator(videos,10)
    page=request.GET.get('page')
    try:
        videos=paginator.page(page)
    except PageNotAnInteger:
        videos=paginator.page(1)
    except EmptyPage:
        videos=paginator.page(paginator.num_pages)
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('category.html',locals())
    else:
        return render_to_response('category.html',locals())

def ondemand_izleme_sayfasi(request,video_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler=Categories.objects.all()
    video_data = Videos.objects.filter(id=video_id)
    video_resource=video_data[0].resource
    if video_resource == 1:
        video_path=video_data[0].path
    elif video_resource == 2:
        video_path=video_data[0].path
    elif video_resource == 3:
        video_path=video_data[0].path
    elif video_resource == 4:
        video = pafy.new(video_data[0].path)
        best = video.getbest(preftype="mp4")
        video_path=best.url
    else:
        video_path=video_data[0].path
    video_name=video_data[0].name
    video_publisher=video_data[0].publisher
    video_like_count=User_Liked_Videos.objects.filter(video_id=video_id).count()
    video_comment_count=Video_Comments.objects.filter(video_id=video_id).count()
    video_comments = Video_Comments.objects.filter(video_id=video_id)
    related_videos = Videos.objects.filter(category=video_data[0].category)
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('watch.html',locals())
    else:
        return render_to_response('watch.html',locals())

def live_stream_sayfasi(request,event_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler=Categories.objects.all()
    video_data = Videos.objects.filter(id=2)
    event = Events.objects.filter(id=event_id)
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('event.html',locals())
    else:
        return render_to_response('event.html',locals())

def live_stream_izleme_sayfasi(request,event_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    event = Events.objects.get(id=event_id)
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('live.html',locals())
    else:
        return render_to_response('live.html',locals())

def live_stream_satin_alma_sayfasi(request,event_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    user_bought = User_Events.objects.filter(user_id=1,event_id=event_id)
    makePayment(request)
    if len(user_bought) >0:
        return HttpResponseRedirect('/live/'+event_id)
    else:
        if request.POST:
            action_name = request.POST.get("action", "")
            if action_name == "login":
                loginUser(request)
            else:
                status="wait an action"
            return render_to_response('buy.html',locals())
        else:
            return render_to_response('buy.html',locals())

def arama(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('search.html',locals())
    else:
        query = request.GET['srch-term']
        event = Events.objects.filter(event_name__contains=query)
        video_data = Videos.objects.filter(name__contains=query)
        return render_to_response('search.html',locals())  

def video_yoneticisi(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    my_videos = Videos.objects.filter(publisher=request.session['user_id'])
    video_count=my_videos.count()
    if request.POST:
        return render_to_response('manager.html',locals())
    else:
        return render_to_response('manager.html',locals())

def listelerim(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    my_lists = User_Playlist.objects.filter(user_id=request.session['user_id'])
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
    recieved_messages=Messages.objects.filter(reciever_id=request.session['user_id'])
    sent_messages=Messages.objects.filter(sender_id=request.session['user_id'])
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "message":
            sendMessage(request)
        else:
            status="wait an action"
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
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('contact.html',locals())
    else:
        return render_to_response('contact.html',locals())

def yardim(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
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

def kullanici_sil(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    obj = Users.objects.get(id=request.session['user_id'])
    obj.delete()
    request.session.flush()
    if request.POST:
        return render_to_response('rss.html',locals())
    else:
        return render_to_response('rss.html',locals())

def sifre_degistir(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('rss.html',locals())
    else:
        return render_to_response('rss.html',locals())

def mail_degistir(request):
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
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('gizlilik.html',locals())
    else:
        return render_to_response('gizlilik.html',locals())

def oturum_kapat(request):
    del request.session['user_id']
    del request.session['user_name']
    request.session.flush()
    return HttpResponseRedirect('/')

def kosullar(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        action_name = request.POST.get("action", "")
        if action_name == "login":
            loginUser(request)
        else:
            status="wait an action"
        return render_to_response('kosullar.html',locals())
    else:
        return render_to_response('kosullar.html',locals())

def sifremi_unuttum(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        email = request.POST['email']
        subject = "Beetube.tv Şifre Sıfırlama"
        message = "http://127.0.0.1:8000/reset_pass?token="+uuid.uuid4().hex
        recipients = [request.POST['email']]
        send_mail(subject, message, settings.EMAIL_HOST_USER,recipients, fail_silently=False)
        return render_to_response('unuttum.html',locals())
    else:
        return render_to_response('unuttum.html',locals())

def sifre_sifirla(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    token=request.GET['token']
    if request.POST:
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        return render_to_response('reset.html',locals())
    else:
        return render_to_response('reset.html',locals())

def like(request):
    vars = {}
    if request.method == 'POST':
        video_id = request.POST.get('slug', None)
        video_obj = Videos.objects.get(pk=video_id)
        user_id=request.session['user_id']
        user_obj=Users.objects.get(pk=user_id)
        like_obj = User_Liked_Videos.objects.filter(video_id=video_obj, user_id=user_obj)
        if like_obj.count() == 0:
            obj = User_Liked_Videos(video_id=video_obj, user_id=user_obj)
            obj.save()

    return HttpResponse(simplejson.dumps(vars),
                    mimetype='application/javascript')

def comment(request):
    vars = {}
    if request.method == 'POST':
        video_id = request.POST.get('slug', None)
        comment = request.POST.get('text', None)
        video_obj = Videos.objects.get(pk=video_id)
        user_id=request.session['user_id']
        user_obj=Users.objects.get(pk=user_id)
        #com_obj = Video_Comments.objects.filter(video_id=video_obj, commenter_id=user_obj)
        #if com_obj.count() == 0:
        obj = Video_Comments(video_id=video_obj, commenter_id=user_obj,comment=comment)
        obj.save()

    return HttpResponse(simplejson.dumps(vars),
                    mimetype='application/javascript')

def new_list(request):
    vars = {}
    if request.method == 'POST':
        list_name = request.POST.get('name', None)
        user_id=request.session['user_id']
        user_obj=Users.objects.get(pk=user_id)
        obj = User_Playlist(user_id=user_obj, playlist_name=list_name)
        obj.save()

    return HttpResponse(simplejson.dumps(vars),
                    mimetype='application/javascript')

def follow(request):
    vars = {}
    if request.method == 'POST':
        video_id = request.POST.get('slug', None)
        video_obj = Videos.objects.get(pk=video_id)
        user_id=request.session['user_id']
        liker_obj=Users.objects.get(pk=user_id)
        liked_obj=Users.objects.get(pk=video_obj.publisher)
        fol_obj = User_Subscriptions.objects.filter(liker_id=liker_obj, liked_id=liked_obj)
        if fol_obj.count() == 0:
            obj = User_Subscriptions(liker_id=liker_obj, liked_id=liked_obj)
            obj.save()
    return HttpResponse(simplejson.dumps(vars),
                        mimetype='application/javascript')


def video_ekle(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        return render_to_response('ekle.html',locals())
    else:
        return render_to_response('ekle.html',locals())
