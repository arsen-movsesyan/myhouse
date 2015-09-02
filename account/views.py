from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.decorators import login_required

from datetime import date



#from account.forms import AddEditUserForm,AddressForm

from account.forms import AddEditAccountForm,TimeWatchForm,AccountUserPermissionForm
from account.models import Account
from config.models import AccountType



@login_required
def view_accounts(request,view_filter='active'):
    house_user = request.user.house_user
    template = loader.get_template("account/view_accounts.html")
    context = dict()
    if view_filter == 'all':
	accounts = Account.objects.filter(created_by=house_user.user_id)
#	accounts = Account.objects.all()
	context['view_method'] = 'all'
    elif view_filter == 'active':
	accounts = Account.objects.filter(disabled = False)
	context['view_method'] = 'active'
    context['all_accounts'] = accounts
    return HttpResponse(template.render(context))

@login_required
def view_account(request,in_acct_id):
    account = Account.objects.get(pk=in_acct_id)
    template = loader.get_template("account/view_account.html")
    context=dict()
    context['account'] = account
    return HttpResponse(template.render(context))



@login_required
def add_account(request):
    main_user = request.user.house_user
    if request.method == 'POST':
	in_form = AddEditAccountForm(request.POST)
	if in_form.is_valid():
	    acct_type = AccountType.objects.get(type_name=in_form.cleaned_data['acct_type'])
	    new_acct = Account.objects.create(
		acct_name = in_form.cleaned_data['acct_name'],
		login_url = in_form.cleaned_data['login_url'],
		created_by = request.user.house_user,
		acct_type = acct_type,
	    )
	    if not in_form.cleaned_data['access_login'] == None:
		new_acct.access_login = in_form.cleaned_data['access_login']
	    if not in_form.cleaned_data['access_password'] == None:
		new_acct.access_login = in_form.cleaned_data['access_password']
	    new_acct.save()
	    return HttpResponseRedirect("/account/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "account/add_edit_account.html"
    in_form = AddEditAccountForm()
    tw_form = TimeWatchForm()
    access_form = AccountUserPermissionForm(initial={'can_view':True,'can_manage':True,'can_edit':False})
    other = main_user.get_other_users()
    context = {'form':in_form,'tw_form':tw_form,'other':other,'access_form':access_form}
    return render(request,template,context)


@login_required
def edit_account(request,in_acct_id):
    account_obj = Account.objects.get(pk=in_acct_id)
    if request.method == 'POST':
	in_form = AddEditAccountForm(request.POST)
	if in_form.is_valid():
	    acct_type = AccountType.objects.get(type_name=in_form.cleaned_data['acct_type'])
	    account_obj.acct_name = in_form.cleaned_data['acct_name']
	    account_obj.login_url = in_form.cleaned_data['login_url']
	    account_obj.acct_type = acct_type

	    if in_form.cleaned_data['disabled']:
		account_obj.disabled = True
		account_obj.disabled_date = date.today()
	    if not in_form.cleaned_data['access_login'] == None:
		account_obj.access_login = in_form.cleaned_data['access_login']
	    if not in_form.cleaned_data['access_password'] == None:
		account_obj.access_password = in_form.cleaned_data['access_password']
	    account_obj.save()
	    return HttpResponseRedirect("/account/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "account/add_edit_account.html"
    in_form = AddEditAccountForm(instance=account_obj)
    context = {'form':in_form}
    return render(request,template,context)


@login_required
def view_time_watch(request):
    return HttpResponseRedirect("/account/")
