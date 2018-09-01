from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

from .views import ProductDeatailSlugView, ProductListView

urlpatterns = [
    url(r'^$',ProductListView.as_view(),name="list"),
    url(r'^(?P<slug>[\w-]+)/$',ProductDeatailSlugView.as_view(), name="detail"),
]
