"""
autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from apitest import views
from product import proviews
from bug import bugviews
from set import setviews
from apptest import appviews
from webtest import webviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('logout/', views.logout),
    path('product_manage/', proviews.product_manage),
    path('apitest_manage/', views.apitest_manage),
    path('apistep_manage/', views.apistep_manage, name='apistep_manage'),
    path('apis_manage/', views.apis_manage),
    path('bug_manage/', bugviews.bug_manage),
    path('set_manage/', setviews.set_manage),
    path('user/', setviews.set_user),
    path('appcase_manage/', appviews.appcase_manage),
    path('appcasestep_manage/', appviews.appcasestep_manage, name='appcasestep_manage'),
    path('webcase_manage/', webviews.webcase_manage),
    path('webcasestep_manage/', webviews.webcasestep_manage, name='webcasestep_manage'),
    path('left/', views.left),
    path('apisearch/', views.apisearch),
    path('setsearch/', setviews.setsearch),
    path('productsearch/', proviews.productsearch),
    path('bugsearch/', bugviews.bugsearch),
    path('appcasesearch/', appviews.appcasesearch),
    path('appcasestepsearch/', appviews.appcasestepsearch),
    path('webcasesearch/', webviews.webcasesearch),
    path('webcasestepsearch/', webviews.webcasestepsearch),
    path('usersearch/', setviews.usersearch),
    path('welcome/', views.welcome),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
