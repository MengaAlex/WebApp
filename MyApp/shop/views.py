from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, ListView


def shop(request):
    product = Product.objects.order_by('-date')[:8]
    return render(request, "shop/shop.html", {'product': product})

def caps(request):
    product = Product.objects.filter(type = 'cap').order_by('-date')
    return render(request, "shop/shop_caps.html", {'product': product})

def shirts(request):
    product = Product.objects.filter(type = 'shirts').order_by('-date')
    return render(request, "shop/shop_shirts.html", {'product': product})

class Details_product(DetailView):
    model = Product
    template_name = 'shop/details_product.html'
    context_object_name = 'details_product'

class Search(ListView):
    template_name = "shop/shop.html"
    context_object_name = "product"
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context 