from multiprocessing import context
from select import select
from turtle import home
from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp.models import *

# Create your views here.
def index(request):
    home = Home.objects.latest('updated')

    about = About.objects.latest('updated')
    skills = skill.objects.all()
    Service = services.objects.latest('updated')
    Project = projects.objects.all()
    Member = team_members.objects.all()
    Contacts= contact.objects.latest('updated')
    
    context = (
       {'home' : home,
       'about' : about,
       'skill' : skills,
       'service' : Service,
       'projects': Project,
       'contact': Contacts,
       'members': Member}

    )
   
    return render(request, 'index.html',context)

