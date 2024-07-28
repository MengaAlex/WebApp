from . import views
from django.urls import path

urlpatterns = [
    path('', views.shop, name='shop'),
    path('caps', views.caps, name='caps'),
    path('shirts', views.shirts, name='shirts'),
    path('<int:pk>', views.Details_product.as_view(), name='details_product'),
    path('search/', views.Search.as_view(), name='search')
]