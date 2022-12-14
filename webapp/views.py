from multiprocessing import context
from pickle import FALSE
from select import select
from turtle import home
from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp.models import *
from django.core.mail import send_mail
import socket
socket.getaddrinfo('localhost', 8000)

# Create your views here.
def index(request):
    home = Home.objects.latest('updated')

    about = About.objects.latest('updated')
    skills = skill.objects.all()
    Service = services.objects.latest('updated')
    Project = projects.objects.all()
    Member = team_members.objects.all()
    Contacts= contact.objects.latest('updated')
    Experience=experience.objects.all()
    Education = education.objects.all()
    context =( {'home' : home,
       'about' : about,
       'skill' : skills,
       'service' : Service,
       'projects': Project,
       'contact': Contacts,
       'members': Member,
       'experience':Experience,
       'education':Education,
       })
    if request.method=="POST":
      Form=form()
      name=request.POST.get('name')
      from_email=request.POST.get('email')
      subject=request.POST.get('subject')
      message=request.POST.get('message')
      Form.name=name
      Form.email=from_email
      Form.subject=subject
      Form.message=message
      Form.save()

      send_mail(
         name ,
         subject + "\n" + message,
         from_email,
         ['stephenkingsoft1@gmail.com'])
      
      return HttpResponse('Thanks For Contacting Us')
      
    
   
    return render(request, 'index.html',context)




