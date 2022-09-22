from email.mime import image
from pickle import NONE
import profile
from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.


class Home(models.Model):
   name = models.CharField(max_length=100)
   picture = models.ImageField(upload_to='picture/')
   careers =  models.CharField(max_length=100, null=True)
   updated = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.name



class About(models.Model):
    experience= models.IntegerField(blank=True)
    jobs = models.CharField(max_length=100)
    description = models.TextField(max_length=500,blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __int__(self):
      return self.experience


class skill(models.Model):
    class Meta:
        verbose_name = 'skill'
    skill_description = models.CharField(max_length=200)
    skill_name = models.CharField(max_length=70, blank=True, null=True)
    score = models.IntegerField(default=90, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.skill_description


class services(models.Model):
    service_1_name = models.CharField(max_length=50)
    service_1_price = models.IntegerField(blank=True, )
    service_1_description = models.CharField(max_length=500)
    service_2_name = models.CharField(max_length=50, null=True)
    service_2_price = models.IntegerField(blank=True,null=True )
    service_2_description = models.CharField(max_length=500, null=True)
    service_3_name = models.CharField(max_length=50, null=True)
    service_3_price = models.IntegerField(blank=True, null=True )
    service_3_description = models.CharField(max_length=500, null=True)
    service_4_name = models.CharField(max_length=50, null=True)
    service_4_price = models.IntegerField(blank=True, null=True)
    service_4_description = models.CharField(max_length=500, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __int__(self):
      return self.service_1_name



class projects(models.Model):
    image = models.ImageField(upload_to = 'projects/')
    link = models.URLField(blank=False)
    
    def __str__(self):
      return str(self.id)


class team_members(models.Model):
    name = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=50, null=True)
    members_image = models.ImageField(upload_to = 'members/')
    members_link = models.URLField(blank=False)

    def __str__(self):
      return str(self.id)


class contact(models.Model):
    header = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
      return  self.header















































 
    