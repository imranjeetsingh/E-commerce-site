from django.conf import settings


from django.conf.urls import url

from .views import cart_home, cart_update,checkout_done_view ,checkout

urlpatterns = [
    url(r'^$',cart_home,name='home'),
    url(r'^update/$',cart_update, name="update"),
    url(r'^checkout/$',checkout, name="checkout"),
    url(r'^checkout/success/$',checkout_done_view, name="success"),
]
