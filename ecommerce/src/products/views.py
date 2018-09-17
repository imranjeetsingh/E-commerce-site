from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from carts.models import Cart
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

    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart']= cart_obj
        return context
    

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

class ProductDeatailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDeatailSlugView,self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart']= cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug    = self.kwargs.get("slug")
        try:
            instance = Product.objects.get(slug = slug , active = True)
        except Product.DoesNotExist:
            raise Http404("Not hii Found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug =slug, active = True)
            instance = qs.first()
        except:
            raise Http404("Uhoohohoohohoho")
        return instance