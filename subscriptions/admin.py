from django.contrib import admin

from subscriptions.models import (
    Subscriptions,
    SubscriptionPrice
)

admin.site.register(Subscriptions)
admin.site.register(SubscriptionPrice)