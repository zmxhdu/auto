from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from webtest.models import Webcase, Webcasestep


# Create your views here.
@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user', '')
    return render(request, "webcase_manage.html", {"user":username, "webcases":webcase_list})


@login_required
def webcasestep_manage(request):
    webcasestep_list = Webcasestep.objects.all()
    username = request.session.get('user', '')
    return render(request, "webcasestep_manage.html", {"user":username, "webcasesteps":webcasestep_list})


@login_required
def webcasesearch(request):
    username = request.session.get('user', '')
    search_webcasename = request.GET.get('webcasename', '')
    webcase_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request, "webcase_manage.html", {"user":username, "webcases":webcase_list})


@login_required
def webcasestepsearch(request):
    username = request.session.get('user', '')
    search_webcasename = request.GET.get('webcasename', '')
    webcasestep_list = Webcasestep.objects.filter(webcasename__icontains=search_webcasename)
    return render(request, "webcasestep_manage.html", {"user":username, "webcasesteps":webcasestep_list})
