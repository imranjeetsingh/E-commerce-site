from django.contrib import admin
from .models import MarketingPreference
# Register your models here.

class MarketingPreferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__','subscribed', 'update']
    readonly_fields = ['mailchimp_subscribed', 'timestamp','update']
    class Meta:
        model = MarketingPreference
        fields = [
            'user',
            'subscribed',
            'mailchimp_subscribed',
            'timestamp',
            'update'
        ]

admin.site.register(MarketingPreference,MarketingPreferenceAdmin)