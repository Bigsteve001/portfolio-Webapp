from turtle import home
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Home)
admin.site.register(About)
admin.site.register(skill)
admin.site.register(services)
admin.site.register(projects)
admin.site.register(team_members)
admin.site.register(contact)

