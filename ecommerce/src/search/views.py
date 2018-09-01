from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from products.models import Product


class SearchProductListView(ListView):
    # queryset        = Product.objects.all()
    template_name   = "search/view.html"

    def get_context_data(self, *args, **kwargs):
       context           = super(SearchProductListView, self).get_context_data(*args, **kwargs)
       context['query']  = self.request.GET.get("q")
       return context


    def get_queryset(self, *args, **kwargs):
        request     = self.request   
        method_dict = request.GET
        print(method_dict)
        query       = method_dict.get('q', None)
        # print(query)
        if query is not None:
            return Product.objects.search(query)