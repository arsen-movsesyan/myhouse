from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from config.models import AccountType

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from config.models import AccountType
from config.forms import AddEditAccountTypeForm

# Create your views here.



@login_required
def view_all_objects(request):
    template = loader.get_template("config/all_objects.html")
    return HttpResponse(template.render())


@login_required
def manage_acct_type(request):
    acct_types = AccountType.objects.all()
    context = dict()
    template = "config/manage_acct_types.html"
    context['types'] = acct_types
    return render(request,template,context)


@login_required
def add_acct_type(request):
    if request.method == 'POST':
	in_form = AddEditAccountTypeForm(request.POST)
	if in_form.is_valid():
	    new_type = AccountType.objects.create(
		type_name = in_form.cleaned_data['type_name'],
		brief = in_form.cleaned_data['brief']
	    )
	    if 'description' in in_form.cleaned_data:
		new_type.description = in_form.cleaned_data['description']
		new_type.save()
	    return HttpResponseRedirect("/config/acct_type")
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    in_form = AddEditAccountTypeForm()
    template = "config/add_edit_acct_type.html"
    context = {'form':in_form}
    return render(request,template,context)

@login_required
def edit_acct_type(request,in_type_id):
    acct_type = AccountType.objects.get(pk=in_type_id)
    if request.method == 'POST':
	in_form = AddEditAccountTypeForm(request.POST)
	if in_form.is_valid():
	    acct_type.type_name = in_form.cleaned_data['type_name']
	    acct_type.brief = in_form.cleaned_data['brief']
	    
	    if 'description' in in_form.cleaned_data:
		acct_type.description = in_form.cleaned_data['description']
	    acct_type.save()
	    return HttpResponseRedirect("/config/acct_type")
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    in_form = AddEditAccountTypeForm(instance=acct_type)
    template = "config/add_edit_acct_type.html"
    context = {'form':in_form}
    return render(request,template,context)

