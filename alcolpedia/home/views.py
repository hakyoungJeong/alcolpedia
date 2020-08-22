from django.shortcuts import render,get_object_or_404,redirect
from article.models import *
from member.models import Profile
from django.utils.timezone import localdate
from django.core.paginator import Paginator

#메인화면
def home(request):
    tag = Tag.objects.all()
    contents_list = Content.objects.filter(sort = "game").order_by('updated_at')
    contents_list_len = len(contents_list)
    contents_list = contents_list[:min(3,contents_list_len)]

    bgm_list = Content.objects.filter(sort = "bgm").order_by('updated_at')
    
    bgm_list_len = len(bgm_list)
    bgm_listt = bgm_list[:min(3,bgm_list_len)]

    try:
        profile = get_object_or_404(Profile, user__username = request.user.username)
        return render(request, 'home.html',{'title': 'Alcolpedia','profile':profile,'tags':tag, 'contents': contents_list, 'bgms': bgm_list})
    except :
        return render(request,'home.html',{'title': 'Alcolpedia','tags':tag, 'contents': contents_list, 'bgms': bgm_list})

#검색기능
def search(request) :
    q = request.GET.get('q')
    if q :
        contents = Content.objects.filter(title__icontains=q)
        try:
            profile = get_object_or_404(Profile, user__username = request.user.username)
            return render(request,'search.html',{'contents':contents, 'q':q,'profile':profile})
        except:
            return render(request,'search.html',{'contents':contents, 'q':q})
    else : 
        return render(request,'search.html')
# def detail(request, content_id):
