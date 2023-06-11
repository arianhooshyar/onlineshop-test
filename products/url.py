from django.urls import path
from .views import ProductsListView, ProductsDetailView, CommentCreateView

urlpatterns = [
    path('', ProductsListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='product_Detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
]
