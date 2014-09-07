# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.middleware import csrf
from django.contrib.auth import *
from management.models import *
from forms import *
from django.http import HttpResponse
import json
import uuid
from payment import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pafy
from django.template import RequestContext
from django.core import serializers

def makePayment(request):
    token = uuid.uuid4().hex
    obj = User_Events(user_id=1,event_id=2,user_token=token)
    obj.save()

def sendMessage(request):
    kime = request.POST.get("kime", "")
    mesaj = request.POST.get("mesaj", "")
    user= User.objects.get(username=kime)
    sender= request.user
    obj = Messages(sender_id=sender, reciever_id=user, message=mesaj,status=2)
    obj.save()

def loginUser(request):
    u_username = request.POST.get("username", "")
    u_password = request.POST.get("password", "")
    user = authenticate(username=u_username, password=u_password)
    if user:
        if user.is_active:
            login(request, user)
            current_user = request.user
            request.session['user_id'] =current_user.id
            request.session['user_name'] =u_username
            status="ok"
        else:
            return HttpResponse("Your Rango account is disabled.")
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
    registered=False
    if request.POST:
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered=True
        else:
            print user_form.errors, profile_form.errors
        return render_to_response('register.html',locals()) 
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
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
    video_comments = Video_Comments.objects.filter(video_id=video_id).order_by('-comment_date')
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
    p = Payment()
    test_obj = p.postToService()
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
    lists = User_Playlist.objects.filter(user_id=request.user)
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
    user = UserProfile.objects.get(user__id=request.user.id)
    if request.POST:
        form = ProfileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return render_to_response('profile.html',locals()) 
    else:
        form = ProfileForm(instance=user)
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
    obj = User.objects.get(id=request.session['user_id'])
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
        user = request.user
        old_p = request.POST.get("old_password", None);
        new_p1 = request.POST.get("new_password1", None);
        new_p2 = request.POST.get("new_password2", None);
        if new_p1 == new_p2:
            if user.check_password(old_p):
                user.set_password(new_p1)
                user.save()
                return HttpResponseRedirect('/sign_out')        
            else:
                pass
        else:
            pass
        return HttpResponseRedirect('/')
    else:
        return render_to_response('reset.html',locals())

def mail_degistir(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        user = request.user
        email = request.POST.get("email", None)
        user.email = email
        user.save()
        return HttpResponseRedirect('/')
    else:
        locals()["user"] = request.user
        return render_to_response('change_email.html',locals())

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
    logout(request)
    request.session.flush()
    #del request.session['user_id']
    #del request.session['user_name']    
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
    cat_id = None
    if request.method == 'GET':
        video_id = request.GET['video_id']
        likes=0
        if video_id:
            video_obj = Videos.objects.get(pk=video_id)
            user_id=request.session['user_id']
            user_obj=User.objects.get(pk=user_id)
            like_obj = User_Liked_Videos.objects.filter(video_id=video_obj, user_id=user_obj)
            if like_obj.count() == 0:
                obj = User_Liked_Videos(video_id=video_obj, user_id=user_obj)
                obj.save()
                if video_obj:
                    likes = video_obj.like_count + 1
                    video_obj.like_count =  likes
                    video_obj.save()
            else:
                obj = User_Liked_Videos.objects.get(video_id=video_obj, user_id=user_obj)
                obj.delete()
                if video_obj:
                    likes = video_obj.like_count - 1
                    video_obj.like_count =  likes
                    video_obj.save()

    return HttpResponse(likes)

def comment(request):
    vars = {}
    if request.method == 'POST':
        video_id = request.POST.get('slug', None)
        comment = request.POST.get('text', None)
        video_obj = Videos.objects.get(pk=video_id)
        user_id=request.session['user_id']
        user_obj=User.objects.get(pk=user_id)
        comments = video_obj.comment_count
        video_obj.comment_count =  comments + 1
        video_obj.save()
        obj = Video_Comments(video_id=video_obj, commenter_id=user_obj,comment=comment)
        obj.save()

    return HttpResponse(json.dumps(vars),
                    mimetype='application/javascript')

def new_list(request):
    vars = {}
    if request.method == 'POST':
        list_name = request.POST.get('name', None)
        user_id=request.session['user_id']
        user_obj=User.objects.get(pk=user_id)
        obj = User_Playlist(user_id=user_obj, playlist_name=list_name)
        obj.save()
        vars = serializers.serialize('json', [ obj, ])
        return HttpResponse(vars,   
                    mimetype='application/json')
    return HttpResponse(json.dumps(vars),
                    mimetype='application/javascript')

def follow(request):
    vars = {}
    if request.method == 'GET':
        video_id = request.GET['slug']
        video_obj = Videos.objects.get(pk=video_id)
        user_id=request.session['user_id']
        liker_obj=User.objects.get(pk=user_id)
        liked_obj=User.objects.get(pk=video_obj.publisher.id)
        fol_obj = User_Subscriptions.objects.filter(liker_id=liker_obj, liked_id=liked_obj)
        if fol_obj.count() == 0:
            obj = User_Subscriptions(liker_id=liker_obj, liked_id=liked_obj)
            obj.save()
    return HttpResponse(json.dumps(vars),
                        mimetype='application/javascript')


def video_ekle(request):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    if request.POST:
        form = AddVideoForm(request.POST,request.FILES,)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.publisher = request.user
            instance.save()
            locals()["success"] = True
            print locals()["success"]
        return render_to_response('ekle.html', locals()) 
    else:
        form = AddVideoForm()
        return render_to_response('ekle.html',locals())

def video_duzenle(request,video_id):
    csrf_token = get_or_create_csrf_token(request)
    kategoriler = Categories.objects.all()
    video = Videos.objects.get(pk=video_id)
    if request.POST:
        form = AddVideoForm(request.POST,instance=video)
        if form.is_valid():
            form.save()
            locals()["success"] = True
        return render_to_response('ekle.html',locals()) 
    else:
        form = AddVideoForm(instance=video)
        return render_to_response('ekle.html',locals())

def liste_duzenle(request,list_id):
    if request.method == "POST":
        list_id = request.POST.get("list_id", None)
        list_name = request.POST.get("list_name", None)
        liste = User_Playlist.objects.get(pk=list_id)
        liste.playlist_name = list_name
        liste.save()
        return HttpResponseRedirect('/lists/')
    else:        
        context = RequestContext(request)
        csrf_token = get_or_create_csrf_token(request)
        liste = User_Playlist.objects.get(pk=list_id)
        list_videos = Playlist_Videos.objects.filter(playlist_id=list_id)
        return render_to_response("edit_list.html",{ "list" : liste,"videos":list_videos},context)

def video_sil(request,video_id):
    obj = Videos.objects.get(id=video_id)
    obj.delete()
    return HttpResponseRedirect('/manager/')

def liste_sil(request,list_id):
    if request.user.id == request.session['user_id']:
        obj = User_Playlist.objects.get(id=list_id)
        obj.delete()
        return HttpResponseRedirect('/lists/')
    else:
        return HttpResponseRedirect('/lists/')

def coklu_listeye_ekle(request):
    if request.method == "POST":
        csrf_token = get_or_create_csrf_token(request)
        if request.POST:
            ids = request.POST.get("ids", None);

            try:
                try:
                    ids = [int(i) for i in ids.split(',')];
                except:
                    ids = [int(i) for i in ids[:-1].split(',')];
            except:
                ids = [int(i) for i in ids[1:].split(',')];
            print ids
            _list = request.POST.get("list");
            print _list
            _list = User_Playlist.objects.get(pk=_list)
            vids = Videos.objects.filter(id__in=ids)
            for vid in vids:
                try:
                    obj = Playlist_Videos.objects.create(video_id=vid, playlist_id=_list)
                except:
                    pass
            return render_to_response('manager.html', locals()) 
        else:
            return render_to_response('manager.html',locals())
    else:
        return render_to_response('manager.html',locals())

def coklu_tag_ekle(request):
    if request.method == "POST":
        csrf_token = get_or_create_csrf_token(request)
        if request.POST:
            ids = request.POST.get("ids", None);
            tags = request.POST.get("tags", None);
            try:
                try:
                    ids = [int(i) for i in ids.split(',')];
                except:
                    ids = [int(i) for i in ids[:-1].split(',')];
            except:
                ids = [int(i) for i in ids[1:].split(',')];
            print ids
            vids = Videos.objects.filter(id__in=ids)
            for vid in vids:
                vid.tags = vid.tags + ',' + tags
                vid.save()
            return render_to_response('manager.html', locals()) 
        else:
            return render_to_response('manager.html',locals())
    return render_to_response('manager.html',locals())


def coklu_kategori_degistir(request):
    if request.method == "POST":
        csrf_token = get_or_create_csrf_token(request)
        if request.POST:
            ids = request.POST.get("ids", None);
            try:
                try:
                    ids = [int(i) for i in ids.split(',')];
                except:
                    ids = [int(i) for i in ids[:-1].split(',')];
            except:
                ids = [int(i) for i in ids[1:].split(',')];
            print ids
            cat = request.POST.get("category");
            category = Categories.objects.get(id=cat)
            vids = Videos.objects.filter(id__in=ids)
            for vid in vids:
                vid.category = category
                vid.save()
            return render_to_response('manager.html', locals()) 
        else:
            return render_to_response('manager.html',locals())

def coklu_sil(request):
    if request.method == "POST":
        csrf_token = get_or_create_csrf_token(request)
        if request.POST:
            ids = request.POST.get("ids", None);
            try:
                try:
                    ids = [int(i) for i in ids.split(',')];
                except:
                    ids = [int(i) for i in ids[:-1].split(',')];
            except:
                ids = [int(i) for i in ids[1:].split(',')];
            print ids
            vids = Videos.objects.filter(id__in=ids)
            vids.delete();
            return render_to_response('manager.html', locals()) 
        else:
            return render_to_response('manager.html',locals())
    return render_to_response('manager.html',locals())

def coklu_public(request):
    if request.method == "POST":
        csrf_token = get_or_create_csrf_token(request)
        if request.POST:
            ids = request.POST.get("ids", None);
            tags = request.POST.get("tags", None);
            try:
                try:
                    ids = [int(i) for i in ids.split(',')];
                except:
                    ids = [int(i) for i in ids[:-1].split(',')];
            except:
                ids = [int(i) for i in ids[1:].split(',')];
            print ids
            vids = Videos.objects.filter(id__in=ids)
            for vid in vids:
                vid.sharing_permissions = 1
                vid.save()
            return render_to_response('manager.html', locals()) 
        else:
            return render_to_response('manager.html',locals())
    return render_to_response('manager.html',locals())

def coklu_url_public(request):
    if request.method == "POST":
        csrf_token = get_or_create_csrf_token(request)
        if request.POST:
            ids = request.POST.get("ids", None);
            tags = request.POST.get("tags", None);
            try:
                try:
                    ids = [int(i) for i in ids.split(',')];
                except:
                    ids = [int(i) for i in ids[:-1].split(',')];
            except:
                ids = [int(i) for i in ids[1:].split(',')];
            print ids
            vids = Videos.objects.filter(id__in=ids)
            for vid in vids:
                vid.sharing_permissions = 2
                vid.save()
            return render_to_response('manager.html', locals()) 
        else:
            return render_to_response('manager.html',locals())
    return render_to_response('manager.html',locals())

def coklu_private(request):
    if request.method == "POST":
        csrf_token = get_or_create_csrf_token(request)
        if request.POST:
            ids = request.POST.get("ids", None);
            tags = request.POST.get("tags", None);
            try:
                try:
                    ids = [int(i) for i in ids.split(',')];
                except:
                    ids = [int(i) for i in ids[:-1].split(',')];
            except:
                ids = [int(i) for i in ids[1:].split(',')];
            print ids
            vids = Videos.objects.filter(id__in=ids)
            for vid in vids:
                vid.sharing_permissions = 3
                vid.save()
            return render_to_response('manager.html', locals()) 
        else:
            return render_to_response('manager.html',locals())
    return render_to_response('manager.html',locals())