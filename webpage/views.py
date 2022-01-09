from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
import csv


def list_products(request):
    products = Product.objects.all()
    return render( request, 'products.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render( request, 'products-form.html', {'form': form})


def update_product( request, id):
    product = Product.objects.get(id=id)
    form = ProductForm( request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})


def export(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Description', 'Price', 'Quantity'])

    for product in Product.objects.all().values_list('description', 'price', 'quantity'):
        writer.writerow(product)

    response['Content-Disposition'] = 'attachment; filename = "products.csv"'

    return response
