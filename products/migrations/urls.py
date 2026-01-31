from products.views import ProductListView

urlpatterns = [
    path('products/' , ProductListView.as_view()),
]