from django.shortcuts import render
from set.models import Set
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def set_manage(request):
    username = request.session.get('user', '')
    set_list = Set.objects.all()
    return render(request, "set_manage.html", {"user": username,"sets": set_list})


def set_user(request):
    username = request.session.get('user', '')
    use_list = User.objects.all()
    return render(request, "set_user.html", {"user": username,"users": use_list})


@login_required
def setsearch(request):
    username = request.session.get('user', '')
    search_setname = request.GET.get('setname', '')
    set_list = Set.objects.filter(setname__icontains=search_setname)
    return render(request, "set_manage.html", {"user":username, "sets":apitest_list})


@login_required
def usersearch(request):
    username = request.session.get('user', '')
    search_username = request.GET.get('username', '')
    user_list = User.objects.filter(username__icontains=search_username)
    return render(request, "user_manage.html", {"user":username, "users":apitest_list})
