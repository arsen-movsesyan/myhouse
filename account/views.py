from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User



from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

#from django.http import JsonResponse

from .models import HouseUser
#from .forms import ProfileForm


# Create your views here.

@login_required
def home(request):
    template = loader.get_template('account/home.html')
    return HttpResponse(template.render())
#    return HttpResponse("Welcome")

"""

@login_required
def view_profile(request):
    if not request.user.profile_obj:
	return HttpResponseRedirect("edit_profile")

@login_required
def edit_profile(request):
    if request.method == 'POST':
	in_form = ProfileForm(request.POST)
	if in_form.is_valid():

@login_required
def view_profile(request):
    if not request.user.profile_obj:
	profile_form = ProfileForm()
	template = 'account/create_profile.html'
	context = {'form':profile_form}
	return render(request,template,context)
    if request.method == 'POST':
	in_form = ProfileForm(request.POST)
	if in_form.is_valid():
	    
	    template=loader.get_template('account/view_profile.html')
	    context={'profile':in_form}
	    return HttpResponse(template.render(context))
	else:
	    pass
    template=loader.get_template('account/view_profile.html')
    context={'form':in_form}
	    return HttpResponse(template.render(context))
    
    return HttpResponse("Profile Editing Page")



"""
