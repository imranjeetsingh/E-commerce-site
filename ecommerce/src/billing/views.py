from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.utils.http import is_safe_url
from .models import BillingProfile, Card
from django.conf import settings

import stripe

STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY", "sk_test_G1XNXJeqKpZxor4XQDr0HwHI")

stripe.api_key = STRIPE_SECRET_KEY

STRIPE_PUB_KEY = getattr(settings,"STRIPE_PUB_KEY","pk_test_kS2vnlijzSUlFP7S86PsmzXf")
# Create your views here.
def payment_method_view(request):

    billing_profile, created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_ , request.get_host()):
        next_url = next_
    return render(request,"billing/payment-method.html",{"publish_key":STRIPE_PUB_KEY,"next_url":next_url})
    

def payment_method_createview(request):
    if request.method=="POST" and request.is_ajax():
        billing_profile, created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Can not find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            # customer = stripe.Customer.retrieve(billing_profile.customer_id)
            # card_response = customer.sources.create(source=token)
            new_card = Card.objects.add_new(billing_profile, token)
            print(new_card)
        return JsonResponse({"message":"Success!! Your card was added."})
    return HttpResponse("error", status_code=401)