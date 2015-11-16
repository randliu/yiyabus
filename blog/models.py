#coding=utf-8

from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
from datetime import date
from yiyabus import settings
from mhlib import PATH

class User(models.Model):
    username = models.CharField(max_length = 30)
    headImg = models.FileField(upload_to = '.')

    def __unicode__(self):
        return self.username


class Demo(models.Model):
    seq = models.AutoField(primary_key = True)
    #title = models.CharField
    title = models.CharField(max_length = 100,default = "new show")
    pkg = models.FileField("Package",upload_to="./demos")
    desc = models.TextField(default = u"更新描述：")
    
    timestamp = models.DateTimeField()
    
    count = models.IntegerField(default = 0)
    version = models.CharField(max_length = 30,default = "2.2.0")

    #qr  =   models.URLField(default=u"http://不要编辑我.com")
    #qr = QRUrl
    
# Create your models here.
class QRUrl(models.Model):
    #seq = models.AutoField()
    url = models.URLField(default = "qq.com")
    #    stock   =   models.ForeignKey(Stock)

    demo =models.OneToOneField(Demo)
#admin.site.register(QRUrl)

class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    pkg = models.FileField('pkg',upload_to='./upload/')
    
    #qr = models.FileField('qr',upload_to= './qr/')


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
    
    


class DemoAdmin(admin.ModelAdmin):
#class DemoAdmin(CustomModelAdmin):
    list_filter = ('version',)

    list_display= ('title','seq')
    
#admin.site.register(BlogsPost,BlogPostAdmin)
admin.site.register(User)
admin.site.register(Demo,DemoAdmin)


from django.db.models.signals import post_save

import qrcode 

import yiyabus.settings
def makeQR(sender, instance,  **kwargs):
    print "sender:"+str(sender)
    print "instance:"+str(instance)
    #print created
    print "kwargs:"+str(kwargs)
    qr=qrcode.QRCode(
                     version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_H,     
                     box_size=10,     
                     border=4, )
    qr.add_data("http://112.74.14.144/media/"+str(instance.pkg))
    img=qr.make_image()
    qr_path=settings.MEDIA_ROOT+"/qr/"+ str(instance.seq)+".png"
    img.save(qr_path)
    #instance.qr = path
    #instance.save()
    #instance.qr.url=
    url=QRUrl()
    url.demo=instance
    url.url=qr_path
    url.save()
post_save.connect(makeQR, sender=Demo)

    
