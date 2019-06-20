from django.contrib import admin
from product.models import Product
from apitest.models import Apitest, Apis
from apptest.models import Appcase


# Register your models here.
class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethon', 'apiresult', 'apistatus', 'create_time', 'id', 'product']
    model = Apis
    extra = 1


class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename','apptestresult','apptester','create_time','id','product']
    model = Appcase
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    inlines = [ApisAdmin, AppcaseAdmin]


admin.site.register(Product)
