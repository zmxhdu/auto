from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required



# Create your views here.
def product_manage(request):
    username = request.session.get('user', '')
    product_list = Product.objects.all()
    return render(request, "product_manage.html", {"user": username,"products": product_list})


@login_required
def productsearch(request):
    username = request.session.get('user', '')
    search_productname = request.GET.get('productname', '')
    product_list = Set.objects.filter(productname__icontains=search_productname)
    return render(request, "product_manage.html", {"user":username, "products":product_list})

