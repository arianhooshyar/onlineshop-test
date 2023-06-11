from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .cart import Card
from .forms import AddToCartProductForm
from products.models import Products


def cart_detail_view(request):
    cart = Card(request)
    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
    })


def add_cart_view(request, product_id):
    cart = Card(request)
    product = get_object_or_404(Products, id=product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)
      #  return HttpResponse()
    return redirect('cart_detail')
