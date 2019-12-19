from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from apitest.models import Apitest, Apistep, Apis
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    #else:
    #    context = {}
    #    return render(request, 'login.html', context)

    return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request,'login.html', {'error': '请先登录'})


def logout(request):
    return render(request, 'login.html')


@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(apitest_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        apitest_list = paginator.page(page)
    except PageNotAnInteger:
        apitest_list = paginator.page(1)
    except EmptyPage:
        apitest_list = paginator.page(paginator.num_pages)
    apitest_count = Apitest.objects.all().count()
    return render(request, "apitest_manage.html", {"user":username, "apitests":apitest_list, "apitestcounts": apitest_count})


@login_required
def apistep_manage(request):
    apistep_list = Apistep.objects.all()
    username = request.session.get('user', '')
    apitestid = request.GET.get('apitest.id', None)
    apitest = Apitest.objects.get(id=apitestid)
    paginator = Paginator(apistep_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        apistep_list = paginator.page(page)
    except PageNotAnInteger:
        apistep_list = paginator.page(1)
    except EmptyPage:
        apistep_list = paginator.page(paginator.num_pages)
    return render(request, "apistep_manage.html", {"user":username, "apitest":apitest, "apisteps":apistep_list})


@login_required
def apis_manage(request):
    apis_list = Apis.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(apis_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        apis_list = paginator.page(page)
    except PageNotAnInteger:
        apis_list = paginator.page(1)
    except EmptyPage:
        apis_list = paginator.page(paginator.num_pages)
    apis_count = Apis.objects.all().count()
    return render(request, "apis_manage.html", {"user":username, "apiss":apis_list, "apiscounts":apis_count})


@login_required
def apisearch(request):
    username = request.session.get('user', '')
    search_apitestname = request.GET.get('apitestname', '')
    apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request, "apitest_manage.html", {"user":username, "apitests":apitest_list})


def left(request):
    return render(request, "left.html")


def welcome(request):
    return render(request, "welcome.html")
