from django.shortcuts import render
from django.views import generic
from .models import Products, Comment
from django.urls import reverse_lazy
from .forms import CommentForm
from django.shortcuts import get_object_or_404, reverse
from cart.forms import AddToCartProductForm


class ProductsListView(generic.ListView):
    model = Products
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductsDetailView(generic.DetailView):
    model = Products
    template_name = 'products/products_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['add_to_cart_form'] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Products, id=product_id)
        obj.product = product
        return super().form_valid(form)
