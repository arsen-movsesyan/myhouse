from django.shortcuts import render
#from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

# Create your views here.

def home(request):
    template=loader.get_template('account/home.html')
    return HttpResponse(template.render())
#    return HttpResponse("Welcome")

def profile(request):
    return HttpResponse("Profile Editing Page")
