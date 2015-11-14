#coding=utf-8

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from blog.models import BlogsPost,User,Demo,QRUrl
from django.shortcuts import render_to_response
import os
from django import forms
from django.http import HttpResponse

base=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    l_blog=[]
    for blog in blog_list:
        l_blog.append(blog)
    return render_to_response('index.html',{'posts':l_blog,'base':base})


def list(request):
    l_demo = Demo.objects.all()
    return render_to_response("list.html",{"l_demo":l_demo})

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            #写入数据库
            user = User()
            user.username = username
            user.headImg = headImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})


