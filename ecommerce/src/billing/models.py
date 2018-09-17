from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from accounts.models import GuestEmail
# from django.contrib.auth.models import User
# Create your models here.

User = settings.AUTH_USER_MODEL

class BillingProfileManager(models.Manager):
    def new_or_get(self,request):
        user           = request.user
        guest_email_id = request.session.get('guest_email_id')
        created        = False
        obj            = None
        if user.is_authenticated:
            obj,created = BillingProfile.objects.get_or_create(
                user=user, email=user.email)
        elif guest_email_id is not None:
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            obj,created = BillingProfile.objects.get_or_create(
                email=guest_email_obj)
        else:
            pass
        return obj, created
        


class BillingProfile(models.Model):
    user        = models.OneToOneField(User,null=True,blank=True)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects     = BillingProfileManager()

    def __str__(self):
        return self.email


def user_created_receiver(sender, instance, created,*args,**kwargs):
    if created and instance.email:
        print(instance)
        BillingProfile.objects.get_or_create(user=instance,email=instance.email)

post_save.connect(user_created_receiver, sender=User)
