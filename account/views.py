from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.decorators import login_required

from datetime import date

from account.forms import AddEditAccountForm,TimeWatchForm,AccessFormSet
from account.models import Account,AccountUserPermission
from config.models import AccountType
from people.models import HouseUser



@login_required
def view_accounts(request,view_filter='active'):
    house_user = request.user.house_user
    template = loader.get_template("account/view_accounts.html")
    context = dict()
    if view_filter == 'all':
	accounts = Account.objects.filter(created_by=house_user)
# Add all other with 'can_view' permission
	context['view_method'] = 'all'
    elif view_filter == 'active':
	accounts = Account.objects.filter(disabled = False)
	context['view_method'] = 'active'
    context['all_accounts'] = accounts
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))

@login_required
def view_account(request,in_acct_id):
    account = Account.objects.get(pk=in_acct_id)
    template = loader.get_template("account/view_account.html")
    context=dict()
    context['account'] = account
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))



@login_required
def add_account(request):
    main_user = request.user.house_user
    other = main_user.get_other_users()
    if request.method == 'POST':
	in_form = AddEditAccountForm(request.POST)
#	tw_form = TimeWatchForm(request.POST)
	access_formset = AccessFormSet(request.POST)
	if access_formset.is_valid() and in_form.is_valid():
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
		new_acct.access_password = in_form.cleaned_data['access_password']
	    new_acct.save()

	    for access_form in access_formset:
		user_pk = int(access_form.cleaned_data['user_id'])
		can_edit = access_form.cleaned_data['can_edit']
		can_view = access_form.cleaned_data['can_view']
		can_manage = access_form.cleaned_data['can_manage']

		access_user = HouseUser.objects.get(pk=user_pk)
		access_map = AccountUserPermission.objects.create(
		    account = new_acct,
		    user = access_user,
		    can_view = can_view,
		    can_manage = can_manage,
		    can_edit =can_edit
		)
#		print access_form.cleaned_data
	    return HttpResponseRedirect("/account/")
#	    return HttpResponseRedirect("#")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "account/add_edit_account.html"
    in_form = AddEditAccountForm()
    tw_form = TimeWatchForm()
    init_formset_data = []
    
    for person in other:

#########################
# First field is made by VoidWidget to display username AS part of form
#########################
	init_form_data={
	    'id':None,
	    'user_name':person.user, # This is for display purposes
	    'user_id':person.user.pk,
	    'can_view':True,
	    'can_manage':True,
	    'can_edit':False}
	init_formset_data.append(init_form_data)
    access_formset = AccessFormSet(initial=init_formset_data)
    context = {'form':in_form,'tw_form':tw_form,'access_formset':access_formset}
    context['username'] = request.session['user_name']
    return render(request,template,context)




@login_required
def edit_account(request,in_acct_id):
    account_obj = Account.objects.get(pk=in_acct_id)
    main_user = request.user.house_user
    other = main_user.get_other_users()
    if request.method == 'POST':
	in_form = AddEditAccountForm(request.POST)
#	tw_form = TimeWatchForm(request.POST)
	access_formset = AccessFormSet(request.POST)
	if access_formset.is_valid() and in_form.is_valid():
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

	    for access_form in access_formset:
		access_map_pk = int(access_form.cleaned_data['id'])
		can_edit = access_form.cleaned_data['can_edit']
		can_view = access_form.cleaned_data['can_view']
		can_manage = access_form.cleaned_data['can_manage']

		access_map = AccountUserPermission.objects.get(pk=access_map_pk)
		access_map.can_view = can_view
		access_map.can_manage = can_manage
		access_map.can_edit = can_edit
		access_map.save()
	    return HttpResponseRedirect("/account/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "account/add_edit_account.html"
    in_form = AddEditAccountForm(instance=account_obj)
    tw_form = TimeWatchForm()
    init_formset_data = []

    for person in other:
	house_user = person.user
	access_map = AccountUserPermission.objects.filter(account=account_obj).get(user=house_user)

#########################
# First field is made by VoidWidget to display username AS part of form
#########################
	init_form_data={
	    'id':access_map.pk,
	    'user_name':house_user, # This is for display purposes
	    'user_id':house_user.pk,
	    'can_view':access_map.can_view,
	    'can_manage':access_map.can_manage,
	    'can_edit':access_map.can_edit}
	init_formset_data.append(init_form_data)
    access_formset = AccessFormSet(initial=init_formset_data)
    context = {'form':in_form,'tw_form':tw_form,'access_formset':access_formset}
    context['username'] = request.session['user_name']
    return render(request,template,context)


@login_required
def delete_account(request,in_acct_id):
    acct_to_delete = Account.objects.get(pk=in_acct_id)
    acct_to_delete.delete()
    return HttpResponseRedirect("/account/")


@login_required
def view_time_watch(request):
    return HttpResponseRedirect("/account/")


