from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from config.models import AccountType

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from config.models import AccountType

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