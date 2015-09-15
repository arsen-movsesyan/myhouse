from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from datetime import date



from .forms import CreateUserForm,LoginUserForm

from account.models import HouseUser
from people.models import Household,MapUserHousehold


def _index(request):
    template=loader.get_template('base/index.html')
    context={}
    return HttpResponse(template.render(context))


def self_register(request):
    if request.method == 'POST':
	in_form=CreateUserForm(request.POST)
	if in_form.is_valid():
	    email = in_form.cleaned_data['email']
	    username = email
	    password = in_form.cleaned_data['password']
	    auth_user = User.objects.create_user(
		username,
		email,
		password
	    )
	    ssn=in_form.cleaned_data['complete_ssn']
	    household_user = HouseUser.objects.create(
		auth_user = auth_user,
		created_by = auth_user.id,
		dob = in_form.cleaned_data['dob'],
		sex = in_form.cleaned_data['sex'],
		ssn_13 = ssn[0:3],
		ssn_45 = ssn[4:6],
		ssn_69 = ssn[7:11],
		first_name = in_form.cleaned_data['first_name'],
		last_name = in_form.cleaned_data['last_name'],
		email = email,
		title = in_form.cleaned_data['title'],
		suffix = in_form.cleaned_data['suffix'],
	    )
#	    household_user.save()
	    new_household = Household.objects.create()
	    map_user_household = MapUserHousehold.objects.create(
		user = household_user,
		household = new_household,
		hh_superuser = True,
	    )


	    user = authenticate(username=username, password=password)    
	    login(request,user)
	    request.session['household_id'] = new_household.id
	    request.session['username'] = user.house_user.first_name
#	    print user.house_user.first_name
	    return HttpResponseRedirect('account/')
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	in_form = CreateUserForm()
	template = 'base/register_user.html'
	context = {'form':in_form}
	return render(request,template,context)



def log_in(request):
    if request.method == 'POST':
	user = authenticate(
		username = request.POST['email'], 
		password = request.POST['password'])
	if user is not None and user.is_active:
	    login(request,user)
	    request.session['user_id'] = user.id
	    household_id = user.house_user.user_map.household.id
	    request.session['household_id'] = household_id
	    request.session['username'] = user.house_user.first_name
#	    print user.house_user.first_name
	    return HttpResponseRedirect('/account/')
	else:
	    return HttpResponse('Wrong Credentials')
    else:
	login_form = LoginUserForm()
	template = 'base/login.html'
	context = {'form':login_form}
	return render(request,template,context)


def log_out(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect('/')

