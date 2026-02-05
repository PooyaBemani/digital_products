from products.views import ProductListView, ProductDetailView
from django.urls import path

urlpatterns = [
    path('products/' , ProductListView.as_view() , name = 'products_list'),
    path('products/<int:pk>/' , ProductDetailView.as_view() , name = 'product_detail'),
]