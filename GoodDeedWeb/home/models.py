from django.db import models
from django.conf import settings

# Create your models here.

class Donation(models.Model):
  title = models.CharField(max_length=30)
  phonenumber = models.CharField(max_length=12)
  category = models.CharField(max_length=20)
  quantity  = models.IntegerField(blank=True, null=True,)
  location = models.CharField(max_length=50, blank=True, null=True,)
  image = models.ImageField(null = True, blank = True, upload_to = 'images/')       
  description = models.TextField()
  date = models.CharField(blank=True, null=True, max_length=999)
  user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
  @property
  def imageURL(self):
    try:
      url = self.image.url
    except: 
      url = 'images/gooddeedplaceholderimage.png'
    return url




class Request(models.Model):
  title = models.CharField(max_length=30)
  phonenumber = models.CharField(max_length=12)
  category = models.CharField(max_length=20)
  quantity  = models.IntegerField(blank=True, null=True,)
  location = models.CharField(max_length=50, blank=True, null=True,)
  image = models.ImageField(null = True, blank = True, upload_to = 'images/')       
  description = models.TextField()
  date = models.CharField(blank=True, null=True, max_length=999)
  user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
  @property
  def imageURL(self):
    try:
      url = self.image.url
    except: 
      url = 'images/gooddeedplaceholderimage.png'
    return url









class UserDetail(models.Model):
  donations = models.IntegerField(blank=True, null = True,)
  points = models.IntegerField(blank=True, null = True,)
  requests = models.IntegerField(blank=True, null=True)
  user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
 

class Contact(models.Model):
  name = models.CharField(blank=True, null=True, max_length=45)
  subject = models.CharField(blank=True, null=True, max_length=55)
  email = models.EmailField(blank=True, null=True, max_length=30)
  content  = models.TextField()
  date = models.CharField(blank=True, null=True, max_length=999)