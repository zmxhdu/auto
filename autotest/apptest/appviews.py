from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from apptest.models import Appcase, Appcasestep
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required
def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(appcase_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        appcase_list = paginator.page(page)
    except PageNotAnInteger:
        appcase_list = paginator.page(1)
    except EmptyPage:
        appcase_list = paginator.page(paginator.num_pages)
    appcase_count = Appcase.objects.all().count()
    return render(request, "appcase_manage.html", {"user":username, "appcases":appcase_list, "appcasecounts":appcase_count})


@login_required
def appcasestep_manage(request):
    appcasestep_list = Appcasestep.objects.all()
    username = request.session.get('user', '')
    appcaseid = request.GET.get('appcase.id', None)
    appcsae = Appcase.objects.get(id=appcaseid)
    paginator = Paginator(appcasestep_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        appcasestep_list = paginator.page(page)
    except PageNotAnInteger:
        appcasestep_list = paginator.page(1)
    except EmptyPage:
        appcasestep_list = paginator.page(paginator.num_pages)
    return render(request, "appcasestep_manage.html", {"user":username, "appcsae":appcsae, "appcasesteps":appcasestep_list})


@login_required
def appcasesearch(request):
    username = request.session.get('user', '')
    search_appcasename = request.GET.get('appcasename', '')
    appcase_list = Appcase.objects.filter(appcasename__icontains=search_appcasename)
    return render(request, "appcase_manage.html", {"user":username, "appcases":appcase_list})


@login_required
def appcasestepsearch(request):
    username = request.session.get('user', '')
    search_appcasename = request.GET.get('appcasename', '')
    appcasestep_list = Appcasestep.objects.filter(appcasename__icontains=search_appcasename)
    return render(request, "appcasestep_manage.html", {"user":username, "appcasesteps":appcasestep_list})
