from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description # this works but it isn't good practice to name the objects and match them exactly because they can change in models. Better way is to map object
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    # obj = Product.objects.get(id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)
