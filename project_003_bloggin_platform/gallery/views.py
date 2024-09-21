from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductForm 


def product_list(request):
    products = Product.objects.all()
    return render(request, 'gallery/index.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'gallery/index2.html', {'product': product})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'gallery/edit.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'gallery/delete.html', {'product': product})


def home(request):
    return HttpResponse('Hello, World!')


def add_product(request):
    product = get_object_or_404(Product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # add product to database
            form.save()
            return redirect('product_list')
    form = ProductForm()
    page = {
        "form": form,
    }
    return render(request, 'gallery/add.html', page)
