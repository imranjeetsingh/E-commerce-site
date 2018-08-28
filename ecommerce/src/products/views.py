from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView


from .models import Product
# Create your views here.

class ProductFeaturedListView(ListView):
    queryset        = Product.objects.all().featured()
    template_name   = "products/list.html"
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductFeaturedDeatailView(DetailView):
    queryset        = Product.objects.all().featured()
    template_name   = "products/featured-detail.html"
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()
    
class ProductListView(ListView):
    queryset        = Product.objects.all()
    template_name   = "products/list.html"
    

class ProductDeatailView(DetailView):
    # queryset        = Product.objects.all()
    template_name   = "products/detail.html"
    # print(queryset)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDeatailView, self).get_context_data(*args, **kwargs)
    #     return context

    def get_object(self, *args, **kwargs):
        # print(args)
        # print(kwargs)
        # request = self.request
        pk      = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance
    
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk      = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)