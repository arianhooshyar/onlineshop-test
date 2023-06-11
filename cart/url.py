from django.urls import path
from .views import cart_detail_view, add_cart_view

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', add_cart_view, name='add_cart'),
]
