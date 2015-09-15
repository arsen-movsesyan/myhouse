from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.decorators import login_required

from datetime import date

from account.forms import AddEditAccountForm,TimeWatchForm,AccessFormSet,AccountPaymentForm
from account.forms import AccountAttributeValueForm
from account.models import Account,AccountUserPermission,AccountTimeWatch,AccountPaymentHistory
from account.models import AccountAttributeValue
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
	accounts = Account.objects.filter(created_by=house_user).filter(disabled = False)
	context['view_method'] = 'active'
    elif view_filter == 'time_watch':
	accounts = Account.objects.filter(created_by=house_user).filter(disabled = False).filter(time_watch=True)
	context['view_method'] = 'time_watch'
    context['all_accounts'] = accounts
    context['username'] = request.session['username']
    return HttpResponse(template.render(context))

@login_required
def view_account(request,in_acct_id):
    in_form = AccountAttributeValueForm(request.POST or None)
    account = Account.objects.get(pk=in_acct_id)
    if request.method =='POST':
	if in_form.is_valid():
	    attribute = in_form.cleaned_data['attribute']
	    value = in_form.cleaned_data['value']
	    new_attr = AccountAttributeValue.objects.create(
		account = account,
		attribute = attribute,
		value = value
	    )
#	    print in_form.cleaned_data
	    return HttpResponseRedirect("/account/view/"+in_acct_id)
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    template = "account/view_account.html"
    
    context=dict()
    attributes = account.attributes.all()
    context['account'] = account
    context['attributes'] = attributes
    context['form'] = in_form
    context['username'] = request.session['username']
    return render(request,template,context)


@login_required
def account_attribute_delete(request,in_acct_id,in_attr_map_id):
    attr_map = AccountAttributeValue.objects.get(pk=in_attr_map_id)
    attr_map.delete()
    return HttpResponseRedirect("/account/view/{0}".format(in_acct_id))



@login_required
def add_account(request):
    main_user = request.user.house_user
    other = main_user.get_other_users()
    if request.method == 'POST':
	in_form = AddEditAccountForm(request.POST)
	access_formset = AccessFormSet(request.POST)
	if access_formset.is_valid() and in_form.is_valid():
	    new_acct = Account.objects.create(
		acct_name = in_form.cleaned_data['acct_name'],
		login_url = in_form.cleaned_data['login_url'],
		created_by = request.user.house_user,
		acct_type = in_form.cleaned_data['acct_type'],
	    )
	    if 'access_login' in in_form.cleaned_data:
		new_acct.access_login = in_form.cleaned_data['access_login']
	    if 'access_password' in in_form.cleaned_data:
		new_acct.access_password = in_form.cleaned_data['access_password']
	    if 'brief' in in_form.cleaned_data:
		new_acct.brief = in_form.cleaned_data['brief']
	    if 'description' in in_form.cleaned_data:
		new_acct.description = in_form.cleaned_data['description']
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
	    return HttpResponseRedirect("/account/")
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
    context['action'] = 'add'
    context['username'] = request.session['username']
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
	    account_obj.acct_name = in_form.cleaned_data['acct_name']
	    account_obj.login_url = in_form.cleaned_data['login_url']
	    account_obj.acct_type = in_form.cleaned_data['acct_type']

	    if 'access_login' in in_form.cleaned_data:
		account_obj.access_login = in_form.cleaned_data['access_login']
	    if 'access_password' in in_form.cleaned_data:
		account_obj.access_password = in_form.cleaned_data['access_password']
	    if 'brief' in in_form.cleaned_data:
		account_obj.brief = in_form.cleaned_data['brief']
	    if 'description' in in_form.cleaned_data:
		account_obj.description = in_form.cleaned_data['description']
	    if 'disabled' in in_form.cleaned_data:
		account_obj.description = in_form.cleaned_data['disabled']
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
	init_form_data = {
	    'id':access_map.pk,
	    'user_name':house_user, # This is for display purposes
	    'user_id':house_user.pk,
	    'can_view':access_map.can_view,
	    'can_manage':access_map.can_manage,
	    'can_edit':access_map.can_edit}
	init_formset_data.append(init_form_data)
    access_formset = AccessFormSet(initial=init_formset_data)
    context = {'form':in_form,'tw_form':tw_form,'access_formset':access_formset}
    context['action'] = 'edit'
    context['username'] = request.session['username']
    return render(request,template,context)


@login_required
def delete_account(request,in_acct_id):
    acct_to_delete = Account.objects.get(pk=in_acct_id)
    acct_to_delete.delete()
    return HttpResponseRedirect("/account/")


@login_required
def view_time_watch(request):
    house_user = request.user.house_user
    template = loader.get_template("account/view_time_watch.html")
    ret_array = []
    accounts = Account.objects.filter(created_by=house_user).filter(disabled = False).filter(time_watch=True)
    for acct_obj in accounts:
	if acct_obj.t_watch.disabled:
	    continue
	info = dict()
	info['obj'] = acct_obj
	d_d_d=acct_obj.t_watch.get_due_date()
	info['due_date'] = d_d_d['due_date']
	info['days_left'] = d_d_d['days_left']
	info['show_payment'] = d_d_d['show_payment']
	info['auto_payment'] = d_d_d['auto_payment']
	info['color'] = d_d_d['color']
	ret_array.append(info)


    context = {'accounts':ret_array}
    context['username'] = request.session['username']
    return HttpResponse(template.render(context))


@login_required
def make_time_watch(request,in_acct_id):
    edit_account = Account.objects.get(pk=in_acct_id)
    if request.method == 'POST':
	in_form = TimeWatchForm(request.POST)
	if in_form.is_valid():
	    if edit_account.time_watch == True:
		new_time_watch = edit_account.t_watch
		new_time_watch.disabled = in_form.cleaned_data['disabled']
		new_time_watch.auto_payment = in_form.cleaned_data['auto_payment']
	    else:
		edit_account.time_watch = True
		edit_account.save()
		new_time_watch = AccountTimeWatch.objects.create(
		    account = edit_account,
		    auto_payment = in_form.cleaned_data['auto_payment']
		)
	    if 'month_frequency' in in_form.cleaned_data:
		new_time_watch.month_frequency = in_form.cleaned_data['month_frequency']
	    if 'due_month_day' in in_form.cleaned_data:
		new_time_watch.due_month_day = in_form.cleaned_data['due_month_day']
	    if 'initial_payment_date' in in_form.cleaned_data:
		new_time_watch.initial_payment_date = in_form.cleaned_data['initial_payment_date']
	    new_time_watch.save()

	    return HttpResponseRedirect("/account/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "account/make_timewatch.html"    
    in_form = TimeWatchForm(instance=edit_account.t_watch)
    context = {'form':in_form}
    context['username'] = request.session['username']
    return render(request,template,context)


@login_required
def acknowledge(request,in_acct_id):
    account = AccountTimeWatch.objects.get(pk=in_acct_id)
    if request.method == 'POST':
	in_form = AccountPaymentForm(request.POST)
	if in_form.is_valid():
	    payment_history = AccountPaymentHistory.objects.create(
		account=account,
		payment_date=in_form.cleaned_data['payment_date'],
		skip=in_form.cleaned_data['skip']
	    )
	    if in_form.cleaned_data['skip']:
		payment_history.confirmation_code = 'Void Acknowledged'
	    else:
		payment_history.confirmation_code = in_form.cleaned_data['confirmation_code']
		payment_history.payment_amount = in_form.cleaned_data['payment_amount']
	    payment_history.save() 
	    return HttpResponseRedirect("/account/view_time_watch")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "account/acknowledge.html"
    in_form = AccountPaymentForm()
    context = {'account':account,'form':in_form}
    context['username'] = request.session['username']
    return render(request,template,context)


@login_required
def view_payment_history(request,in_acct_id):
    account = AccountTimeWatch.objects.get(pk=in_acct_id)
    payments = account.payment_history.all()
    template = loader.get_template("account/view_payment_history.html")
    context = {'account':account,'payments':payments}
    return HttpResponse(template.render(context))
