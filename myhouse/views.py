from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .forms import *


def home(request):
    template=loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context))

def register(request):
    if request.method == 'POST':
	in_form=CreateUserForm(request.POST)
	if in_form.is_valid():
	    new_user=User.objects.create_user(
		    in_form.cleaned_data['username'],
		    in_form.cleaned_data['email'],
		    in_form.cleaned_data['password'],
	    )
	    return HttpResponseRedirect('account/')
	else:
	    template=loader.get_template('err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	in_form=CreateUserForm()
	template='create_user.html'
	context={'form':in_form}
	return render(request,template,context)



def log_in(request):
    if request.method == 'POST':
#	login_form=LoginUserForm(request.POST)
	user=authenticate(
		username=request.POST['username'], 
		password=request.POST['password'])
	if user is not None:
	    login(request,user)
	    return HttpResponseRedirect('/account/')
#	    return HttpResponse(request,'account.home.html')
	else:
	    return HttpResponse('Wrong Credentials')
    else:
	login_form=LoginUserForm()
	template='login.html'
	context={'form':login_form}
	return render(request,template,context)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
